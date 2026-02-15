from Models.training_camp_models import Recruta

squad = [Recruta("David", 10),
        Recruta("Bryan", 10),
        Recruta("Liam", 10),
        Recruta("Ben", 10),
        Recruta("Victor", 10)]

print("--- INÍCIO DO TREINAMENTO - 10KM ---")

for recruta in squad:
    recruta.run(10)
print("-" * 30) #Linha divisória visual

print("--- RELATÓRIO FINAL ---")
print(Recruta.contagem_tropas(), "")



