from datetime import datetime


class LivroDaVida:

    def __init__(self):
        self.eventos = []

    def registrar(self, titulo, descricao):

        evento = {
            "titulo": titulo,
            "descricao": descricao,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        self.eventos.append(evento)

    def mostrar(self):

        return self.eventos
