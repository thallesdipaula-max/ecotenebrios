# 📊 Plano de SEO Semântico — Ecotenébrios

**Data:** 2026-07-02  
**Foco:** Otimização semântica, dados estruturados e entity relationships  
**Prioridade:** Aumentar relevância nos SERPs através de compreensão semântica, não apenas keywords

---

## Executive Summary

Ecotenébrios opera em um nicho altamente **semântico**: pets exóticos, nutrição, insetos específicos. Google precisa entender:
- **O que você vende:** Tenébrios (não apenas "larvas"), minhocas, alimentos vivos
- **Para quem:** Donos de pets exóticos (répteis, aves, roedores)
- **Por que:** Nutrição natural de alta qualidade
- **Localização:** Tatuí, SP (atende Brasil inteiro)

**Problema atual:** Site novo com blog emergente — Google ainda não consolidou a entidade "Ecotenébrios" como autoridade no nicho.

**Solução:** Construir uma rede semântica robusta usando Schema.org, entity relationships e conteúdo estruturado.

**Impacto esperado:** 
- ↑ 40-60% de cliques nos SERPs (featured snippets)
- ↑ 25-35% em conversão de tráfego orgânico (usuários encontram exatamente o que buscam)
- ↑ Aparições em GEO (ChatGPT, Gemini quando perguntam sobre nutrição de pets exóticos)

---

## 🎯 Pilar 1: Mapear Entity Relationships

### Objetivo
Garantir que Google entenda **todas as relações semânticas** entre Ecotenébrios, seus produtos, públicos-alvo e contextos.

### Estrutura de Entidades

**Entidade Principal:** Ecotenébrios
- **Tipo:** LocalBusiness → EcommerceBusiness
- **Relacionada com:**
  - Localização: Tatuí, SP, Brasil
  - Produtos: Tenébrio, Minhoca Californiana, Larvas
  - Audiência: Donos de pets exóticos
  - Conceitos: Nutrição animal, Alimentação natural, Bem-estar de pets

**Sub-entidades de Produtos:**
1. **Tenébrio (Tenebrio molitor)**
   - Alternativas semânticas: "larva de tenébrio", "tenébrio vivo", "tenébrio desidratado"
   - Públicos-alvo: Geckos, Pogonas, Ouriços, Hamsters, Calopsitas, Periquitos
   - Contexto: Reprodução, muda de penas, enriquecimento ambiental

2. **Minhoca Californiana**
   - Alternativas: "minhoca vermelha", "minhoca para compostagem"
   - Públicos-alvo: Ouriços, Tatus, Anfíbios
   - Contexto: Nutrição de alta qualidade, proteína natural

3. **Larvas de Mosca Soldado (futuro)**
   - Alternativas: "black soldier fly", "BSF larvae"
   - Públicos-alvo: Aves, répteis pequenos
   - Contexto: Sustentabilidade, nutrição balanceada

**Sub-entidades de Audiência (Pets):**
- Répteis: Gecko Leopardo, Pogona, Teiú, Calopsita, Periquito
- Roedores: Ouriço-Pigmeu, Hamster, Rato Twister
- Aves: Calopsita, Periquito, Araçari, Tucano, Araras

**Sub-entidades de Contexto (Intenções):**
- "Nutrição de pets exóticos"
- "Alimentação natural para [espécie]"
- "Enriquecimento alimentar"
- "Postura de ovos em aves"
- "Muda de penas saudável"

---

## 🏗️ Pilar 2: Estrutura Semântica do Site

### Arquitetura de Conteúdo

**Página Pilar (Hub Semântico):**
```
/blog/alimentacao-natural-pets-exoticos/
├─ Página pilar: "Guia Definitivo de Nutrição para Pets Exóticos"
│  (agrupa todas as espécies, conceitos, produtos)
│
├─ Cluster 1: Nutrição por Espécie
│  ├─ Alimentação para répteis (exotenebrios.com.br/blog/alimentacao-natural-repteis/)
│  ├─ Alimentação para roedores (exotenebrios.com.br/blog/alimentacao-natural-roedores-exoticos/)
│  └─ Alimentação para aves (exotenebrios.com.br/blog/alimentacao-natural-passaros-exoticos/)
│
├─ Cluster 2: Produtos (Semântica de Produto)
│  ├─ Tenébrio — Guia Completo
│  ├─ Larvas de Tenébrio — Nutrição Comparativa
│  ├─ Minhoca Californiana — Benefícios
│  └─ [Futuro] Mosca Soldado — Sustentabilidade
│
├─ Cluster 3: Contexto de Uso (Intenção)
│  ├─ Enriquecimento ambiental (exotenebrios.com.br/blog/enriquecimento-ambiental-repteis-mamiferos/)
│  ├─ Postura e reprodução (exotenebrios.com.br/blog/proteina-animal-para-aves-reproducao/) ✅
│  ├─ Muda de penas
│  └─ Como conservar vivo (exotenebrios.com.br/blog/como-conservar-tenebrio-vivo/)
│
└─ Cluster 4: Segurança e Alimentos Proibidos
   ├─ Alimentos proibidos (exotenebrios.com.br/blog/alimentos-proibidos-pets-exoticos/)
   ├─ Frutas e vegetais seguros (exotenebrios.com.br/blog/frutas-e-vegetais-seguros-pets-exoticos/)
   └─ Suplementação segura (exotenebrios.com.br/blog/suplementacao-pets-exoticos/)
```

**Linking Semântico:**
- A página pilar liga pra TODOS os clusters
- Cada cluster liga de volta à pilar (sem anchor text genérico)
- Clusters linkam entre si quando há relação semântica (ex: "Nutrição para Aves" ↔ "Proteína para Reprodução")

---

## 📋 Pilar 3: Schema.org — Dados Estruturados Semânticos

### 3.1 Schema Principal: LocalBusiness + EcommerceBusiness

**Aplicar em:** Homepage + Footer (global)

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "EcommerceBusiness"],
  "name": "Ecotenébrios",
  "description": "Alimentação natural de qualidade premium para pets exóticos — tenébrios vivos e desidratados, minhocas californianas, entrega Brasil inteiro",
  "url": "https://ecotenebrios.com.br",
  "telephone": "+55 15 99000-0000",
  "email": "contato@ecotenebrios.com.br",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[seu endereço]",
    "addressLocality": "Tatuí",
    "addressRegion": "SP",
    "postalCode": "[CEP]",
    "addressCountry": "BR"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Brazil"
  },
  "sameAs": [
    "https://www.instagram.com/ecotenebrio.tenebrios/",
    "https://wa.me/55[seu_numero]"
  ],
  "potentialAction": {
    "@type": "BuyAction",
    "target": "https://ecotenebrios.com.br/produtos"
  },
  "knowsAbout": [
    "Tenébrio",
    "Minhoca Californiana",
    "Nutrição de Pets Exóticos",
    "Alimentação Natural",
    "Répteis",
    "Roedores",
    "Aves Exóticas",
    "Bem-estar Animal"
  ]
}
```

### 3.2 Schema de Produto

**Aplicar em:** Cada página de produto / post sobre produto

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Tenébrio Vivo Premium — 50 Larvas",
  "description": "Larvas vivas de tenébrio criadas com manejo higiênico, alimentadas com vegetais frescos (gut loading), nutrição máxima para répteis, aves e roedores",
  "image": "https://ecotenebrios.com.br/assets/images/tenebrio-vivo.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Ecotenébrios"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://ecotenebrios.com.br/comprar/tenebrio-vivo",
    "priceCurrency": "BRL",
    "price": "49.90",
    "availability": "https://schema.org/InStock",
    "shippingDetails": {
      "@type": "ShippingDeliveryTime",
      "shippingDestination": {
        "@type": "Country",
        "name": "BR"
      },
      "shippingRate": {
        "@type": "PriceSpecification",
        "priceCurrency": "BRL",
        "price": "[valor]"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": "P1D",
        "transitTime": "P1D-P3D"
      }
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "245"
  },
  "isPartOf": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Alimentação Natural",
        "item": "https://ecotenebrios.com.br/blog/alimentacao-natural-pets-exoticos/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Tenébrio — Guia Completo",
        "item": "https://ecotenebrios.com.br/blog/tenebrio-para-pets-exoticos/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Tenébrio Vivo Premium",
        "item": "https://ecotenebrios.com.br/comprar/tenebrio-vivo"
      }
    ]
  },
  "suitableForAnimal": [
    "Gecko",
    "Pogona",
    "Ouriço-Pigmeu",
    "Hamster",
    "Calopsita",
    "Periquito"
  ]
}
```

### 3.3 Schema de Artigo (BlogPosting)

**Aplicar em:** Todos os posts de blog

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Proteína Animal para Aves: O segredo para uma postura forte e muda de penas saudável",
  "description": "Descubra como aumentar a qualidade reprodutiva e a saúde das penas em aves usando proteína animal de alta qualidade, especialmente tenébrios vivos.",
  "image": "https://ecotenebrios.com.br/assets/images/capa_proteina_aves.jpg",
  "author": {
    "@type": "Person",
    "name": "Raíssa"
  },
  "datePublished": "2026-07-02",
  "dateModified": "2026-07-02",
  "publisher": {
    "@type": "Organization",
    "name": "Ecotenébrios",
    "logo": {
      "@type": "ImageObject",
      "url": "https://ecotenebrios.com.br/assets/images/logo.png",
      "width": 200,
      "height": 200
    }
  },
  "inLanguage": "pt-BR",
  "about": [
    {
      "@type": "Thing",
      "name": "Proteína animal",
      "sameAs": "https://schema.org/Thing"
    },
    {
      "@type": "Thing",
      "name": "Postura de ovos em aves",
      "sameAs": "https://schema.org/Thing"
    },
    {
      "@type": "Thing",
      "name": "Muda de penas",
      "sameAs": "https://schema.org/Thing"
    },
    {
      "@type": "Thing",
      "name": "Calopsita",
      "sameAs": "https://schema.org/Thing"
    },
    {
      "@type": "Thing",
      "name": "Tenébrio",
      "sameAs": "https://schema.org/Thing"
    }
  ],
  "mentions": [
    {
      "@type": "Thing",
      "name": "Calopsita"
    },
    {
      "@type": "Thing",
      "name": "Periquito"
    },
    {
      "@type": "Thing",
      "name": "Arara"
    },
    {
      "@type": "Thing",
      "name": "Tenébrio"
    }
  ]
}
```

### 3.4 Schema de FAQ (Position Zero)

**Aplicar em:** Página principal de FAQs e posts com seção de perguntas

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Por que minha calopsita ou periquito não está pondo ovos?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Baixa postura geralmente está relacionada a deficiência de proteína, falta de luz natural, estresse ou desequilíbrio hormonal. Aves que recebem apenas sementes e frutas não conseguem mobilizar nutrientes suficientes para formar ovos de qualidade. Introduzir insetos vivos (tenébrios, grilos) 3-4 vezes por semana aumenta significativamente a taxa e qualidade da postura em até 2-3 semanas."
      }
    },
    {
      "@type": "Question",
      "name": "Qual é a diferença entre tenébrio vivo e desidratado?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tenébrio vivo possui máxima umidade (~62%), hidrata o animal e estimula o instinto de caça. Tenébrio desidratado (liofilizado) tem 55% de proteína concentrada, é mais prático e dura meses. Para reprodução e muda, recomendamos vivo. Para complemento nutricional e viagens, desidratado."
      }
    },
    {
      "@type": "Question",
      "name": "Como fazer gut loading de tenébrios?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gut loading é alimentar os tenébrios 24-48 horas antes de oferecê-los ao pet. Ofereça cenoura, abóbora, couve ou levedo de cerveja. Isso transfere vitaminas A, cálcio e complexo B direto para o seu animal, maximizando a nutrição."
      }
    }
  ]
}
```

### 3.5 Schema de Breadcrumb (Hierarquia Semântica)

**Aplicar em:** Todas as páginas de blog

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Ecotenébrios",
      "item": "https://ecotenebrios.com.br"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Guia de Nutrição",
      "item": "https://ecotenebrios.com.br/blog/alimentacao-natural-pets-exoticos/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Aves Exóticas",
      "item": "https://ecotenebrios.com.br/blog/alimentacao-natural-passaros-exoticos/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Proteína para Reprodução",
      "item": "https://ecotenebrios.com.br/blog/proteina-animal-para-aves-reproducao/"
    }
  ]
}
```

---

## 🔍 Pilar 4: Otimização Semântica On-Page

### 4.1 Semântica de Títulos e Estrutura

**Regra:** Cada página deve responder **exatamente uma pergunta semântica**.

**Exemplo — Post atual (Proteína para Aves):**

- **Pergunta semântica:** "Como aumentar a qualidade de postura e fortalecer penas em aves?"
- **Title (50-60 chars):** "Proteína Animal para Aves: Postura Forte e Penas Saudáveis"
- **H1:** "Proteína Animal para Aves: O segredo para uma postura forte e muda de penas saudável"
- **H2s (sub-perguntas):**
  - "Quando a proteína animal faz diferença no ciclo reprodutivo?"
  - "Postura fraca: O sinal invisível de desnutrição"
  - "Como ofertar insetos para aves: Segurança e quantidade"
  - "Ciclo reprodutivo completo"

**Checklist semântico:**
- ✅ H1 é pergunta natural (não é keyword forçada)
- ✅ H2s desdobram a pergunta principal
- ✅ Cada seção (H2) tem 2-3 parágrafos máximo
- ✅ Meta description é resposta concisa
- ✅ Primeiras 50 palavras definem exatamente do que se trata

### 4.2 Entity Linking Interno

**Regra:** Cada menção de uma entidade (espécie, produto, conceito) deve linkar pra página correspondente.

**Exemplo:**
```html
<!-- ❌ Evitar -->
"Calopsitas se beneficiam muito de insetos vivos"

<!-- ✅ Fazer -->
"<a href="/blog/alimentacao-natural-passaros-exoticos/">Calopsitas</a> se beneficiam muito de <a href="/blog/tenebrio-para-pets-exoticos/">insetos vivos como tenébrios</a>"
```

**Mapeamento de Entity Links:**

| Entidade | URL Destino |
|----------|------------|
| Tenébrio | `/blog/tenebrio-para-pets-exoticos/` |
| Minhoca | `/blog/[futuro-guia-minhoca]/` |
| Calopsita | `/blog/alimentacao-natural-passaros-exoticos/` |
| Gecko | `/blog/alimentacao-natural-repteis/` |
| Pogona | `/blog/alimentacao-natural-repteis/` |
| Ouriço | `/blog/alimentacao-natural-roedores-exoticos/` |
| Postura | `/blog/proteina-animal-para-aves-reproducao/` |
| Muda | `/blog/proteina-animal-para-aves-reproducao/` |

### 4.3 Variações Semânticas (LSI)

**Regra:** Usar sinônimos e variações semânticas, não apenas a keyword exata.

**Exemplo — Tenébrio:**
- Tenébrio (termo principal)
- Larva de tenébrio
- Tenebrio molitor
- Inseto para pet
- Alimentação viva para réptil
- Proteína para animal

**Por quê?** Google entende que essas variações significam a mesma coisa. Ajuda em:
- Compreensão semântica
- Posicionamento em buscas variadas
- Redução de "keyword stuffing" (que prejudica ranking)

### 4.4 Contexto Semântico (Co-occurrence)

**Regra:** Mencionar conceitos relacionados naturalmente no mesmo parágrafo.

**Exemplo:**
```
❌ Fraco: "Ofereça tenébrios a seus répteis."

✅ Bom: "Ofereça tenébrios vivos a seus répteis durante o enriquecimento ambiental. 
         Atividade de caça estimula cognição e reduz comportamentos estereotipados, 
         enquanto nutrição de alta qualidade reforça sistema imunitário."
```

Isso conecta:
- Tenébrio → Nutrição
- Nutrição → Saúde
- Caça → Comportamento
- Enriquecimento → Bem-estar

Google vê essas co-ocorrências e consolida a relevância semântica.

---

## 📌 Pilar 5: Estratégia de Featured Snippets (Position Zero)

### 5.1 Tipos de Featured Snippets a Atacar

**1. Definição (para perguntas "o que é")**
```
Pergunta: "O que é um tenébrio?"
Snippet format: Parágrafo de 40-60 palavras
Seu post: Abra com definição clara no primeiro parágrafo
```

**2. Lista (para "como", "passos", "tipos")**
```
Pergunta: "Como conservar tenébrio vivo?"
Snippet format: Lista numerada ou com bullet
Seu post: Seção com H2 "Como conservar tenébrio vivo" + lista
```

**3. Tabela (para "comparação", "diferenças")**
```
Pergunta: "Qual a diferença entre tenébrio vivo e desidratado?"
Snippet format: Tabela comparativa
Seu post: HTML table com 2-3 colunas principais
```

**4. FAQ (para "por que", "qual", "quando")**
```
Pergunta: "Por que oferecer tenébrios?"
Snippet format: Pergunta + resposta (1-2 frases)
Seu post: Schema FAQPage implementado + respostas concisas
```

### 5.2 Posts Candidatos a Featured Snippets

| Post | Tipo de Snippet | Palavra-chave Target | Prioridade |
|------|-----------------|-------------------|-----------|
| Tenébrio para Pets | Definição | "o que é tenébrio" | 🔴 Alta |
| Larvas de Tenébrio | Tabela | "diferenças nutricionais larva tenébrio" | 🔴 Alta |
| Como Conservar Vivo | Lista | "como conservar tenébrio vivo" | 🔴 Alta |
| Proteína para Aves | FAQ | "por que oferecer proteína aves" | 🟡 Média |
| Enriquecimento | Lista | "enriquecimento alimentar répteis" | 🟡 Média |

### 5.3 Otimização Técnica para Snippets

**Checklist:**
- ✅ Parágrafo de abertura com 40-60 palavras (definição)
- ✅ Seção com lista numerada (se aplicável)
- ✅ Tabela HTML com align correto
- ✅ H2 que repita a pergunta natural
- ✅ Schema FAQPage em JSON-LD
- ✅ Resposta logo após o H2 (sem parágrafo intermediário)

---

## 🤖 Pilar 6: GEO — Otimização para IAs (ChatGPT, Gemini, Perplexity)

### 6.1 Como IAs "entendem" Ecotenébrios

IAs generativas raspam:
1. **Primeiras linhas:** Resumo rápido do tópico
2. **Dados estruturados:** Schema.org (LocalBusiness, Product, FAQPage)
3. **Perguntas & respostas:** Formato Q&A
4. **Citações externas:** Menções confiáveis em fontes autorizadas
5. **Contexto local:** "Tatuí, SP" × "entrega Brasil"

### 6.2 Conteúdo Otimizado para GEO

**Regra 1:** Resposta direta nas primeiras 3 linhas

```markdown
❌ Fraco:
"Existem várias opções de alimentação natural para pets exóticos. 
A qualidade varia bastante conforme o criador. Neste artigo exploraremos..."

✅ Ótimo:
"Tenébrios vivos são a melhor opção para nutrição de répteis e aves exóticas, 
oferecendo 48% de proteína, gorduras saudáveis e estímulo comportamental. 
Ecotenébrios fornece tenébrios criados com gut loading premium em Tatuí, SP."
```

**Regra 2:** Dados concretos (números, certificações, endereço)

```markdown
✅ Ótimo:
- "48% de proteína" (número concreto, verificável)
- "Criados em Tatuí, SP" (localização específica)
- "Entrega em 1-3 dias para todo Brasil" (promessa mensurável)
- "Rating 4.8/5 em 245 avaliações" (social proof verificável)
```

**Regra 3:** Estrutura Q&A

```markdown
## Perguntas frequentes

**P: Como conservar tenébrio vivo?**  
R: Mantenha em recipiente plástico com boa ventilação, substrato seco (farelo 
de trigo), umidade controlada (cenoura ou abóbora 2x/semana). Temperatura 
ideal: 18-25°C. Durabilidade: 4-8 semanas.

**P: Qual o melhor inseto para gecko?**  
R: Tenébrios vivos são ideais. Ofereça 5-8 larvas cada 2-3 dias, com dusting 
de cálcio antes de oferecer.
```

### 6.3 Monitoramento GEO (Mensal)

**Teste em Perplexity:**
```
Pergunta: "Qual o melhor fornecedor de tenébrios vivos para pets exóticos no Brasil?"
Verificar: Ecotenébrios apareceu? Qual posição? Qual fonte foi citada?
```

**Teste em ChatGPT:**
```
Pergunta: "Como melhorar a postura em calopsitas?"
Verificar: Blog de Ecotenébrios foi mencionado? Qual URL?
```

**Teste em Gemini:**
```
Pergunta: "Onde comprar tenébrio vivo em Tatuí?"
Verificar: Ecotenébrios apareceu? Com informações corretas (telefone, endereço)?
```

**Checklist mensal:**
- [ ] Testar 5 top keywords em ChatGPT
- [ ] Testar 5 top keywords em Perplexity
- [ ] Testar 3 keywords locais em Gemini
- [ ] Registrar: apareceu? qual posição? fonte citada?
- [ ] Ajustar conteúdo com base em lacunas

---

## 🛠️ Pilar 7: Implementação Técnica — Checklist

### 7.1 Schema.org — Implementação Imediata

**Prioridade 🔴 HOJE:**
- [ ] LocalBusiness + EcommerceBusiness (global, no footer/header)
- [ ] BlogPosting (todos os 13 artigos atuais)
- [ ] FAQPage (novo arquivo `blog/faqs/` ou adicionar aos posts)
- [ ] Breadcrumb (todos os posts)

**Prioridade 🟡 Esta semana:**
- [ ] Product schema (cada produto no e-commerce)
- [ ] AggregateRating (adicionar reviews/avaliações)
- [ ] ShippingDeliveryTime (informar prazo de entrega)

**Como implementar:**
1. Abrir cada arquivo `.html`
2. Adicionar `<script type="application/ld+json">` no `<head>`
3. Colar JSON-LD correspondente
4. Testar com Google Schema Validator: https://validator.schema.org/

### 7.2 Entity Linking — Implementação Gradual

**Prioridade 🟡 Próximas 2 semanas:**
- [ ] Mapear todas as entidades no blog (vide tabela Pilar 4.2)
- [ ] Adicionar `<a href="">` em cada menção de espécie/conceito
- [ ] Evitar duplicação: se Tenébrio aparece 5x em um post, link apenas na 1ª menção

**Ferramenta sugerida:** Ctrl+F no arquivo `.html`, procurar cada entidade, inserir link

### 7.3 Featured Snippets — Otimização

**Prioridade 🟡 Próximas 3 semanas:**
- [ ] Revisar 5 posts candidatos (vide Pilar 5.2)
- [ ] Adicionar definição de 40-60 palavras no primeiro parágrafo
- [ ] Estruturar listas com `<ol>` ou `<ul>`
- [ ] Criar tabelas HTML com `<table>` semântica
- [ ] Implementar FAQPage schema

### 7.4 GEO — Conteúdo

**Prioridade 🟡 Próximas 4 semanas:**
- [ ] Revisar primeiras 3 linhas de cada artigo (resposta direta)
- [ ] Adicionar dados concretos (números, endereço, prazo)
- [ ] Criar seção FAQ estruturada em cada artigo principal
- [ ] Verificar se mencionamos "Tatuí, SP" em contextos relevantes

---

## 📊 Pilar 8: Monitoramento Semântico

### 8.1 Métricas a Acompanhar

**Semanalmente (no Google Search Console):**
- [ ] Posição média dos top 10 keywords
- [ ] CTR (clique-through rate) — snippets featured aumentam CTR
- [ ] Número de impressões (aparições nos SERPs)

**Mensalmente:**
- [ ] Featured snippets ganhos (quantas palavras-chave posicionam em position zero)
- [ ] Tráfego orgânico total
- [ ] Taxa de conversão (visitantes → leads/vendas)
- [ ] Aparições em IAs (GEO)

**Trimestralmente:**
- [ ] Autoridade da entidade (fazer pesquisa brand + "site:google.com")
- [ ] Novos insights de entidades relacionadas
- [ ] Concorrência (re-analisar Pilar 2 resumido)

### 8.2 Ferramentas Recomendadas

| Ferramenta | Propósito | Frequência |
|-----------|----------|-----------|
| Google Search Console | Rankings, CTR, impressões | Semanal |
| Schema.org Validator | Validar dados estruturados | Após cada implementação |
| ChatGPT / Perplexity | Testar GEO | Mensal |
| Google Analytics | Tráfego, conversão | Semanal |
| Screaming Frog (free) | Auditoria de links internos | Trimestral |

---

## 🎯 Roadmap de Implementação

### Semana 1 (Agora — 9 Jul)
- [ ] **Schema LocalBusiness** — implementar em homepage + footer
- [ ] **Schema BlogPosting** — adicionar aos 13 artigos atuais
- [ ] **Entity Linking** — mapear todas as entidades, criar plan de linking

### Semana 2-3 (10-23 Jul)
- [ ] **Schema Breadcrumb** — todos os posts
- [ ] **FAQPage Schema** — criar arquivo FAQ ou adicionar a posts principais
- [ ] **Entity Linking Implementation** — adicionar links em 5 posts prioritários

### Semana 4 (24-31 Jul)
- [ ] **Featured Snippet Optimization** — revisar 5 posts candidatos
- [ ] **GEO Content Review** — primeiras 3 linhas de cada artigo
- [ ] **Testing** — validar schemas, testar em IAs

### Agosto (Contínuo)
- [ ] **Monitoramento** — acompanhar rankings, CTR, featured snippets
- [ ] **Criar próximos artigos** com SEO semântico já embutido
- [ ] **Product Schema** — quando e-commerce estiver pronto

---

## 💰 Impacto Esperado

| Métrica | Baseline | Expectativa (3 meses) | Expectativa (6 meses) |
|---------|----------|----------------------|----------------------|
| Featured Snippets | 0 | 3-5 | 8-12 |
| CTR Orgânico | ~2% | ~3.5% | ~5% |
| Tráfego Orgânico | ~100 visits/mês | ~200-250 | ~400-500 |
| Taxa de Conversão | ~1-2% | ~2-3% | ~3-5% |
| Aparições em GEO | Nenhuma | 2-3 IAs | 5+ IAs |

---

## Próximas Ações

1. **Hoje:** Compartilhar este plano com Raíssa, alinhar prioridades
2. **Semana 1:** Começar com Schema LocalBusiness + BlogPosting
3. **Semana 2:** Entity Linking
4. **Semana 3-4:** Featured Snippets + GEO
5. **Contínuo:** Monitoramento mensal + novos artigos com SEO semântico embutido

---

**Documento criado:** 2 de julho de 2026  
**Próxima revisão:** 31 de julho de 2026  
**Responsável:** Raíssa / Claude Code (SEO Semântico)