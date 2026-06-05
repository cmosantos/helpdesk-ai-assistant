# HelpDesk AI Assistant

Protótipo de assistente virtual com Inteligência Artificial para apoio ao suporte técnico N1.

## Visão Geral

O **HelpDesk AI Assistant** é um assistente virtual simples criado para ajudar pessoas usuárias em dúvidas comuns de suporte técnico corporativo. O projeto utiliza uma base de conhecimento organizada para responder sobre temas como Microsoft 365, Outlook, Teams, senha, MFA, OneDrive, lentidão no computador e abertura de chamados.

A proposta do projeto é demonstrar como um assistente de IA pode apoiar o atendimento inicial, orientar o usuário de forma clara e reduzir dúvidas repetitivas antes do encaminhamento para o time de suporte.

Este projeto foi desenvolvido como entrega do Lab **Construa Seu Assistente Virtual Com Inteligência Artificial**, da DIO.

## Problema

Em ambientes corporativos, muitas solicitações de suporte são recorrentes e poderiam receber uma primeira orientação automática. Usuários geralmente precisam de respostas simples, rápidas e seguras sobre problemas do dia a dia, como falha de acesso, dificuldade com e-mail, MFA, Teams ou lentidão no computador.

O desafio é criar um assistente que consiga responder com base em informações previamente organizadas, evitando respostas inventadas e indicando abertura de chamado quando não houver informação suficiente.

## Solução

O assistente consulta uma base de conhecimento local em formato JSON e identifica o assunto mais próximo da dúvida informada pelo usuário. A partir disso, retorna uma orientação inicial com passos simples de troubleshooting e informa quando a demanda deve ser escalada para atendimento técnico.

O foco não é substituir o analista de suporte, mas apoiar o primeiro contato, melhorar a triagem e orientar o usuário com segurança.

## Público-Alvo

O projeto foi pensado para:

- Usuários corporativos que precisam de suporte inicial.
- Times de Service Desk ou Help Desk N1.
- Analistas de suporte que desejam organizar conhecimento técnico em formato reutilizável.
- Estudantes que querem criar um projeto simples de IA aplicado à área de TI.

## Funcionalidades

- Conversa simples via terminal.
- Consulta a uma base de conhecimento estruturada.
- Respostas baseadas em temas previamente cadastrados.
- Tratamento para perguntas fora do escopo.
- Orientação para abertura de chamado quando necessário.
- Registro de cenários de teste e métricas de avaliação.

## Estrutura do Repositório

```text
helpdesk-ai-assistant/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── base_conhecimento_suporte.json
│   └── cenarios_teste.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   ├── 05-pitch.md
│   └── 06-relatorio-testes.md
├── src/
│   └── app.py
└── assets/
    └── arquitetura.md
```

## Como Executar

Pré-requisito: ter o Python instalado.

Clone ou baixe este repositório e execute:

```bash
cd helpdesk-ai-assistant
python src/app.py
```

Depois, digite uma dúvida de suporte técnico, por exemplo:

```text
Meu Outlook não abre
```

ou:

```text
Não consigo acessar o Teams
```

Para sair, digite:

```text
sair
```

## Exemplos de Uso

### Entrada

```text
Meu Outlook não está abrindo.
```

### Saída Esperada

```text
Entendi sua dúvida sobre Outlook. Tente reiniciar o aplicativo, verificar a conexão com a internet e abrir o Outlook pelo navegador. Se o erro continuar, informe a mensagem exibida e abra um chamado para análise do suporte.
```

### Entrada

```text
Meu MFA não chega no celular.
```

### Saída Esperada

```text
Entendi sua dúvida sobre autenticação multifator. Verifique se o celular está com internet, se o aplicativo Microsoft Authenticator está instalado e se as notificações estão permitidas. Se você trocou de aparelho ou perdeu acesso ao aplicativo, será necessário acionar o suporte para redefinição segura do MFA.
```

## Como o Assistente Evita Respostas Inventadas

O assistente responde apenas quando encontra relação entre a pergunta do usuário e os temas presentes na base de conhecimento. Quando não encontra informação suficiente, ele informa que não possui dados confiáveis para responder e recomenda abertura de chamado.

Essa abordagem reduz o risco de respostas inventadas e reforça o uso responsável da IA no suporte técnico.

## Métricas de Avaliação

Foram consideradas as seguintes métricas:

- Assertividade da resposta.
- Resposta dentro da base de conhecimento.
- Clareza para o usuário final.
- Indicação correta de escalonamento.
- Taxa de respostas seguras para dúvidas fora do escopo.

Os detalhes estão no arquivo [`docs/04-metricas.md`](docs/04-metricas.md).

## Possíveis Melhorias Futuras

- Criar interface web com Streamlit.
- Integrar com API de LLM.
- Conectar com uma base real de artigos de conhecimento.
- Registrar histórico de conversas.
- Integrar com ferramenta de chamados.
- Criar avaliação automática das respostas.

## Tecnologias Utilizadas

- Python
- JSON
- Markdown
- Conceitos de IA generativa
- Base de conhecimento
- Engenharia de prompts

## Autor

Projeto desenvolvido por **Cláudio Menezes de Oliveira Santos** como parte de estudos em Inteligência Artificial, suporte técnico e automação aplicada à área de TI.
