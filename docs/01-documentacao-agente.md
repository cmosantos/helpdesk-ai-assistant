# 01 - Documentação do Agente

## Nome do Agente

**HelpDesk AI Assistant**

## Caso de Uso

O agente foi criado para apoiar o atendimento inicial de suporte técnico N1 em um ambiente corporativo. Ele responde dúvidas comuns sobre Microsoft 365, Outlook, Teams, MFA, OneDrive, senha, lentidão no computador, impressoras e abertura de chamados.

A ideia é oferecer uma primeira orientação rápida, simples e segura para a pessoa usuária antes do acionamento direto do time de suporte.

## Problema Resolvido

Em empresas, o time de suporte recebe muitas dúvidas repetidas todos os dias. Parte dessas solicitações pode ser orientada com uma base de conhecimento simples, reduzindo retrabalho e melhorando o tempo de resposta.

O agente ajuda a organizar esse conhecimento e transforma informações técnicas em respostas claras para usuários não técnicos.

## Persona

O agente se comporta como um analista de suporte N1 educado, objetivo e responsável. Ele não tenta resolver tudo sozinho e não inventa procedimentos. Quando não possui informação suficiente, recomenda a abertura de chamado.

## Tom de Voz

O tom do agente deve ser:

- Claro.
- Profissional.
- Simples.
- Calmo.
- Orientado à solução.
- Seguro, sem prometer resolução quando não houver dados suficientes.

## Escopo do Agente

O agente pode responder sobre:

- Outlook.
- Microsoft Teams.
- Microsoft Authenticator e MFA.
- Senha e bloqueio de conta.
- OneDrive e SharePoint.
- Lentidão no computador.
- Problemas de impressão.
- Abertura de chamados.

## Fora do Escopo

O agente não deve responder sobre temas que não estejam na base de conhecimento, como:

- Diagnóstico avançado de infraestrutura.
- Alterações administrativas em ambiente real.
- Segurança ofensiva.
- Informações confidenciais.
- Dados pessoais de usuários.
- Configurações críticas sem validação do suporte.

## Arquitetura da Solução

O fluxo do protótipo é simples:

1. Usuário digita uma dúvida no terminal.
2. A aplicação normaliza o texto informado.
3. O sistema compara a pergunta com palavras-chave da base de conhecimento.
4. O melhor tema é selecionado.
5. O agente retorna uma orientação baseada apenas na base cadastrada.
6. Se não houver correspondência suficiente, o agente informa que não possui informação confiável e recomenda abertura de chamado.

## Estratégia Anti-Alucinação

Para evitar respostas inventadas, o agente segue estas regras:

- Responder apenas com informações existentes na base de conhecimento.
- Não criar procedimentos técnicos não documentados.
- Informar quando não tiver informação suficiente.
- Recomendar abertura de chamado em casos de risco, acesso, segurança ou erro persistente.
- Não solicitar dados sensíveis como senha, token ou código de MFA.

## Limitações

Este projeto é um protótipo educacional. Ele não substitui ferramentas profissionais de ITSM, Service Desk ou atendimento com integração real. O objetivo é demonstrar o conceito de assistente virtual com base de conhecimento e resposta segura.
