import os
import re
import sys
import json
from bs4 import BeautifulSoup

def audit_site(web_dir):
    print(f"Iniciando auditoria no diretório: {web_dir}")
    html_files = []
    for root, dirs, files in os.walk(web_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    report = []
    report.append("# 📋 Relatório de Auditoria Impeccable")
    report.append(f"Arquivos analisados: {len(html_files)}\n")

    for file_path in html_files:
        rel_path = os.path.relpath(file_path, web_dir).replace('\\', '/')
        report.append(f"## 📄 Arquivo: [web/{rel_path}](file:///{file_path.replace(os.sep, '/')})")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Meta tags
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else "AUSENTE"
        report.append(f"- **Title**: {title} (Tamanho: {len(title) if title_tag else 0} chars)")
        if title_tag and len(title) > 60:
            report.append("  - ⚠️ *Aviso*: Title longo (> 60 chars)")

        desc_tag = soup.find('meta', attrs={'name': 'description'})
        desc = desc_tag['content'] if desc_tag and desc_tag.has_attr('content') else "AUSENTE"
        report.append(f"- **Description**: {desc} (Tamanho: {len(desc) if desc_tag else 0} chars)")
        if desc_tag and len(desc) > 160:
            report.append("  - ⚠️ *Aviso*: Meta description longa (> 160 chars)")
            
        canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
        canonical = canonical_tag['href'] if canonical_tag and canonical_tag.has_attr('href') else "AUSENTE"
        report.append(f"- **Canonical**: {canonical}")

        # Headings
        h1s = soup.find_all('h1')
        report.append(f"- **H1s**: {len(h1s)} encontrados")
        if len(h1s) != 1:
            report.append(f"  - ❌ *Erro*: Deve haver exatamente um H1 por página (encontrado: {len(h1s)})")
            
        # Schemas
        schemas_found = []
        ld_json_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
        for tag in ld_json_tags:
            try:
                data = json.loads(tag.string)
                if isinstance(data, dict):
                    if '@type' in data:
                        schemas_found.append(data['@type'])
                    elif '@graph' in data:
                        for item in data['@graph']:
                            if '@type' in item:
                                schemas_found.append(item['@type'])
            except Exception as e:
                schemas_found.append(f"JSON-LD Inválido ({type(e).__name__})")
        report.append(f"- **Schemas**: {', '.join(schemas_found) if schemas_found else 'Nenhum'}")

        # Links verification
        links = soup.find_all('a')
        broken_links = []
        external_links = 0
        internal_links = 0
        for l in links:
            href = l.get('href')
            if not href or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('javascript:'):
                continue
            
            if href.startswith('http://') or href.startswith('https://'):
                external_links += 1
            else:
                internal_links += 1
                # Resolve relative path
                file_dir = os.path.dirname(file_path)
                # Strip query params / hash
                clean_href = href.split('?')[0].split('#')[0]
                if clean_href == "" or clean_href == "/":
                    target_resolved = os.path.join(web_dir, 'index.html')
                elif clean_href.startswith('/'):
                    target_resolved = os.path.join(web_dir, clean_href[1:])
                else:
                    target_resolved = os.path.join(file_dir, clean_href)
                
                # Check directory or file
                if os.path.isdir(target_resolved):
                    target_resolved = os.path.join(target_resolved, 'index.html')
                elif not os.path.exists(target_resolved) and not target_resolved.endswith('.html'):
                    target_resolved += '.html'
                    if not os.path.exists(target_resolved):
                        target_resolved = target_resolved[:-5] + '/index.html'

                if not os.path.exists(target_resolved):
                    broken_links.append(f"{href} (Caminho tentado: {os.path.relpath(target_resolved, web_dir)})")
                    
        report.append(f"- **Links**: {internal_links} internos, {external_links} externos")
        if broken_links:
            report.append("  - ❌ *Links Quebrados*:")
            for bl in broken_links:
                report.append(f"    - {bl}")

        # Image verification
        images = soup.find_all('img')
        heavy_images = []
        missing_alt = []
        for img in images:
            src = img.get('src')
            alt = img.get('alt')
            
            if not src:
                continue
                
            if not alt or alt.strip() == "":
                missing_alt.append(src)
                
            if not src.startswith('http') and not src.startswith('data:'):
                file_dir = os.path.dirname(file_path)
                img_path = os.path.join(file_dir, src)
                if os.path.exists(img_path):
                    size = os.path.getsize(img_path)
                    if size > 150 * 1024: # > 150KB
                        heavy_images.append(f"{src} ({size / 1024:.1f} KB)")
                else:
                    report.append(f"  - ❌ *Imagem quebrada*: {src}")
                    
        if missing_alt:
            report.append(f"  - ⚠️ *Imagens sem alt*: {', '.join(missing_alt[:3])}{'...' if len(missing_alt)>3 else ''}")
        if heavy_images:
            report.append(f"  - ⚠️ *Imagens pesadas (>150KB)*:")
            for hi in heavy_images:
                report.append(f"    - {hi}")
        report.append("") # empty line

    # Save report
    os.makedirs('saidas', exist_ok=True)
    report_content = '\n'.join(report)
    with open('saidas/articles_audit_log.txt', 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print("Relatório salvo em saidas/articles_audit_log.txt")
    print(report_content[:1500] + "\n... [veja saidas/articles_audit_log.txt para relatório completo]")

if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'audit'
    target = sys.argv[2] if len(sys.argv) > 2 else 'web'
    
    if command == 'audit':
        audit_site(target)
    else:
        print(f"Comando '{command}' não suportado pelo script python. Rode com 'audit'.")
