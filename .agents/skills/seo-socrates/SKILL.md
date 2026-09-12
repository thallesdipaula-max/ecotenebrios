---
name: seo-socrates
description: >
  Otimização SEO semântica e GEO/AEO com metodologia Daniel Sócrates.
  Use quando: "otimizar artigo", "melhorar SEO", "meta description",
  "FAQ schema", "otimizar pra IA", "GEO", "AEO", "título SEO",
  "links internos", "gaps de conteúdo", "benchmarking SEO",
  "newsletter SEO", "resumo de artigo", "subtítulos", "/seo-socrates"
---

# /seo-socrates — Metodologia Daniel Sócrates para Ecotenébrios

Skill autônoma de otimização SEO semântica e GEO/AEO. Roda os 9 prompts técnicos da metodologia Daniel Sócrates, adaptados pro nicho de alimentação natural para pets exóticos.

---

## Dependências

Ler **antes de qualquer execução**:

| Arquivo | O que extrair |
|---------|---------------|
| `_memoria/empresa.md` | Produtos, público-alvo, diferenciais, região |
| `_memoria/preferencias.md` | Tom de voz, estilo de escrita, o que evitar |
| `_memoria/estrategia.md` | Foco atual (priorizar prompts relevantes) |
| `marketing/seo/` | Outputs anteriores (evitar repetir trabalho) |

---

## Workflow

### Fase A — Preparação

1. Ler arquivos de memória
2. Perguntar ao usuário: **qual artigo/página/tópico quer otimizar?**
3. Classificar a intenção:
   - **Otimização de artigo existente** → rodar prompts 1, 2, 3, 4, 7, 8
   - **Criação do zero** → rodar prompts 1, 2, 3, 4, 5, 6, 9
   - **Auditoria completa** → rodar todos os 9
4. Checar se já existe output anterior em `marketing/seo/`

### Fase B — Execução

Rodar os prompts selecionados. Em cada um:
- Seguir o processo descrito abaixo
- Aplicar **Checklist de Qualidade** (seção ao final)
- Salvar output no caminho indicado

### Fase C — Consolidação

1. Compilar todos os outputs num único relatório
2. Salvar em `marketing/seo/09-socrates-[topico].md`
3. Listar ações pendentes (implementação no site, posts, etc.)
4. Sugerir próximos passos (ex: "Quer que eu gere o carrossel com esse conteúdo?")

---

## Os 9 Prompts

---

### 1. Meta Descrição Otimizada

**Quando usar:** Antes de publicar qualquer página/artigo, ou quando o usuário pedir "meta description"

**Input:** Palavra-chave alvo + URL ou rascunho do conteúdo

**Processo:**
1. Ler `_memoria/preferencias.md` pra calibrar tom
2. Gerar **3 opções** até 155 caracteres
3. Aplicar fórmula: **termo-semente no início + benefício + CTA leve**
4. Validar: palavra-chave aparece? é persuasiva? tem CTA?

**Output:** 3 opções com justificativa. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Meta Descrições")

**Exemplo (Ecotenébrios):**
> "Procurando tenébrios vivos de qualidade? Garanta nutrição premium com manejo artesanal e envio seguro. Conheça nossos produtos!"

---

### 2. Motor de FAQ (JSON-LD)

**Quando usar:** Quando o usuário pedir "FAQ", "perguntas frequentes", "schema FAQ", ou antes de publicar artigo novo

**Input:** Tema/artigo + palavra-chave principal

**Processo:**
1. Pesquisar com **WebSearch**: `"[palavra-chave] perguntas frequentes"` e autocomplete do Google
2. Selecionar as **6 perguntas mais reais** (o que o público realmente pergunta)
3. Escrever respostas diretas de **40-60 palavras** (foco em GEO/AEO — IAs precisam de respostas concisas)
4. Formatar em 2 versões:
   - **Visível** (pro site): `<details><summary>Pergunta</summary>Resposta</details>`
   - **JSON-LD** (pro schema): bloco `FAQPage` pronto pra colar no `<head>`

**Output:** 6 P&R + JSON-LD. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "FAQ")

**Exemplo de pergunta:**
> **P:** Tenébrio é bom para geckos?
> **R:** Sim, o tenébrio comum (Tenebrio molitor) é uma excelente fonte de proteínas para geckos. Cada larva contém cerca de 20% de proteína e 13% de gordura, sendo ideal para complementar a dieta de répteis insetívoros. Ofereça 2-3 unidades por refeição, 2-3 vezes por semana.

---

### 3. Subtítulos Inteligentes (H2/H3)

**Quando usar:** Quando o usuário pedir "estrutura do artigo", "subtítulos", "headings", ou antes de escrever um artigo novo

**Input:** Tema/artigo + intenção de busca

**Processo:**
1. Mapear a **intenção de busca** (o que a pessoa quer resolver?)
2. Gerar **8 a 10 cabeçalhos** (H2 e H3) cobrindo:
   - Definição / conceito-chave
   - Benefícios / por que importa
   - Como aplicar / guia prático
   - Cuidados / erros comuns
   - Comparativos (se fizer sentido)
   - Perguntas relacionadas (pra FAQ interno)
3. Cada heading deve conter uma **entidade relacionada** de forma natural
4. Validar: a estrutura responde todas as dúvidas reais do público?

**Output:** Estrutura de headings. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Estrutura")

**Exemplo:**
```
H2: O que são tenébrios e por que são ideais para répteis
  H3: Composição nutricional do tenébrio comum
  H3: Diferença entre tenébrio vivo e desidratado
H2: Como oferecer tenébrios para seu pet
  H2: Quantidade ideal por espécie
  H3: Geckos e pogonas
  H3: Aves exóticas
H2: Onde comprar tenébrios de qualidade
H2: Perguntas frequentes sobre tenébrios
```

---

### 4. Otimizador AEO/GEO (Prontidão para IA)

**Quando usar:** Sempre que otimizar conteúdo existente, ou quando o usuário pedir "otimizar pra IA", "GEO", "AEO"

**Input:** Rascunho ou artigo existente

**Processo:**
1. Reescrever parágrafos aplicando:
   - **Alta densidade de fatos** (números, porcentagens, nomes científicos)
   - **Frases curtas** na ordem **sujeito-verbo-objeto**
   - **Definições claras** de conceitos na primeira menção
   - **Dados verificáveis** (fonte quando possível)
2. Adicionar **"information gain"** — informações que nenhum concorrente tem (ex: dados da produção artesanal da Ecotenébrios, experiência real da Raíssa)
3. Testar: "Se o ChatGPT ler isso, consegue citar de volta com precisão?"

**Output:** Texto reescrito. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Otimização AEO/GEO")

**Exemplo (antes vs depois):**
- **Antes:** "Os tenébrios são muito nutritivos para répteis."
- **Depois:** "O tenébrio comum (Tenebrio molitor) contém 20% de proteína e 13% de gordura por 100g, sendo uma das melhores opções de alimentação viva para geckos e pogonas."

---

### 5. Resumo para Newsletter

**Quando usar:** Quando o usuário pedir "newsletter", "resumo de artigo", "email marketing"

**Input:** Artigo completo do blog

**Processo:**
1. Extrair os **3-5 pontos mais valiosos** do artigo
2. Escrever e-mail de **100-150 palavras** com:
   - Assunto curto e atrativo (até 50 caracteres)
   - Abertura com gancho (problema ou curiosidade)
   - Conteúdo em 2-3 parágrafos curtos
   - CTA amigável pro WhatsApp
3. Tom: conforme `_memoria/preferencias.md`

**Output:** E-mail pronto. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Newsletter")

**Exemplo de assunto:**
> "Seu gecko pode estar com deficiência de cálcio (e você nem sabe)"

---

### 6. Gerador de Títulos (H1 / Page Title)

**Quando usar:** Quando o usuário pedir "título", "H1", "page title", ou antes de publicar

**Input:** Palavra-chave alvo + URL ou tema

**Processo:**
1. Gerar **10 opções** de títulos com até **60 caracteres**
2. Posicionar a **palavra-chave no início** sempre que possível
3. Aplicar variações:
   - Positivo/benefício ("Como...")
   - Negativo/medo ("O que evitar...")
   - Curiosidade ("O que ninguém te conta...")
   - Comparativo ("X vs Y...")
   - Lista ("5 motivos...")
4. Evitar clickbait excessivo — prometer o que o artigo entrega
5. Validar: CTR estimado? Palavra-chave visível? É clicável?

**Output:** 10 títulos. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Títulos")

**Exemplo:**
> "Tenébrios Vivos: Guia Completo para Alimentar seu Réptil"

---

### 7. Otimizador de Artigo (Benchmarking)

**Quando usar:** Quando o usuário pedir "benchmarking", "comparar com concorrentes", "revisar artigo"

**Input:** Rascunho do artigo + palavra-chave alvo

**Processo:**
1. Usar **WebSearch** pra encontrar os **3 melhores resultados** no Google pra palavra-chave
2. Usar **WebFetch** pra ler cada um
3. Comparar contra o rascunho:
   - **Lacunas de informação:** o que os concorrentes cobrem e o artigo não?
   - **Entidades ausentes:** termos técnicos, nomes científicos, dados que faltam
   - **Information gain:** o que o artigo tem de único que os concorrentes não têm?
4. Gerar relatório com:
   - Tabela: concrente → pontos fortes → pontos fracos
   - Lista de adições recomendadas
   - Sugestão de diferenciação

**Output:** Relatório de benchmarking. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Benchmarking")

---

### 8. Caça Links Internos

**Quando usar:** Quando o usuário pedir "links internos", "internal linking", ou depois de publicar artigo novo

**Input:** URL do artigo novo + mapa do site (se existir)

**Processo:**
1. Listar todas as páginas/artigos existentes do site
2. Identificar quais são **relevantes** pro artigo novo
3. Sugerir links com **âncoras descritivas** de até 5 palavras
4. Priorizar:
   - Links pra páginas de conversão (produtos, Kit Premium)
   - Links de artigos informacionais entre si (clusters)
   - Links de HomePage pra artigos importantes

**Output:** Lista de links internos sugeridos. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Links Internos")

**Exemplo:**
> - [tenébrio desidratado para répteis](/produtos/tenebrio-desidratado) — no parágrafo sobre alimentação desidratada
> - [guia de nutrição para geckos](/blog/nutricao-geckos) — no parágrafo sobre dieta por espécie

---

### 9. Caça Gaps

**Quando usar:** Quando o usuário pedir "gaps", "o que escrever", "ideias de conteúdo", "temas faltantes"

**Input:** Lista de artigos existentes (se existir)

**Processo:**
1. Mapear todos os tópicos já abordados no blog/site
2. Usar **WebSearch** pra descobrir:
   - Perguntas que o público faz e não são respondidas
   - Termos relacionados com demanda mas sem conteúdo
   - Tópicos de concorrentes que a Ecotenébrios não cobre
3. Classificar gaps por:
   - **Potencial de tráfego** (volume estimado)
   - **Relevância pro negócio** (conecta com produtos?)
   - **Dificuldade de produção** (complexidade do tema)
4. Sugerir **5-10 novos temas** com:
   - Título sugerido
   - Palavra-chave alvo
   - Intenção de busca
   - Formato recomendado (artigo, guia, FAQ, comparativo)

**Output:** Lista de gaps e temas. Salvar em `marketing/seo/09-socrates-[topico].md` (seção "Gaps")

---

## Templates de Schema JSON-LD

### FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Pergunta 1 aqui",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Resposta direta de 40-60 palavras aqui. Inclua dados concretos, nomes científicos e números quando possível."
      }
    },
    {
      "@type": "Question",
      "name": "Pergunta 2 aqui",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Resposta aqui."
      }
    }
  ]
}
```

### Article

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Título do Artigo",
  "description": "Meta description do artigo em até 155 caracteres",
  "author": {
    "@type": "Person",
    "name": "Raíssa"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Ecotenébrios",
    "logo": {
      "@type": "ImageObject",
      "url": "URL_DO_LOGO"
    }
  },
  "datePublished": "2026-01-01",
  "dateModified": "2026-01-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "URL_DO_ARTIGO"
  }
}
```

### LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Ecotenébrios",
  "description": "Alimentação natural para pets exóticos — tenébrios, minhocas californianas e larvas vivas e desidratadas.",
  "image": "URL_DA_FOTO",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Endereço",
    "addressLocality": "Tatuí",
    "addressRegion": "SP",
    "postalCode": "CEP",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "LATITUDE",
    "longitude": "LONGITUDE"
  },
  "telephone": "TELEFONE",
  "url": "SITE_URL",
  "priceRange": "$$",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ]
}
```

---

## Prompt Auxiliar: FAQ → JSON-LD

**Quando usar:** Depois de gerar o FAQ (prompt 2), pra converter direto em schema

**Input:** 6 perguntas e respostas do prompt 2

**Processo:**
1. Pegar cada P&R
2. Inserir no template `FAQPage` acima
3. Validar:
   - Cada `name` é a pergunta exata?
   - Cada `text` tem 40-60 palavras?
   - Não há erros de formatação JSON?
4. Testar com Google Rich Results Test (fornecer link)

**Output:** Bloco JSON-LD pronto pra colar no `<head>` do artigo

---

## Checklist de Qualidade Automático

Rodar **antes de entregar cada output**:

### Conteúdo
- [ ] Usa terminologia correta do nicho (tenébrio, Tenebrio molitor, répteis insetívoros)
- [ ] Dados são reais e verificáveis (WebSearch/WebFetch)
- [ ] Não há informações genéricas de pet shop — tudo específico da Ecotenébrios
- [ ] Tom bate com `_memoria/preferencias.md` (educativo, conversacional, sem ser vendedor)

### SEO
- [ ] Palavra-chave aparece no título e primeiras linhas
- [ ] Metas descriptions têm até 155 caracteres
- [ ] Títulos H1 têm até 60 caracteres
- [ ] Headings são hierárquicos (H2 → H3, sem pular)

### GEO/AEO
- [ ] Respostas diretas nas primeiras linhas de cada seção
- [ ] Frases curtas, ordem sujeito-verbo-objeto
- [ ] Dados concretos (números, porcentagens, nomes científicos)
- [ ] Formato Q&A pra seções de FAQ

### Schema
- [ ] JSON-LD é válido (sem erros de formatação)
- [ ] Todos os campos obrigatórios estão preenchidos
- [ ] URLs são absolutas (com https://)

### Integração
- [ ] Output salvo em `marketing/seo/09-socrates-[topico].md`
- [ ] Links internos sugeridos usam âncoras descritivas
- [ ] Próximos passos estão claros (carrossel? publicar? implementar?)

---

## Integração com Outras Skills

| Skill | Como se conecta |
|-------|-----------------|
| `/publicar-tema` | Consome outputs dos prompts 5 (newsletter), 3 (subtítulos) e 6 (títulos) |
| `/carrossel` | Pode gerar carrossel visual a partir do conteúdo otimizado (prompt 4) |
| `/anuncio-google` | Usa meta descriptions (prompt 1) e títulos (prompt 6) |
| `/planejar-instagram` | Prompts de gaps (prompt 9) alimentam ideias de conteúdo |

---

## Regras

1. Toda pesquisa deve ser **real** (usar WebSearch/WebFetch), nunca inventar dados de volume ou concorrência
2. Copies e textos seguem `_memoria/preferencias.md` estritamente
3. Termos em **português do Brasil**, como o público busca
4. Quando um dado não puder ser obtido (ex: volume exato), deixar claro que é **estimativa** e explicar a lógica
5. Schema JSON-LD deve ser **válido** — testar antes de entregar
6. Conteúdo AEO/GEO: **frases curtas, SVO, dados concretos** — IAs precisam de precisão
7. Sempre salvar outputs em `marketing/seo/` — nunca manter só na conversa
8. Ao finalizar, sempre sugerir **próximos passos** (carrossel, publicar, implementar no site)

---

## Exemplo Completo de Execução

**Cenário:** O usuário pede "otimize um artigo sobre tenébrios vivos pra geckos"

### Fase A — Preparação
1. ✅ Lê `_memoria/empresa.md` → Ecotenébrios, tenébrios vivos, Tatuí-SP, envio Brasil
2. ✅ Lê `_memoria/preferencias.md` → tom educativo, conversacional, emojis naturais
3. ✅ Pergunta: "Qual é o artigo? Tem rascunho ou quer criar do zero?"
4. ✅ Usuário: "Tenho um rascunho, vou colar"
5. ✅ Classifica: **Otimização de artigo existente** → prompts 1, 2, 3, 4, 7, 8

### Fase B — Execução

**Prompt 1 — Meta Descrição:**
> 1. keyword: "tenébrios vivos para gecko"
> 2. Gera 3 opções:
>    - "Tenébrios vivos para gecko: garanta nutrição premium com manejo artesanal. Envio climatizado pra todo Brasil. Conheça!"
>    - "Seu gecko merece tenébrios vivos de qualidade. Produto artesanal, envio seguro. Saiba mais!"
>    - "Alimente seu gecko com tenébrios vivos ricos em proteínas. Ecotenébrios — qualidade que você pode ver."
> 3. ✅ Checklist: keyword presente? sim. até 155 chars? sim. CTA? sim.

**Prompt 2 — FAQ:**
> 1. WebSearch: "tenébrios vivos para gecko perguntas"
> 2. Seleciona 6 perguntas reais:
>    - "Tenébrio é bom para gecko?"
>    - "Quantos tenébrios dar pro gecko por dia?"
>    - "Tenébrio vivo ou desidratado, qual melhor?"
>    - "Como guardar tenébrios vivos?"
>    - "Tenébrio causa impaction em répteis?"
>    - "Onde comprar tenébrios vivos de qualidade?"
> 3. Escreve respostas de 40-60 palavras com dados concretos
> 4. Gera versão visível + JSON-LD

**Prompt 3 — Subtítulos:**
> Gera 9 headings:
> ```
> H2: O que são tenébrios e por que são perfeitos pra geckos
>   H3: Composição nutricional do Tenebrio molitor
> H2: Tenébrio vivo vs desidratado — qual escolher?
> H2: Como oferecer tenébrios para seu gecko
>   H3: Quantidade ideal por tamanho do réptil
>   H3: Frequência de alimentação
> H2: Cuidados na hora de guardar tenébrios vivos
> H2: Benefícios do enriquecimento ambiental com insetos
> H2: Onde comprar tenébrios vivos de qualidade no Brasil
> ```

**Prompt 4 — AEO/GEO:**
> Reescreve o parágrafo de introdução:
> - **Antes:** "Os tenébrios são uma ótima opção pra alimentar seu gecko."
> - **Depois:** "O tenébrio comum (Tenebrio molitor) é uma larva de besouro com 20% de proteína e 13% de gordura por 100g. É a opção mais acessível de alimentação viva para geckos (Phelsuma e Hemidactylus), fornecendo cálcio, fósforo e micronutrientes essenciais pra saúde óssea e digestão."

**Prompt 7 — Benchmarking:**
> 1. WebSearch: "tenébrios vivos para gecko" → top 3
> 2. WebFetch em cada URL
> 3. Compara: lacunas encontradas → nenhum fala sobre envio climatizado, nenhum tem dados da Raíssa sobre manejo artesanal
> 4. Sugere adicionar: seção "Por que o manejo artesanal importa" com experiência real

**Prompt 8 — Links Internos:**
> Sugere:
> - [tenébrio desidratado para répteis](/produtos/tenebrio-desidratado) → no parágrafo sobre alternativas
> - [guia completo de alimentação para pogonas](/blog/alimentacao-pogonas) → no parágrafo sobre espécies relacionadas
> - [kit tenébrios vivos](/produtos/kit-tenebrios-vivos) → na seção "Onde comprar"

### Fase C — Consolidação

1. Compila tudo em `marketing/seo/09-socrates-tenebrios-geckos.md`
2. Lista ações pendentes:
   - [ ] Inserir JSON-LD FAQ no artigo
   - [ ] Substituir meta description
   - [ ] Adicionar seção "manejo artesanal" (benchmarking)
   - [ ] Implementar links internos sugeridos
3. Sugere próximos passos:
   - "Quer que eu gere um carrossel resumo desse artigo?"
   - "Posso montar a versão newsletter pra email marketing"
   - "Quer que eu salve essas otimizações no artigo?"
