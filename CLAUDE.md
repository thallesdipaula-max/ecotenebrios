# MazyOS — Sistema operacional do negócio

Sua empresa roda em cima desse arquivo. Aqui ficam as regras de operação
do MazyOS — como o Claude lê o contexto, aprende com correções, mantém
tudo atualizado e cria skills novas conforme a operação evolui.

Esse arquivo é editável. Quando o `/instalar` rodar, ele complementa o
final dessa página com as regras específicas do seu negócio.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem
e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos

Usar essas informações como base pra qualquer resposta ou decisão. Ao
sugerir prioridades, formatos ou abordagens, considerar o foco atual
descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar
`identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas
usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante
em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se
não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o
usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o
padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma
instrução que parece permanente (frases como "na verdade é assim", "não
faça mais isso", "prefiro assim", "sempre que...", "evita...", "da
próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (clientes, serviços, mercado) → `_memoria/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato, o que evitar) → `_memoria/preferencias.md`
- **Sobre prioridades e foco** (projetos, metas, prazos) → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.
Confirmar mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na
verdade o arquivo se chama X"). Só perguntar quando a informação tiver
valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill
nova, mudança de foco, processo novo, ferramenta instalada, estrutura
alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Se sim, identificar o que atualizar:

- **Cliente, serviço, ferramenta, equipe** → `_memoria/empresa.md`
- **Mudança de prioridade ou foco** → `_memoria/estrategia.md`
- **Tom ou estilo** → `_memoria/preferencias.md`
- **Pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Visual (cores, fontes, logo)** → `identidade/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo
inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto (escrever um email avulso, criar um post)
- Perguntas simples ou conversas sem ação
- Mudanças já salvas pelo bloco "Aprender com correções"

**Dica:** rode `/atualizar` pra uma varredura completa quando houver dúvida.

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`. Se
   existir, usar como base e adaptar pro contexto
2. Perguntar se é específica desse projeto ou útil em qualquer:
   - Específica → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Universal → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar
   o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, exemplos),
   criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code

---

# Ecotenébrios — Regras operacionais

## O que é esse workspace

Operação da Ecotenébrios. Comercialização de alimentação natural para pets exóticos (minhocas, tenébrios, larvas), produção artesanal, 100% de responsabilidade da Raíssa (gestora/operadora solo).

**Estrutura de pastas:**
- `_memoria/` — contexto da empresa, preferências de comunicação, foco atual
- `identidade/` — marca visual (cores, logo, design-guide)
- `marketing/` — conteúdo Instagram, carrosséis, legendas, calendário editorial
- `comercial/` — propostas, materiais de venda, lista de clientes
- `operacoes/` — processos (produção, estoque, logística, atendimento)
- `financeiro/` — relatórios, fluxo de caixa, análise de vendas
- `dados/` — arquivos para análise (vendas, engajamento, feedback)
- `saidas/` — documentos pontuais, relatórios, exports
- `projetos/` — iniciativas que cruzam setores

## Sobre a empresa

**Ecotenébrios** é uma empresa de comércio eletrônico especializada em alimentação natural (viva e desidratada) para pets exóticos. Atuamos no segmento de nutrição premium para animais, atendendo donos que se preocupam com qualidade. Raíssa é responsável por toda a operação: produção artesanal, venda, atendimento, conteúdo.

## Foco da operação

**Principal gargalo:** Visibilidade (seguidores que engajam) e frete (caro, reduz conversão).

**Primeira alavanca:** Aumentar alcance e autoridade no Instagram através de conteúdo consistente, planejado e educativo. Automatizar o planejamento semanal (candidata a skill `/mapear-rotinas` depois).

**Próximas frentes:** Explorar anúncios pagos, otimizar SEO, parcerias com influenciadores de pets exóticos.

## Entregas frequentes

- **Conteúdo Instagram:** Carrosséis educativos, reels, stories (semanal)
- **Atendimento:** WhatsApp, respostas de dúvidas sobre produtos
- **Relatórios:** Vendas semanais, engajamento, estoque (monitoramento)

## Tom de voz

**Conversacional, educativo, descontraído mas não informal.** Faz perguntas pra engajar. Explica os benefícios dos produtos (nutrição, cuidado) sem parecer vendedor. Usa emojis naturalmente. Linguagem normal, equilibrada — evita formalismo excessivo e gírias.

**Referência:** Legendas reais do Instagram (@ecotenebrio.tenebrios) que educam enquanto vendem.

## Regras de organização

- Conteúdo Instagram: salvar em `marketing/instagram/` (carrosséis, briefings, calendário)
- Atendimento/FAQ: documentar em `operacoes/faq.md`
- Análises de vendas/engajamento: `dados/`
- Relatórios periódicos: `financeiro/relatorios/`
- Ideias para skills: acompanhar em `estrategia.md` (tarefas repetidas)

## Ferramentas conectadas

- [x] Instagram (@ecotenebrio.tenebrios) — principal canal
- [x] WhatsApp — atendimento direto
- [x] Google Search Console — conectado para monitoramento de SEO
- [ ] Google Ads — para explorar depois
- [ ] Meta Ads — para explorar depois
- [ ] Google Analytics — se tiver site

## Skills criadas

- **✅ `/planejar-instagram`** — gera planejamento semanal de 5-7 posts educativos (automatiza tarefa repetitiva)

## Próximas skills a criar

- Analisar dados de vendas e engajamento automaticamente
- Gerar carrosséis educativos com templates
