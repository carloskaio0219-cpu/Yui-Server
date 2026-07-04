from openai import OpenAI
from config import OPENROUTER_API_KEY, BASE_URL, MODELO
from personalidade import PERSONALIDADE


class Cerebro:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=BASE_URL
        )

    def pensar(self, mensagem):

        resposta = self.client.chat.completions.create(
            model=MODELO,
            messages=[
                {
                    "role": "system",
                    "content": PERSONALIDADE
                },
                {
                    "role": "user",
                    "content": mensagem
                }
            ]
        )

        return resposta.choices[0].message.content
