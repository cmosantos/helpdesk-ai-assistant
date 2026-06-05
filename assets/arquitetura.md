# Arquitetura do Projeto

```mermaid
flowchart TD
    A[Usuário informa uma dúvida] --> B[Aplicação Python]
    B --> C[Normalização do texto]
    C --> D[Consulta à base de conhecimento JSON]
    D --> E{Tema encontrado?}
    E -->|Sim| F[Resposta orientada pela base]
    E -->|Não| G[Resposta segura sem inventar informação]
    F --> H[Usuário recebe orientação]
    G --> H
```

## Descrição

O projeto usa uma arquitetura simples para demonstrar o funcionamento de um assistente virtual baseado em conhecimento.

A aplicação recebe a pergunta, compara com palavras-chave cadastradas e retorna a melhor orientação disponível. Quando não encontra correspondência suficiente, o assistente evita alucinação e recomenda abertura de chamado.
