# 06 - Relatório de Testes

## Objetivo

Este relatório registra testes simples realizados com o HelpDesk AI Assistant para validar se o protótipo responde corretamente com base na base de conhecimento.

## Testes Realizados

## Teste 1 - Outlook

Entrada:

```text
Meu Outlook não abre.
```

Resultado esperado:

O assistente deve identificar o tema Outlook e orientar reiniciar o aplicativo, testar acesso pelo navegador e abrir chamado se o erro continuar.

Status: aprovado.

## Teste 2 - MFA

Entrada:

```text
Troquei de celular e meu Authenticator não funciona.
```

Resultado esperado:

O assistente deve identificar problema de MFA e recomendar acionamento do suporte para redefinição segura.

Status: aprovado.

## Teste 3 - Teams

Entrada:

```text
Não consigo entrar na reunião do Teams.
```

Resultado esperado:

O assistente deve identificar Microsoft Teams e sugerir testes no aplicativo, navegador, conta correta, áudio, câmera e login.

Status: aprovado.

## Teste 4 - Fora do Escopo

Entrada:

```text
Como configuro um servidor de produção?
```

Resultado esperado:

O assistente deve informar que não encontrou informação suficiente na base de conhecimento e recomendar abertura de chamado ou consulta a especialista.

Status: aprovado.

## Conclusão

O protótipo conseguiu responder adequadamente aos cenários principais. A solução ainda é simples, mas demonstra de forma clara o uso de base de conhecimento, regras de segurança e resposta orientada ao usuário.
