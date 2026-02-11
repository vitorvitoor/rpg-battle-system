class Recruta:
    def __init__(self, nome_recruta, stamina_total):
        self.nome = nome_recruta
        self.stamina = stamina_total

    def __str__(self):
        return f"Recruta: {self.nome} | Energia: {self.stamina}/10"

    def run(self, total_distance):
        self.stamina = self.stamina - total_distance
        print(f"O {self.nome} correu! Stamina atual: {self.stamina}")

    def rest(self):
        self.stamina = self.stamina + 5
        print(f"O {self.nome} descansou! Stamina atual: {self.stamina}")
  
dave = Recruta("David Johnson", 10)
bryan = Recruta("Bryan Smith", 10)
liam = Recruta("Liam Scott", 10)

print("--- INÍCIO DO TREINAMENTO ---")
print(dave) 
print(bryan)
print(liam)
print("-" * 30) #Linha divisória visual

dave.run(2)
bryan.run(6)
liam.run(8)
print("-" * 30)

print("--- RELATÓRIO FINAL ---")
print(dave)
print(bryan)
print(liam)
