# Registro de Deploy: Nova Página /comprar/ e Carrossel Interativo da Home

> **Data de Execução**: 20/09/2026  
> **Responsável**: Estrategista de SEO Semântico (Sócrates) & Frontend Craft  
> **Status**: Commitado localmente no branch `main` pronto para envio  
> **Commits Realizados**:
> - `d172d10`: *feat(home): elegant 3-column product grid on desktop and swipe carousel on mobile*
> - `4eec359`: *feat(home): upgrade desktop carousel with floating side navigation and 3-card slide view*
> - `7c7cfdc`: *feat(carousel): add mobile animated swipe badge and dynamic pagination dots*
> - `8e74a14`: *feat(home): implement horizontal snap-scroll product carousel*
> - `08c9abd`: *feat(shop): redesign premium /comprar/ checkout using naturalist workbench system*

---

## 1. 🛍️ O Que Foi Desenvolvido

### A. Página Interativa de Montagem de Pedidos (`/comprar/`)
* **Visual The Naturalist's Workbench**:
  - Tons terrosos e naturais (`#FAF8F3`, verde sálvia `#6B8E71`, verde floresta `#2D3B2D`).
  - Cards táteis com steppers interativos (`+` e `−`) com tamanho ergonômico (44×44px) e animação de clique.
* **Mecanismo de Desconto Progressivo (*Combo Meter*)**:
  - **1 item**: Preço cheio unitário com link rápido InfinitePay.
  - **2 itens**: Barra avança e desbloqueia automaticamente **5% OFF**.
  - **3 ou mais itens**: Barra atinge 100% e ativa **10% OFF no pedido todo**.
* **Recibo de Compra Fixo (*Sticky Receipt Card*)**:
  - Acompanha o scroll com subtotal dinâmico, linha de desconto visual e total a pagar.
  - **Botão WhatsApp Master**: Monta uma mensagem com formatação rica contendo itens, desconto, região de frete, nome, cidade e espécie do pet.
* **Chips de Espécies de Pets**:
  - Atalhos táteis em 1 clique para Gecko, Calopsita, Trinca-Ferro, Ouriço, Pogona, Peixes e Roedores.
* **Barra Flutuante Mobile**:
  - Permite ao tutor finalizar o pedido no WhatsApp a qualquer momento no smartphone sem rolar até o fim da página.

---

### B. Carrossel Horizontal de Produtos na Home (`index.html`)
* **Substituição de Seções Verticais**: As seções empilhadas de oferta foram unificadas em uma vitrine horizontal dinâmica com *CSS Scroll-Snap*.
* **Otimização para Desktop**: Setas de navegação lateral (`‹` e `›`) para avançar no mouse.
* **Otimização para Mobile**:
  - **Selo animado com pulso lateral**: `👉 Deslize para o lado para ver todos os alimentos`.
  - **Bolinhas de Paginação Dinâmicas**: 4 indicadores (*dots*) sincronizados em tempo real com o deslize do dedo e clicáveis.
  - **Efeito Visual de Próximo Card (*Card Peeking*)**: `85vw` para mostrar a borda do próximo produto e estimular o arraste.

---

## 2. 🔗 Catálogo Oficial & Links de Pagamento

| Produto | Preço | Link InfinitePay Oficial | Modalidade de Frete |
|---|---|---|---|
| **Kit Premium Tenébrios Vivos** | R$ 49,90 | [Link InfinitePay](https://link.infinitepay.io/raissa-sarles/VC1DLTEtSQ-bzfv7yiX4U-49,90) | Frete Grátis Brasil |
| **Tenébrios Desidratados 50g** | R$ 39,90 | [Link InfinitePay](https://link.infinitepay.io/raissa-sarles/VC1DLTEtSQ-HgH3GDr86l-39,90) | Envio Climatizado |
| **Minhocas Californianas 50un** | R$ 39,90 | [Link InfinitePay](https://link.infinitepay.io/raissa-sarles/VC1DLTEtSQ-RCdQTtivbb-39,90) | Envio Climatizado |
| **WhatsApp Oficial (Raíssa)** | — | [wa.me/5515981098418](https://wa.me/5515981098418) | Atendimento Direto |

---

## 3. ⚡ Otimizações de Performance & Acessibilidade (Auditoria PageSpeed Insights)

Com base no diagnóstico do PageSpeed Insights mobile:
1. **Acessibilidade (Meta 100/100)**:
   - **Contraste de Cores (WCAG AA)**: Ajustadas as cores de botões verdes (Hero WhatsApp e Montar Pedido Combo) de `#25D366` para verde esmeralda escuro (`#128C7E` / `#1B6E39`), elevando a taxa de contraste para > 4.8:1 contra texto branco.
   - **Área de Toque (*Target Size*)**: Adicionada área clicável transparente de 44×44px (`::after`) aos indicadores de paginação do carrossel (`.carousel-dot`).
   - **Nomes Acessíveis Únicos**: Adicionados atributos `aria-label` descritivos individuais para os botões de checkout e artigos recomendados.

2. **Performance & Core Web Vitals (Meta 95+)**:
   - **Eliminação de *Forced Reflow***: O listener de `scroll` do carrossel teve o cálculo de `offsetWidth` desacoplado e colocado em cache na inicialização e no `resize`, zerando os 48ms de recálculo forçado de layout.
   - **Otimização de Carregamento de Fontes**: Inclusão de `@font-face` com `font-display: swap` para a biblioteca de ícones Phosphor.
   - **Adiantamento Inteligente de Scripts de Terceiros**: Carregamento assíncrono do Meta Pixel (`fbevents.js`) postergado via `requestIdleCallback` (3.5s) ou na primeira interação do usuário, liberando a thread principal e eliminando tarefas longas de TBT.
   - **Animações Compostas**: Variável `--transition` otimizada para transicionar apenas propriedades de compositor (`opacity`, `transform`, `background-color`, `box-shadow`) em vez de propriedades de layout geométrico (`all`).

---

## 4. 🚀 Como Subir Para Produção (GitHub Pages)

No seu terminal com permissão do Git, execute:
```powershell
git push origin main
```
Assim que enviado, o GitHub Pages atualizará o site oficial instantaneamente em:
* **Home:** `https://ecotenebrios.com.br/`
* **Página de Compras:** `https://ecotenebrios.com.br/comprar/`
