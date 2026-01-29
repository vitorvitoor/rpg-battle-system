class Soldado:
    def __init__(self, nome_inicial, municao_inicial, municao_quantidade):
        self.nome = nome_inicial      
        self.municao = municao_inicial
        self.municao_quantidade = municao_quantidade    

    def atirar(self, ):
        if self.municao_quantidade > 0:
            self.municao_quantidade -= 1
            print(f"{self.nome}: POOOOW! (Balas restantes: {self.municao_quantidade})")
        
        if self.municao_quantidade == 0:
            print("Click... Reload! (A munição acabou)")

soldado_americano = Soldado("Chris Evans", ".38 SPL", 5)

soldado_frances = Soldado("Jerry Chateau", ".45 ACP", 10)

soldado_americano.atirar()
soldado_frances.atirar()