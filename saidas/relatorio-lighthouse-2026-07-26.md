# Relatório Lighthouse — Ecotenébrios

**Data:** 26/07/2026 12:07 BRT  
**Ferramenta:** Lighthouse 13.4.0 / HeadlessChromium 149.0.7827.155  
**URL:** https://ecotenebrios.com.br/

---

## Resumo dos scores

| Categoria | Mobile | Desktop |
|---|---|---|
| **Performance** | **73** ⚠️ | **98** ✅ |
| **Acessibilidade** | **92** ✅ | **92** ✅ |
| **Práticas recomendadas** | **100** ✅ | **100** ✅ |
| **SEO** | **100** ✅ | **100** ✅ |
| **Navegação agêntica** | **2/2** ✅ | **2/2** ✅ |

---

## Métricas principais (Mobile)

| Métrica | Valor | Avaliação |
|---|---|---|
| FCP (First Contentful Paint) | **3,2 s** | ⚠️ Lento |
| LCP (Largest Contentful Paint) | **4,9 s** | ❌ Ruim |
| TBT (Total Blocking Time) | **70 ms** | ✅ Bom |
| CLS (Cumulative Layout Shift) | **0** | ✅ Perfeito |
| SI (Speed Index) | **4,8 s** | ⚠️ Lento |

## Métricas principais (Desktop)

| Métrica | Valor | Avaliação |
|---|---|---|
| FCP | **0,5 s** | ✅ Rápido |
| LCP | **0,8 s** | ✅ Rápido |
| TBT | **50 ms** | ✅ Bom |
| CLS | **0.063** | ⚠o Aceitável |
| SI | **0,8 s** | ✅ Rápido |

---

## Diagnóstico e ações prioritárias

### 🔴 Crítico — Impacta Performance Mobile

#### 1. Imagem hero sem otimização responsiva
**Economia estimada:** 116 KiB  
**Problema:** `hero.webp` (1024×1024, 54 KiB) exibida em 665×665. Também sem `fetchpriority="high"` e com `loading="lazy"` — a LCP não é priorizada.  
**Ação:** Redimensionar hero para ~700×700 com compressão adequada. Adicionar `fetchpriority="high"` e remover `loading="lazy"` da hero.

#### 2. Cache TTL muito curto (10 min)
**Economia estimada:** 377 KiB  
**Problema:** Imagens e CSS próprios com cache de apenas 10 minutos. Visitantes recorrentes baixam tudo de novo.  
**Ação:** Definir `Cache-Control: public, max-age=31536000, immutable` para assets estáticos (imagens, CSS, fontes). Usar hash nos nomes de arquivo para invalidar cache.

#### 3. Recursos que bloqueiam renderização
**Economia estimada:** 850 ms  
**Problema:** `style.css` (7,1 KiB) e Phosphor Icons via CDN (1,5 KiB) bloqueiam o primeiro paint.  
**Ação:** Inline do CSS crítico no `<head>` e carregar o restante com `media="print" onload="this.media='all'"`. Adiar Phosphor Icons ou carregar assincronamente.

#### 4. Cadeia de requisições crítica longa
**Latência máxima:** 1.482 ms  
**Problema:** O caminho crítico passa por 4 hops: HTML → style.css → Phosphor CDN → woff2 (144 KiB).  
**Ação:** Pré-conectar (`<link rel="preconnect">`) ao CDN `cdn.jsdelivr.net`. Carregar apenas os pesos de Phosphor usados (atualmente carrega 6 estilos: regular, thin, light, bold, fill, duotone).

#### 5. CSS não usado — Phosphor Icons
**Economia estimada:** 81 KiB  
**Problema:** Todos os 6 estilos do Phosphor são carregados, mas provavelmente só 1-2 são usados.  
**Ação:** Importar apenas os estilos efetivamente usados (ex.: apenas `regular` e `bold`).

#### 6. Imagens sem width/height explícitas
**Impacto:** CLS potencial  
**Problema:** Hero, logo e ofertas não têm `width`/`height` no HTML — o layout pode pular enquanto as imagens carregam.  
**Ação:** Adicionar `width` e `height` em todas as `<img>`.

#### 7. JavaScript não usado (Facebook Pixel)
**Economia estimada:** 62 KiB  
**Problema:** `fbevents.js` (103 KiB transferidos, 38 KiB não usados) e `config` (63 KiB, 24 KiB não usados).  
**Ação:** Carregar Pixel com `async` e considerar adiar para após a LCP.

### 🟡 Médio — Acessibilidade (score 92)

#### 8. Contraste insuficiente
**Elementos com falha:**
- FRETE GRÁTIS / FRETE GRÁTIS SP (`shipping-tag`)
- Perguntas do FAQ (ex.: "Quanto de tenébrio meu pet deve comer por dia?")
- Footer: WhatsApp, Instagram, copyright, descrição

**Ação:** Escurecer as cores do texto dos elementos `shipping-tag` e `faq-question` para atingir relação de contraste ≥ 4.5:1. No footer, garantir que o texto sobre o fundo atenda ao mínimo de contraste.

#### 9. Links idênticos com finalidades diferentes
**Problema:** Auditado como "práticas recomendadas" — links duplicados podem confundir leitores de tela.  
**Ação:** Revisar links do footer e garantir que descrições sejam únicas quando apontam para destinos diferentes.

### 🟢 Baixo — Otimizações finas

#### 10. Font-display
**Economia estimada:** 30 ms  
**Problema:** Phosphor woff2 sem `font-display: swap`.  
**Ação:** Adicionar `font-display: swap` via CSS ou certificar-se de que o CDN já envia o header correto.

#### 11. JavaScript legado
**Economia estimada:** 13 KiB  
**Problema:** Facebook Pixel contém polyfills Babel desnecessários para browsers modernos.  
**Ação:** Não aplicável (código de terceiros). Monitorar se há versão mais moderna do pixel.

#### 12. Redução de CSS (minificação)
**Economia estimada:** 3 KiB  
**Problema:** `duotone/style.css` do Phosphor (23 KiB) pode ser reduzido em 3 KiB.  
**Ação:** Ativar minificação no build ou usar uma CDN que sirva versão .min.css.

#### 13. Tarefas longas — 3 encontradas
**Problema:** Tarefas >50ms na thread principal podem causar jank.  
**Ação:** Se houver scripts próprios, avaliar se podem ser chunkados ou adiados.

---

## Plano de ação sumarizado

| Prioridade | Ação | Ganho estimado | Esforço |
|---|---|---|---|
| 1 | Otimizar hero (tamanho + fetchpriority) | LCP ↓ 1-2s | Baixo |
| 2 | Cache TTL longo em assets estáticos | 377 KiB economizados | Baixo |
| 3 | Inline CSS crítico + adiar resto | FCP ↓ 800ms | Médio |
| 4 | Carregar só estilos Phosphor usados | 81 KiB CSS eliminado | Baixo |
| 5 | Pré-conexão ao CDN jsdelivr | LCP ↓ 200-400ms | Muito baixo |
| 6 | Width/height em todas as imagens | CLS prevenido | Baixo |
| 7 | Corrigir contraste (shipping-tag, FAQ, footer) | Acessibilidade ↑ 100 | Baixo |
| 8 | Adiar Facebook Pixel | LCP ↓ ~300ms | Baixo |

---

## Observações

- **Mobile com desempenho 73:** O gargalo principal é o carregamento inicial (FCP 3.2s, LCP 4.9s). As imagens e CSS bloqueiam a renderização. Com as ações acima, é factível chegar a **85+** em mobile.
- **Desktop com 98:** Já está excelente. Pequenos ajustes de contraste e CLS (0.063 vindo de imagens sem dimensões) resolvem.
- **SEO 100 e Práticas 100:** Sem problemas nessas categorias.
- **Facebook Pixel é o maior peso morto:** 166 KiB transferidos, ~62 KiB não usados. Vale considerar carregar só depois da interação do usuário.
