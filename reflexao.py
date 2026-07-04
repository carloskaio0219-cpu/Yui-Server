class Reflexao:

    def refletir(self, mensagem, memorias, emocao):

        reflexoes = []

        # A Yui verifica se já conhece esse assunto
        if memorias:
            reflexoes.append("Tenho lembranças relacionadas a isso.")
        else:
            reflexoes.append("Ainda não tenho lembranças sobre esse assunto.")

        # Analisa seu estado emocional
        reflexoes.append(f"Meu estado emocional atual é: {emocao}.")

        # Pensa no objetivo principal
        reflexoes.append("Minha missão é ajudar o mestre, aprender com ele e evoluir.")

        return reflexoes
