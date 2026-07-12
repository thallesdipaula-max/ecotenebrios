---
name: Ecotenébrios Design System
description: Sistema visual baseado no conceito "The Naturalist's Workbench" (O Laboratório do Naturalista) para alimentação natural premium.
colors:
  primary: "#6B8E71"
  primary-dark: "#4a5f4e"
  secondary: "#A8C9B5"
  neutral-bg: "#F5F1E8"
  neutral-text: "#1A1A1A"
  border: "#e0dcd0"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "clamp(1.75rem, 5vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
rounded:
  sm: "8px"
  md: "12px"
  lg: "20px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  button-primary-hover:
    backgroundColor: "{colors.primary-dark}"
  blog-card:
    backgroundColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "24px"
---

# Design System: Ecotenébrios

## 1. Overview

**Creative North Star: "The Naturalist's Workbench" (O Laboratório do Naturalista)**

A atmosfera do design é **orgânica e prática**, focando em uma experiência limpa e calorosa que transmite segurança, profissionalismo e a proximidade do manejo artesanal da Raíssa. O visual rejeita o aspecto industrial e impessoal das marcas pet massificadas ou a frieza de layouts tecnológicos.

### Key Characteristics:
- **Orgânico**: Cores de terra, folhas e linho que se relacionam com a alimentação natural viva e desidratada.
- **Estruturado**: Informações e dados organizados em tabelas de fácil escaneabilidade e boxes informativos claros.
- **Humano**: Imagens reais e autorais, valorizando o cuidado em cada lote e o carinho no preparo da nutrição.

## 2. Colors

A paleta de cores reflete a natureza, saúde e vitalidade dos pets exóticos, usando variações de verde, terra e areia.

### Primary
- **Verde Folha Orgânico** (#6B8E71): Usado nos elementos principais da marca, botões de ação e títulos de seção para transmitir saúde e natureza.
- **Verde Floresta Fechada** (#4a5f4e): Usado nos estados de hover, links e textos destacados que necessitam de contraste elevado.

### Secondary
- **Verde Menta Suave** (#A8C9B5): Usado como cor de apoio, backgrounds secundários de tags e badges para suavizar áreas informativas.

### Neutral
- **Areia Quente Suave** (#F5F1E8): Cor de fundo principal de toda a aplicação, que confere um tom aconchegante e natural ao site.
- **Quase Preto / Carvão** (#1A1A1A): Usado para textos de corpo e títulos, mantendo leitura confortável e alta legibilidade.
- **Linho Muted / Cinza Quente** (#e0dcd0): Usado em bordas e divisores discretos.

## 3. Typography

A tipografia utiliza fontes do sistema para carregamento ultra-rápido, mantendo foco na facilidade de leitura e estrutura de conteúdo.

**Display Font:** System Default Sans (Inter / Segoe UI / SF Pro)
**Body Font:** System Default Sans

### Hierarchy
- **Display / H1** (Bold 700, clamp(1.75rem, 5vw, 3rem), 1.2, letterSpacing -0.02em): Usado no título principal da landing page e títulos de postagens.
- **Headline / H2** (Bold 700, var(--font-size-2xl) ~32px, 1.3): Usado para títulos de seções secundárias e grandes divisões.
- **Title / H3** (Bold 700, var(--font-size-xl) ~24px, 1.3): Usado em subseções e títulos de posts do blog.
- **Body** (Regular 400, 16px, 1.6): Texto corrido de leitura confortável, limitado a uma largura de no máximo 75ch para evitar fadiga ocular.
- **Label / Tag** (Bold 700, 11px, letterSpacing 0.05em, UPPERCASE): Usado em categorias, tags de pets e botões menores.

## 4. Elevation

O sistema utiliza um design essencialmente plano, focado em linhas finas e contraste de cores. Profundidade e elevação física são reservadas para indicar interatividade e foco do usuário (hover/active states).

### Shadow Vocabulary
- **Interactive Shadow (Hover)** (`box-shadow: 0 12px 24px rgba(107, 142, 113, 0.12)`): Usado ao passar o mouse sobre os cards de produto e blog para dar sensação de elevação tátil.
- **Rest Shadow (Card)** (`box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02)`): Shadow imperceptível usada em elementos em repouso sobre o fundo areia.

## 5. Components

### Buttons
- **Shape:** Cantos levemente arredondados de 8px.
- **Primary:** Fundo Verde Folha (#6B8E71), texto branco, padding de 16px 32px.
- **Hover / Focus:** Fundo transita suavemente para Verde Floresta (#4a5f4e) com efeito de transição cúbica de 0.3s.

### Cards / Containers
- **Corner Style:** Arredondamento suave de 12px.
- **Background:** Branco sólido.
- **Border:** Bordas finas de 1px solid (#e0dcd0).
- **Internal Padding:** 24px (md) ou 32px (lg) para garantir boa respiração interna.

### Tags / Badges
- **Style:** Arredondamento total (cápsula / 20px), fundo creme suave (#f0ebe0) e texto cinza (#555).
- **Interactive State:** Ao passar o mouse, o fundo transita para Verde Menta (#A8C9B5) e o texto para Verde Floresta (#4a5f4e).

## 6. Do's and Don'ts

### Do:
- **Do** Manter o fundo principal na cor Areia Quente (#F5F1E8) para dar consistência orgânica à marca.
- **Do** Garantir que a largura do bloco de texto dos posts não passe de 75ch para melhor conforto de leitura.
- **Do** Usar imagens reais e WebP compactadas para garantir carregamento ultra-rápido do site.
- **Do** Utilizar as tags e badges no formato de pílulas arredondadas para catalogar as espécies e categorias.

### Don't:
- **Don't** Usar gradientes de cores de tecnologia (roxo, azul neon) nas seções ou botões do site.
- **Don't** Exceder o arredondamento de 12px em cards de blog ou caixas de texto (evitar visual excessivamente infantil ou arredondado).
- **Don't** Usar sombras pretas carregadas (usar sempre sombras leves com base na tonalidade verde da marca).
- **Don't** Adicionar barras de bordas laterais espessas (ex: `border-left: 4px solid ...`) como detalhes decorativos em cards ou caixas de avisos.
