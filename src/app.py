import json
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB_PATH = BASE_DIR / "data" / "base_conhecimento_suporte.json"


def normalizar_texto(texto: str) -> str:
    """Remove acentos e coloca o texto em minúsculas para facilitar a comparação."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(char for char in texto if unicodedata.category(char) != "Mn")
    return texto


def carregar_base_conhecimento() -> list:
    """Carrega a base de conhecimento em JSON."""
    with open(KB_PATH, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def calcular_pontuacao(pergunta: str, item: dict) -> int:
    """Calcula uma pontuação simples com base nas palavras-chave encontradas."""
    pergunta_normalizada = normalizar_texto(pergunta)
    pontuacao = 0

    for palavra in item.get("palavras_chave", []):
        palavra_normalizada = normalizar_texto(palavra)
        if palavra_normalizada in pergunta_normalizada:
            pontuacao += 1

    return pontuacao


def buscar_resposta(pergunta: str, base_conhecimento: list) -> dict | None:
    """Busca o tema mais provável na base de conhecimento."""
    melhor_item = None
    melhor_pontuacao = 0

    for item in base_conhecimento:
        pontuacao = calcular_pontuacao(pergunta, item)
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_item = item

    if melhor_pontuacao == 0:
        return None

    return melhor_item


def montar_resposta(item: dict | None) -> str:
    """Monta a resposta final do assistente."""
    if item is None:
        return (
            "Não encontrei informação suficiente na base de conhecimento para responder com segurança. "
            "Recomendo abrir um chamado ou consultar o time de suporte responsável."
        )

    perguntas_apoio = item.get("perguntas_apoio", [])
    perguntas_formatadas = "\n".join(f"- {pergunta}" for pergunta in perguntas_apoio[:3])

    return (
        f"Tema identificado: {item['tema']}\n\n"
        f"Orientação inicial:\n{item['resposta']}\n\n"
        f"Perguntas de apoio para o chamado:\n{perguntas_formatadas}\n\n"
        f"Quando escalar:\n{item['quando_escalar']}"
    )


def exibir_boas_vindas() -> None:
    print("=" * 72)
    print("HelpDesk AI Assistant")
    print("Assistente virtual de suporte técnico N1")
    print("Digite sua dúvida ou escreva 'sair' para encerrar.")
    print("=" * 72)


def main() -> None:
    base_conhecimento = carregar_base_conhecimento()
    exibir_boas_vindas()

    while True:
        pergunta = input("\nUsuário: ").strip()

        if pergunta.lower() in {"sair", "exit", "quit"}:
            print("\nAssistente: Atendimento encerrado. Obrigado!")
            break

        if not pergunta:
            print("\nAssistente: Por favor, descreva sua dúvida para que eu possa ajudar.")
            continue

        item = buscar_resposta(pergunta, base_conhecimento)
        resposta = montar_resposta(item)
        print(f"\nAssistente:\n{resposta}")


if __name__ == "__main__":
    main()
