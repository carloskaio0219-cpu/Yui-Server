from core import Core

print("=" * 40)
print("YUI v1.0")
print("=" * 40)
print("Olá, mestre. Fico feliz em falar com você mais uma vez.")
print("Digite 'sair' para encerrar.\n")

yui = Core()

while True:
    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        print("\nYui: Até logo, mestre. Foi um prazer conversar com você.")
        break

    try:
        resposta = yui.conversar(mensagem)
        print(f"\nYui: {resposta}\n")

    except Exception as erro:
        print("\nOcorreu um erro:")
        print(erro)
    
