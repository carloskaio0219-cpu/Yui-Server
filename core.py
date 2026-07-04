from identidade import Identidade
from memoria import Memoria
from emocoes import Emocoes
from objetivos import Objetivos
from valores import Valores
from reflexao import Reflexao
from cerebro import Cerebro
from config import OPENROUTER_API_KEY


class Core:

    def __init__(self):

        self.identidade = Identidade()
        self.memoria = Memoria()
        self.emocoes = Emocoes()
        self.objetivos = Objetivos()
        self.valores = Valores()
        self.reflexao = Reflexao()
        self.cerebro = Cerebro(OPENROUTER_API_KEY)

    def conversar(self, mensagem):

        # Recupera memórias relacionadas (por enquanto vazio)
        memorias = []

        # Estado emocional atual
        emocao = "Calma"

        # Reflexão da Yui
        reflexoes = self.reflexao.refletir(
            mensagem,
            memorias,
            emocao
        )

        contexto = "\n".join(reflexoes)

        prompt = f"""
Mensagem do mestre:
{mensagem}

Reflexões internas:
{contexto}
"""

        resposta = self.cerebro.pensar(prompt)

        return resposta
