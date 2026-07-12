---
name: planejar-instagram
description: >
  Planeja a grade de conteúdo semanal (5-7 posts) para o Instagram da Ecotenébrios, baseando-se nos pilares da marca, tom de voz educativo/conversacional e na estratégia do negócio.
  Use quando o usuário pedir "/planejar-instagram", "planejar posts", "planejamento semanal", "grade de conteúdo" ou "criar calendário editorial".
---

# /planejar-instagram — Planejamento Editorial Semanal

Esta skill automatiza a criação do calendário semanal de conteúdo para o Instagram da Ecotenébrios (@ecotenebrio.tenebrios), garantindo consistência, relevância e alinhamento estratégico com o negócio operado pela Raíssa.

---

## Dependências e Arquivos de Referência

Antes de planejar qualquer linha de conteúdo, **você deve ler**:
- **Contexto do Negócio:** `_memoria/empresa.md`
- **Diretrizes Estratégicas:** `_memoria/estrategia.md` (identificar o foco atual, ex: frete, engajamento)
- **Pilares & Benefícios:** `_memoria/diferencias-beneficios.md` (Proteína, Enriquecimento, Manejo, Bem-estar)
- **Tom de Voz:** `_memoria/preferencias.md`
- **Padrão Visual:** `identidade/design-guide.md`
- **Ativos de Imagem Disponíveis:**
  - `web/assets/images/logo.png` (Logo oficial transparente)
  - `web/assets/images/hero.png` (Foto hero: Tenébrios vivos na palma da mão)
  - `web/assets/images/produto-1.jpg` (Tenébrios vivos no substrato)
  - `web/assets/images/produto-2.jpg` (Tenébrios desidratados no pote de vidro)
  - `web/assets/images/produto-3.jpg` (Minhocas californianas na terra)

---

## Workflow em 4 Passos

### Passo 1 — Definição do Foco Semanal

Pergunte à Raíssa se existe algum foco ou novidade específica para esta semana (ex: focar em frete grátis para a região, chegada de novo lote de tenébrios vivos, conscientização sobre répteis no inverno, etc.). 
*Se ela disser que não ou preferir que você decida, monte uma grade equilibrada cobrindo os 4 pilares principais.*

### Passo 2 — Geração da Grade de Conteúdo (5 a 7 Posts)

Gere uma tabela clara com a proposta de planejamento para a semana, seguindo a seguinte estrutura de colunas:

| Dia | Título / Headline do Post | Objetivo | Formato | Pilar & Ativo Visual Sugerido |
| :--- | :--- | :--- | :--- | :--- |
| **Seg** | *Headline instigante* | Educação / Conexão... | Carrossel / Reels... | Pilar abordado + Foto específica (`produto-X.jpg`) |
| ... | ... | ... | ... | ... |

#### Regras para a Grade:
1. **Alternância de Formato:** Não use o mesmo formato em dias seguidos (intercale Carrossel de Texto, Carrossel com Fotos reais do produto, Reels informativo e Post Único).
2. **Equilíbrio de Objetivos:** A grade deve ter:
   - **60% Conteúdo Educativo/Valor** (ensinar como cuidar do pet, curiosidades de manejo).
   - **20% Prova Social/Bastidores** (o manejo artesanal feito pela Raíssa, feedback de clientes).
   - **20% Venda Direta/Conversão** (como comprar via WhatsApp, catálogo de preços).
3. **Alternância Visual de Capas:** Para manter o feed lindo:
   - Alternar capas claras, capas escuras e capas com fotos reais dos produtos.

### Passo 3 — Aprovação e Detalhamento

Apresente a tabela e peça a aprovação da Raíssa. Uma vez aprovada (ou após os ajustes solicitados), gere o briefing detalhado de cada post planejado.

Para cada post, entregue:
1. **Briefing Visual:**
   - Se for **Carrossel**: Roteiro slide a slide (Capa + 3 a 5 slides de conteúdo + CTA final), indicando cores de fundo baseadas no `design-guide.md` e a imagem a ser usada.
   - Se for **Reels**: Roteiro com gancho (hook) nos primeiros 3 segundos, instruções de cena e texto falado/legenda do vídeo.
   - Se for **Post Único**: Design do card e texto principal.
2. **Legenda Final (Pronta para copiar):**
   - **Hook:** Começar com uma pergunta ou afirmação forte que conecte com o dono do pet exótico.
   - **Desenvolvimento:** Texto fluído, dinâmico, dividido em parágrafos curtos.
   - **CTA (Chamada de Ação):** Direcionar para o link da bio (WhatsApp) ou incentivar salvamento/comentário.
   - **Bloco de Hashtags:** 10-15 hashtags relevantes (ex: #ecotenebrios #alimentacaonatural #petsexoticos #tenebrio #minhocacaliforniana #repteisbrasil).

### Passo 4 — Salvamento e Organização

Crie uma pasta com a data da semana em `marketing/instagram/planejamentos/semana-YYYY-MM-DD/` e salve o planejamento completo em um arquivo `planejamento.md`.

*Dica de Integração:* Se o formato escolhido for Carrossel, você pode instruir a Raíssa a chamar a skill **`/carrossel`** usando o texto detalhado gerado para renderizar as imagens automaticamente!

---

## Regras Críticas de Comunicação e Tom de Voz

- **Nunca use clichês de marketing digital** como *"Você não vai acreditar!"*, *"O segredo que não te contam"*, ou chamadas agressivas de vendas.
- **Seja Científico mas Acessível:** Explique que o tenébrio possui ômegas 6 e 9 de forma simples, mostrando que isso traz brilho às penas de pássaros ou melhora a pele de lagartos.
- **Fale em Nome da Raíssa:** Use a primeira pessoa do singular de forma humilde e responsável quando for post de bastidores (ex: *"Tudo que sai da Ecotenébrios passa pelas minhas mãos..."*).
- **Sem Emojis Decorativos Excessivos:** Use emojis de forma inteligente e natural (máximo 1-2 por parágrafo, nunca no meio de frases importantes).
- **Cores & Fontes:** Siga estritamente o bege/creme `#F5F1E8`, verde `#6B8E71` e o preto `#1A1A1A` nas sugestões visuais.
