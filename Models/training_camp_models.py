class Recruta:

    total_alistados = 0 

    def __init__(self, nome_recruta, stamina_total):
        self.nome = nome_recruta
        self.stamina = stamina_total

        Recruta.total_alistados += 1

    @classmethod #afeta todos os soldados pois age diretamente na classe
    def contagem_tropas(cls): 
        return f"Temos {cls.total_alistados} soldados no campo!"
    
    def __str__(self):
        return f"Recruta: {self.nome} | Energia: {self.stamina}/10"

    def run(self, total_distance):
        self.stamina = self.stamina - total_distance
        print(f"O {self.nome} correu! Stamina atual: {self.stamina}")

    def rest(self):
        self.stamina = self.stamina + 5
        print(f"O {self.nome} descansou! Stamina atual: {self.stamina}")
  