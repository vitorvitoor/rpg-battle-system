class Soldado:
    def __init__(self, nome_inicial, municao_inicial):
        self.nome = nome_inicial      
        self.municao = municao_inicial

soldado_americano = Soldado("Chris Evans", ".38 SPL")

soldado_frances = Soldado("Jerry Cabannes", ".45 ACP")

print(vars(soldado_americano))
print(vars(soldado_frances))