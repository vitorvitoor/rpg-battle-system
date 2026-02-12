from Models.training_camp_models import Recruta

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
print(Recruta.contagem_tropas())
