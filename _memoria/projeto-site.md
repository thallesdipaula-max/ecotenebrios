# Projeto: Site Ecotenébrios

> Memória do projeto do site. Atualize sempre que mudar estrutura, páginas ou SEO.

## O que é

Landing page + blog de conteúdo hospedados no domínio **ecotenebrios.com.br**. Site estático, sem framework — HTML/CSS/JS puros, deploy automático por Git (Netlify/Vercel).

## Estrutura

- `web/` — raiz do site
  - `index.html` — landings de vendas (Kit Premium, Desidratados, Minhocas) + blog grid
  - `blog/<slug>/index.html` — 16 artigos educativos
  - `sucesso/` — página pós-pagamento
  - `sitemap.xml`, `robots.txt`, `_headers`, `CNAME`, `google*.html` (verificação)
- CSS: `web/css/style.css`
- Imagens: `web/assets/images/*.webp`

## Ferramentas conectadas

- Dominio ecotenebrios.com.br (CNAME → Git)
- Google Search Console conectado (verification tag no index.html)
- Meta Pixel (`1006621321781390`) em todas as páginas
- Google Analytics — ainda não conectado

## Estado atual do SEO (audit base)

**Já implementado (bom estado):**
- Schema JSON-LD no index: LocalBusiness, FAQPage, ItemList de produtos (3 produtos com Price/Offer)
- Schema em TODOS os artigos: BlogPosting (com `about`/`mentions`), BreadcrumbList, FAQPage
- Canonical, Open Graph, Twitter Cards, robots.txt, sitemap.xml em todas as páginas
- Hierarquia H1/H2/H3 respeitada nos artigos; internal linking entre artigos

**Gaps identificados (tecnico/semantico):**
- `og:image` do index usa `logo.webp` (deveria ser imagem de compartilhamento 1200x630) — ainda pendente
- ~~BlogPosting sem `dateModified`, `mainEntityOfPage`, `speakable`, `@id` na URL~~ ✅ concluído 2026-09-12
- ~~Index não tem schema `WebSite` + `Organization`~~ ✅ concluído 2026-09-12
- `meta name="keywords"` presente (Google ignora, mas pode manter)
- ~~H1 do index não tinha keyword~~ ✅ H1 agora: "Alimentação Natural para Pets Exóticos — Tenébrios Vivos, Minhocas e Larvas"

## Alterações de SEO semântico — concluído 2026-09-12

- **Schema BlogPosting (16 artigos):** adicionado `@id`, `mainEntityOfPage`, `dateModified` e `speakable` (cssSelector `.article-title`/`.article-body`) — validado JSON em todos
- **Home:** novo schema `@graph` com `Organization` + `WebSite`; `LocalBusiness` enriquecido (`founder`, `logo`, `areaServed`, `knowsAbout`); `og:locale pt_BR`
- **Internal linking:** 16 artigos com link âncora "Kit Premium" → `../../index.html#kit-premium` (seção da home agora tem `id="kit-premium"`); satélites `calopsita` e `como-criar` ganharam link ao pilar → 16/16 artigos linkam `alimentacao-natural-pets-exoticos`
- **Sitemap:** `lastmod` de todas as URLs atualizado para 2026-09-12

## Proximos passos candidatos

1. Corrigir OG image do index (imagem 1200x630 dedicada) — único gap técnico restante
2. Publicar conteúdo novo (skill `/publicar-tema`) e registrar no sitemap ao publicar
3. Robuster linkagem: produto oferecido? verificar `Kit Matrizes` (como-criar) se tiver home section própria

## Artigos do blog (16)

- alimentacao-natural-passaros-exoticos
- alimentacao-natural-pets-exoticos (pilar)
- alimentacao-natural-repteis
- alimentacao-natural-roedores-exoticos
- alimentos-proibidos-pets-exoticos
- calopsita-pode-comer-melao-kiwi-mexerica
- como-conservar-tenebrio-vivo
- como-criar-tenebrio-em-casa
- enriquecimento-ambiental-repteis-mamiferos
- frutas-e-vegetais-seguros-pets-exoticos
- gecko-pogona-sem-comer
- larvas-de-tenebrio-diferencas-nutricionais
- onde-comprar-tenebrio-vivo
- proteina-animal-para-aves-reproducao
- suplementacao-pets-exoticos
- tenebrio-para-pets-exoticos

## Estrategia semantica

- Metodologia Daniel Sócrates: skill `seo-socrates` (9 prompts: meta descrição, FAQ JSON-LD, subtítulos com entidades, AEO/GEO, títulos, benchmarking, links internos, gaps)
- Fluxo completo de 8 passos: skill `seo` (pesquisa de demanda, concorrência, GMB, on-page, conteúdo, ads, monitoramento, GEO)
- Outputs de pesquisa: `marketing/seo/`