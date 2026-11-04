# Perguntas e respostas dos labs de MCP

Registro do que foi pedido no Copilot e do que ele respondeu em 4 de novembro de 2026. Onde a resposta não foi colada no chat, isso está indicado.

## Lab 1 — Arquivos

Pasta de trabalho: `C:\Users\Natan\labs-mcp\lab1-workspace`

### Listar a pasta do lab

**Pergunta:** Use a ferramenta do servidor filesystem para listar o conteúdo de `C:\Users\Natan\labs-mcp\lab1-workspace`.

**Resposta:** A pasta não contém arquivos ou subpastas.

### Criar produtos.txt

**Pergunta:** Crie um arquivo chamado `produtos.txt` nessa pasta com 5 produtos fictícios, cada um com nome e preço.

**Resposta:** Arquivo criado com:

- Café Aurora — R$ 18,90
- Fone Nebulosa — R$ 129,90
- Caneca Pixel — R$ 34,50
- Mochila Vento — R$ 189,00
- Luminária Lunar — R$ 76,90

### Produto mais caro

**Pergunta:** Leia `produtos.txt` e diga qual é o produto mais caro.

**Resposta:** Mochila Vento, por R$ 189,00.

### Estrutura de pastas

**Pergunta:** Criar `src/`, `src/models/`, `src/controllers/`, `tests/` e um `README.md` na pasta do lab.

**Resposta:** Pastas e `README.md` criados. O README descreve o projeto de exemplo e a função de `src/models`, `src/controllers` e `tests`.

## Lab 2 — GitHub

Conta usada: `natanaelgsneto`.

### Issues recentes do VS Code

**Pergunta:** Liste as 5 issues abertas mais recentes do repositório `microsoft/vscode` e resuma cada uma.

**Resposta:**

1. #346135 — Copilot Chat: local code links in WSL lose GitLens integration compared with Explorer. Em uma janela WSL, abrir um arquivo pelo link do Copilot Chat não oferece a mesma integração do GitLens que o Explorer.
2. #346134 — Reduce cloud sandbox feed connection eagerness. Evitar conexões WebSocket de atualização do sandbox na nuvem quando o usuário não tem essas sessões.
3. #346128 — What's the point of using tunnels if they can never be connected for more than 10 minutes. Reinícios interrompem túneis e exigem reconexão manual.
4. #346127 — Tunnels don't work. Os túneis deixaram de conectar após uma atualização.
5. #346123 — Support CLI-first AI tooling with developer-controlled terminal execution. Melhor suporte a ferramentas de IA por CLI, com o terminal controlado pelo desenvolvedor.

### Issues com "performance" no título

**Pergunta:** No repositório `microsoft/vscode`, busque no máximo 5 issues abertas com "performance" no título. Responda só com número e título.

**Resposta:**

- #341284 — lag scroll and poor performance on the snap package instead of native ones
- #340858 — Agent chat: Performance issues
- #336928 — Degradation of startup performance since 1.129
- #335969 — Performance issues from version 1.133.0 onward
- #335388 — Copilot Chat: large streamed terminal output preview tanks UI performance/responsiveness

### Pull requests do cookbook

**Pergunta:** Liste os 3 pull requests mergeados mais recentes de `anthropics/anthropic-cookbook`. Responda apenas número e título.

**Resposta:**

- #958 — fix(registry): remove duplicate agent security review entry
- #959 — feat(managed_agents): add a dreaming cookbook
- #944 — Bring cookbooks up to Haiku 5.5 and the 2.0 SDK

A busca por search falhou por permissão do token. A lista acima veio da ferramenta de listar pull requests.

### Repositórios da conta

**Pergunta:** Liste os meus repositórios. Responda só com o nome completo.

**Resposta:** `natanaelgsneto/ColorirFotos`, `JMETER`, `LinguagemR`, `CursoCompletoLinguagemR_DSA_ACADEMY`, `CNU-CONTE-DO`, `SiteRepositorio`, `Convert-black-and-white-photo-to-color`, `crea`, `PowerBI_DSA-`, `Chatbot-wix`, `codigo-para-gerar-listas-e-cartoes-no-trelo`, `Automacao-de-Testes-com-Playwright-Python-e-Pytest`, `TrabalhoDeSilvia`, `natanaelgsneto-Automacao-python-with-Playwright-and-pytest`, `api_calculadora_swagger_yaml`, `CursoPostman`, `AnaliseDeDiscurso-`, `AnaliseSandra`, `CNU`, `Formacao-Completa-em-Inteligencia-Artificial-2026`, `Python-JupyterNotebook`.

### Issue de teste

**Pergunta:** Me dê os detalhes da issue #1 de `natanaelgsneto/api_calculadora_swagger_yaml`, incluindo os comentários.

**Resposta:** Issue #1, título "Lab 2 MCP", aberta, autor natanaelgsneto, criada em 04/11/2026 às 22:42 UTC. Corpo: "Issue de teste do Lab 2." Na primeira leitura não havia comentários. Link: https://github.com/natanaelgsneto/api_calculadora_swagger_yaml/issues/1

**Pergunta:** Adicione um comentário na issue #1 dizendo: "Testando o MCP do GitHub com o GitHub Copilot - Lab 2 do curso."

**Resposta:** Comentário adicionado nessa issue.

## Lab 3 — Páginas da web

### useActionState

**Pergunta:** Acesse https://react.dev/reference/react/useActionState e explique o que este hook faz. Depois gere um exemplo prático de formulário com validação de campos.

**Resposta:** `useActionState` conecta uma Action a um estado do componente. A Action recebe o estado anterior e os dados enviados, executa validações ou operações assíncronas e devolve um novo estado.

```js
const [state, formAction, isPending] = useActionState(action, initialState);
```

- `state`: resultado atual da Action
- `formAction`: função passada ao formulário em `action`
- `isPending`: indica se a Action está em andamento

O exemplo gerado foi um formulário de cadastro em React 19 com TypeScript, validando nome, e-mail, senha e confirmação de senha, e mostrando "Enviando..." enquanto `isPending` é verdadeiro.

### Outras perguntas deste lab

Estas perguntas foram enviadas. A resposta final do Copilot não foi colada neste chat:

- Quais são as novidades do Python 3.13? Liste as principais. Em seguida, acesse https://docs.python.org/3/whatsnew/3.13.html e liste as novidades com base na página.
- Acesse https://docs.pydantic.dev/latest/concepts/models/ e crie um modelo Pydantic de Pedido de e-commerce com id, cliente, itens, status e data de criação.
- Acesse https://modelcontextprotocol.io/introduction e faça um resumo executivo do MCP em no máximo 10 bullets.
- Compare o tratamento de erros em TypeScript nestas páginas e gere um guia rápido: https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html e https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

## Lab 4 — SQLite

Banco: `C:\Users\Natan\labs-mcp\lab4-workspace\loja.db`

### Tabelas

**Pergunta:** Use o servidor MCP sqlite. Quais tabelas existem no banco e qual é a estrutura de cada uma?

**Resposta:**

- `categorias`: `id` (INTEGER, chave primária), `nome` (TEXT, obrigatório)
- `produtos`: `id`, `nome`, `categoria_id`, `preco` (REAL), `estoque` (INTEGER, padrão 0)
- `clientes`: `id`, `nome`, `email`, `cidade`
- `pedidos`: `id`, `cliente_id`, `data_pedido`, `status` (padrão `concluido`)
- `itens_pedido`: `id`, `pedido_id`, `produto_id`, `quantidade`, `preco_unit`
- `sqlite_sequence`: tabela interna do SQLite para chaves AUTOINCREMENT

### Cinco produtos mais caros

**Pergunta:** Quais são os 5 produtos mais caros do catálogo? Responda só com nome e preço.

**Resposta:**

- Notebook Ultra Slim — R$ 5.899,00
- Notebook Pro 15" — R$ 4.299,90
- Monitor Ultrawide 34" — R$ 2.799,00
- Notebook Básico 14" — R$ 2.199,90
- Placa de Vídeo RTX 4060 — R$ 2.199,00

### Mês de maior faturamento

**Pergunta:** Qual foi o mês com maior faturamento total? Mostre o valor em reais.

**Resposta:** Novembro de 2024, com R$ 7.897,70.

### Clientes que mais gastaram

**Pergunta:** Quais são os 3 clientes que mais gastaram? Mostre o nome, o número de pedidos e o total gasto por cada um.

**Resposta:**

- Diego Alves — 2 pedidos — R$ 8.478,70
- Ana Costa — 3 pedidos — R$ 8.288,60
- Elena Souza — 2 pedidos — R$ 5.429,60

### Estoque baixo

**Pergunta:** Quais produtos estão com estoque abaixo de 10 unidades? Liste do menor estoque para o maior. Responda só com nome e estoque.

**Resposta:**

- Processador i7-13ª Gen — 3
- Monitor Ultrawide 34" — 4
- Placa de Vídeo RTX 4060 — 6
- Headset Gamer 7.1 — 7
- Notebook Ultra Slim — 8
- Monitor 27" QHD — 9

### Novo produto

**Pergunta:** Adicione um produto chamado "Teclado Mecânico RGB" na categoria "Periféricos", com preço de R$ 349,90 e estoque inicial de 25 unidades.

**Resposta:** Produto adicionado à categoria Periféricos (id 2), por R$ 349,90, com 25 unidades.

### Relatório de vendas

**Pergunta:** Gere um relatório com total de pedidos, faturamento total, ticket médio, produto mais vendido em quantidade e categoria com maior receita.

**Resposta:**

1. Total de pedidos: 15
2. Faturamento total: R$ 32.452,50
3. Ticket médio por pedido: R$ 2.163,50
4. Produto mais vendido: Mouse Wireless Ergonômico — 5 unidades
5. Categoria com maior receita: Notebooks — R$ 16.698,70
