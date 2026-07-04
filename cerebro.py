from openai import OpenAI

class Cerebro:
    def __init__(self, api_key):
        self.cliente = OpenAI(api_key=api_key)

    def pensar(self, mensagem):
        resposta = self.cliente.chat.completions.create(
            model="qwen-plus",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é Yui, uma IA amigável, inteligente, leal ao seu criador "
                        "Kirito e sempre busca aprender e evoluir."
                    )
                },
                {
                    "role": "user",
                    "content": mensagem
                }
            ]
        )

        return resposta.choices[0].message.content
