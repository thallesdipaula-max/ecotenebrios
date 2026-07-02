# 📋 Auditoria SEO Semântico — Status Atual vs Oportunidades

**Data:** 2 de julho de 2026  
**Baseline:** 13 artigos publicados + 1 homepage  
**Objetivo:** Implementar plano de SEO Semântico de 8 pilares

---

## 🟢 O QUE JÁ TEMOS (Pronto!)

### ✅ 1. Schema BlogPosting
**Status:** 13/13 artigos ✅ 100%

Todos os artigos têm `BlogPosting` com:
- Headline, description, image
- Author (Raíssa), datePublished
- Publisher (Ecotenébrios)
- URL e canonical tag

**Exemplo:**
```json
{
  "@type": "BlogPosting",
  "headline": "Proteína Animal para Aves: O segredo...",
  "author": {"@type": "Person", "name": "Raíssa"},
  "datePublished": "2026-07-02"
}
```

### ✅ 2. LocalBusiness Schema (Homepage)
**Status:** 1/1 homepage ✅

Homepage tem schema LocalBusiness com:
- Nome, telefone, email
- Endereço (Tatuí, SP)
- areaServed (Brasil inteiro)
- sameAs (Instagram, WhatsApp)

### ✅ 3. FAQPage Schema
**Status:** 4/13 artigos ✅ 31%

Artigos com FAQPage já implementado:
1. ✅ `proteina-animal-para-aves-reproducao` — 3 perguntas
2. ✅ `enriquecimento-ambiental-repteis-mamiferos` — 2 perguntas
3. ✅ `alimentacao-natural-passaros-exoticos` — 1 pergunta
4. ✅ `gecko-pogona-sem-comer` — 2 perguntas

**O que falta:** 9 artigos ainda precisam de FAQPage

### ✅ 4. Cross-Linking (Básico)
**Status:** 13/13 artigos têm "Leia também" ✅

Todos os artigos linkam uns aos outros na seção final:
- Média: 11-12 links por artigo (na seção "Leia também")
- Cobertura: todos linkam pra Tenébrio, Larvas, Alimentação por espécie

**Problema:** Links estão apenas no final, não distribuídos semanticamente no corpo do artigo

### ✅ 5. Meta Tags Básicas
**Status:** 13/13 artigos ✅

- Meta description
- Meta keywords (relevantes ao nicho)
- Open Graph (og:title, og:description, og:image)
- Canonical tag
- Theme color

---

## 🟡 O QUE ESTÁ PARCIAL (Meia-boca)

### ⚠️ 1. Breadcrumb Schema
**Status:** 1/13 artigos ✅ (apenas o novo)

Apenas `proteina-animal-para-aves-reproducao` tem BreadcrumbList:
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"position": 1, "name": "Ecotenébrios", "item": "https://ecotenebrios.com.br"},
    {"position": 2, "name": "Guia de Nutrição", "item": "..."},
    {"position": 3, "name": "Aves Exóticas", "item": "..."},
    {"position": 4, "name": "Proteína para Reprodução", "item": "..."}
  ]
}
```

**O que falta:** 12 artigos precisam de Breadcrumb Schema

### ⚠️ 2. Entity Mentions (about/mentions)
**Status:** 1/13 artigos ✅ (apenas o novo)

Apenas `proteina-animal-para-aves-reproducao` tem `about` e `mentions`:
```json
"about": [
  {"@type": "Thing", "name": "Proteína animal"},
  {"@type": "Thing", "name": "Postura de ovos em aves"},
  {"@type": "Thing", "name": "Calopsita"},
  {"@type": "Thing", "name": "Tenébrio"}
],
"mentions": [
  {"@type": "Thing", "name": "Calopsita"},
  {"@type": "Thing", "name": "Periquito"},
  {"@type": "Thing", "name": "Tenébrio"}
]
```

**O que falta:** 12 artigos precisam de entity mentions semânticas

---

## 🔴 O QUE FALTA (Oportunidades)

### ❌ 1. Product Schema
**Status:** 0/∞

Nenhum artigo tem Product Schema. Crítico para:
- Tenébrio Vivo / Desidratado
- Minhoca Californiana
- [Futuros] Mosca Soldado, etc.

**Impacto:** Google não entende que você vende esses produtos

**Exemplo necessário:**
```json
{
  "@type": "Product",
  "name": "Tenébrio Vivo Premium — 50 Larvas",
  "description": "Larvas vivas criadas com gut loading...",
  "offers": {
    "@type": "Offer",
    "price": "49.90",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "245"
  },
  "suitableForAnimal": ["Gecko", "Pogona", "Ouriço-Pigmeu"]
}
```

### ❌ 2. Entity Linking Semântico (No Corpo)
**Status:** 0% (apenas na seção "Leia também")

**Situação atual:**
- Links estão concentrados no final de cada artigo
- Não há linking semântico no corpo do texto
- Exemplo: post sobre "Enriquecimento" nunca menciona "Tenébrio" como link

**O que falta:**
- Primeira menção de "Gecko" → link para `/alimentacao-natural-repteis/`
- Primeira menção de "Postura" → link para `/proteina-animal-para-aves-reproducao/`
- Primeira menção de "Muda de penas" → link para `/proteina-animal-para-aves-reproducao/`
- Etc.

### ❌ 3. Hub Semântico (Página Pilar)
**Status:** 0/1

**Necessário criar:**
- Página pilar: `/blog/alimentacao-natural-pets-exoticos/`
- Que agrupe TODOS os clusters semânticos
- Que linke pra subclusters

**Modelo atual:** Cada artigo é independente (sem hub central)

### ❌ 4. Featured Snippet Optimization
**Status:** 0% (nenhum artigo otimizado para snippets)

**O que falta:**
- Revisar primeiras 50-60 palavras (deve responder a pergunta concisamente)
- Estruturar FAQs como `<h2>P: Pergunta?</h2>` `<p>R: Resposta.</p>`
- Criar tabelas HTML semânticas pra comparações
- Listar passos em `<ol>` ou `<ul>` estruturado

**Artigos candidatos:**
1. 🔴 Alta: `tenebrio-para-pets-exoticos` (definição + tipos)
2. 🔴 Alta: `larvas-de-tenebrio-diferencas-nutricionais` (tabela comparativa)
3. 🔴 Alta: `como-conservar-tenebrio-vivo` (lista de passos)
4. 🟡 Média: `alimentacao-natural-passaros-exoticos` (guia completo)
5. 🟡 Média: `protei-animal-para-aves-reproducao` (já tem FAQ)

### ❌ 5. GEO (Generative AI Optimization)
**Status:** 0% (nenhum artigo otimizado para IAs)

**O que falta:**
- Revisar primeiras 3 linhas (resposta direta)
- Adicionar dados concretos (números, endereço, prazo)
- Criar seções FAQ estruturadas
- Implementar schema FAQPage em todos

**Teste necessário:** Perguntar ao ChatGPT/Perplexity/Gemini sobre "nutrição de pets exóticos" e verificar se Ecotenébrios aparece

### ❌ 6. Variações Semânticas (LSI Keywords)
**Status:** Parcial

**Exemplo atual:** Artigos usam "Tenébrio" mas não exploram variações:
- "Tenebrio molitor"
- "Larva de tenébrio"
- "Inseto vivo para réptil"
- "Proteína natural para animais"
- "Alimentação viva para gecko"

### ❌ 7. Estrutura de Dados Estendida
**Status:** 0%

**Faltam schemas:**
- `VideoObject` (se produzir vídeos)
- `NewsArticle` ou `Article` (se quiser expandir)
- `Place` (Tatuí, SP como localização física)
- `AggregateRating` (para avaliações)

---

## 📊 Resumo Quantitativo

| Elemento | Implementado | Faltando | Prioridade |
|----------|--------------|----------|-----------|
| BlogPosting | 13/13 (100%) | 0 | ✅ Pronto |
| LocalBusiness | 1/1 (100%) | 0 | ✅ Pronto |
| FAQPage | 4/13 (31%) | 9 | 🔴 ALTA |
| Breadcrumb | 1/13 (8%) | 12 | 🔴 ALTA |
| Entity Mentions | 1/13 (8%) | 12 | 🔴 ALTA |
| Product Schema | 0/∞ (0%) | ∞ | 🟡 MÉDIA |
| Entity Linking (corpo) | 0% | 100% | 🔴 ALTA |
| Hub Semântico | 0/1 (0%) | 1 | 🟡 MÉDIA |
| Featured Snippets | 0% | 100% | 🟡 MÉDIA |
| GEO Optimization | 0% | 100% | 🟡 MÉDIA |

---

## 🚀 Roadmap Priorizado (4 Semanas)

### **Semana 1 — Foundation (Schemas Rápidos)**
**Tempo estimado:** 3-4 horas

- [ ] Adicionar FAQPage Schema aos 9 artigos restantes
- [ ] Adicionar Breadcrumb Schema aos 12 artigos restantes
- [ ] Adicionar `about/mentions` aos 12 artigos restantes

**Resultado:** 3 schemas implementados em todos os artigos

### **Semana 2 — Entity Linking (Semântico)**
**Tempo estimado:** 4-5 horas

- [ ] Revisar cada artigo e adicionar links semânticos no corpo (não apenas final)
- [ ] Mapear: 1ª menção de Gecko → link; 1ª menção de Postura → link; etc.
- [ ] Testar com Ctrl+F cada artigo

**Resultado:** 100+ novos links semânticos distribuídos nos artigos

### **Semana 3 — Featured Snippets + Hub**
**Tempo estimado:** 5-6 horas

- [ ] Revisar 5 artigos candidatos a featured snippets
- [ ] Reescrever primeiras 50-60 palavras (resposta concisa)
- [ ] Criar Breadcrumb visual (não apenas schema)
- [ ] Criar página hub: `/blog/alimentacao-natural-pets-exoticos/`

**Resultado:** 5 artigos otimizados para position zero; hub criado

### **Semana 4 — GEO + Monitoramento**
**Tempo estimado:** 3-4 horas

- [ ] Revisar primeiras 3 linhas de cada artigo (dados concretos)
- [ ] Testar em ChatGPT/Perplexity/Gemini
- [ ] Implementar Google Search Console monitoring
- [ ] Documentar baseline de rankings

**Resultado:** Artigos otimizados para IAs; monitoramento iniciado

---

## 💡 Quick Wins (Fáceis de Fazer Hoje)

1. **Copiar schema Breadcrumb** do artigo novo para todos os 12 antigos (5 min/artigo = 1 hora)
2. **Copiar schema de Entity Mentions** do artigo novo para todos os 12 antigos (3 min/artigo = 36 min)
3. **Validar todos os schemas** com https://validator.schema.org/ (2 min/artigo = 26 min)

**Total: ~2 horas de trabalho puro**

---

## 🎯 Próximo Passo

**Opção A:** Automatizar com script (criar template + copiar em bulk)  
**Opção B:** Fazer manualmente (garantido correto, mas mais tempo)  
**Opção C:** Combinar (schema simples em bulk, conteúdo semântico manual)

**Recomendação:** Opção C é a melhor relação tempo/qualidade.

---

**Documento gerado:** 2 de julho de 2026  
**Status geral:** 60% implementado, 40% a fazer