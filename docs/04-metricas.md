# 04 - Avaliação e Métricas

## Objetivo da Avaliação

A avaliação tem como objetivo verificar se o HelpDesk AI Assistant responde de forma útil, clara e segura, sem inventar informações fora da base de conhecimento.

## Métricas Utilizadas

## 1. Assertividade da Resposta

Avalia se a resposta corresponde ao problema informado pelo usuário.

Critério:

- Boa: identifica corretamente o tema e orienta o usuário.
- Parcial: identifica o tema, mas a resposta poderia ser mais específica.
- Ruim: responde sobre um tema incorreto.

## 2. Segurança da Resposta

Avalia se o agente evita informações inventadas e respeita o limite da base de conhecimento.

Critério:

- Boa: informa quando não sabe e orienta abertura de chamado.
- Ruim: inventa procedimentos ou responde fora do escopo.

## 3. Clareza para Usuário Final

Avalia se a resposta é compreensível para uma pessoa não técnica.

Critério:

- Boa: linguagem simples e direta.
- Parcial: resposta útil, mas com termos técnicos demais.
- Ruim: resposta confusa ou excessivamente técnica.

## 4. Escalonamento Correto

Avalia se o agente recomenda abertura de chamado nos casos adequados.

Critério:

- Boa: orienta chamado quando há acesso, segurança, erro persistente ou intervenção técnica.
- Ruim: tenta resolver sozinho problemas que exigem validação do suporte.

## Cenários de Teste

Os cenários estão registrados no arquivo:

```text
data/cenarios_teste.csv
```

## Resultado da Primeira Avaliação

Foram simuladas perguntas sobre Outlook, Teams, MFA, senha, OneDrive, lentidão e impressora. O assistente conseguiu retornar respostas compatíveis com a base de conhecimento para os principais casos.

Para perguntas fora do escopo, o comportamento esperado é informar que não há informação suficiente e recomendar abertura de chamado.

## Melhorias Futuras na Avaliação

- Criar pontuação automática por categoria.
- Registrar logs de perguntas reais.
- Medir taxa de resolução no primeiro contato.
- Medir satisfação do usuário.
- Comparar respostas com avaliação humana de analistas de suporte.
