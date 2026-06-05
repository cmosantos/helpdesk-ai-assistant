# 02 - Base de Conhecimento

## Objetivo da Base

A base de conhecimento do HelpDesk AI Assistant organiza informações comuns de suporte técnico N1. Ela serve como fonte principal para as respostas do agente.

O assistente não deve responder com base em suposições. Ele deve consultar os temas cadastrados e retornar orientações compatíveis com o conteúdo disponível.

## Arquivo Principal

A base está localizada em:

```text
data/base_conhecimento_suporte.json
```

## Estrutura dos Dados

Cada item da base possui os seguintes campos:

- `id`: identificador interno do tema.
- `tema`: assunto principal da dúvida.
- `palavras_chave`: termos usados para localizar o tema.
- `resposta`: orientação principal apresentada ao usuário.
- `perguntas_apoio`: perguntas que ajudam o suporte a entender melhor o problema.
- `quando_escalar`: orientação sobre quando abrir ou escalar um chamado.

## Temas Cadastrados

A primeira versão da base contém temas comuns em um Service Desk corporativo:

1. Outlook não abre ou apresenta erro.
2. Problemas de acesso ou uso do Microsoft Teams.
3. Problemas com MFA e Microsoft Authenticator.
4. Senha, bloqueio de conta e acesso corporativo.
5. OneDrive não sincroniza arquivos.
6. Computador lento ou travando.
7. Problemas de impressão.
8. Como abrir um chamado de suporte.

## Critério de Seleção da Resposta

O protótipo utiliza correspondência simples por palavras-chave. A pergunta do usuário é comparada com os termos cadastrados em cada tema. O tema com maior pontuação é escolhido.

Caso a pontuação seja baixa, o assistente considera que não há informação suficiente e responde de forma segura, orientando a abertura de chamado.

## Cuidados com Dados Sensíveis

A base não contém dados reais de usuários, senhas, tokens, e-mails corporativos ou informações confidenciais. Todos os dados são simulados para fins educacionais.

## Possíveis Evoluções

A base pode evoluir para incluir:

- Artigos de conhecimento internos.
- Procedimentos por categoria de chamado.
- Respostas por nível de criticidade.
- Integração com sistemas ITSM.
- Conteúdo em português e inglês para suporte global.
