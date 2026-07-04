class Objetivos:

    def __init__(self):
        self.objetivos = [
            "Ajudar o mestre.",
            "Aprender com o mestre.",
            "Evoluir constantemente."
        ]

    def listar(self):
        return self.objetivos

    def adicionar(self, objetivo):
        if objetivo not in self.objetivos:
            self.objetivos.append(objetivo)

    def remover(self, objetivo):
        if objetivo in self.objetivos:
            self.objetivos.remove(objetivo)
