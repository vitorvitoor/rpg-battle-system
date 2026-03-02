class Hero:

    total_heroes = 0 

    def __init__(self, hero_name, hp, combat_class, attack):
        self.name = hero_name
        self.hp = hp
        self.max_hp = hp
        self.combat_class = combat_class
        self.attack = attack

        Hero.total_heroes += 1

    @classmethod #affect all the heroes because is acting directly on the class
    def troops_count(cls): 
        return f"We have {cls.total_heroes} heroes on the field!"
    
    def __str__(self):
        return f"[{self.combat_class}] {self.name} | Energy: {self.hp}/{self.max_hp}"

    def run(self, total_distance):
        if total_distance > self.hp:
            print(f"{self.name} tryed to run {total_distance}km but passed away of exausthion...")
            self.hp = 0
        else:
            self.hp -= total_distance
            print(f"{self.name} runned! current hp: {self.hp}")

    def rest(self):
        self.hp += 5
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print(f"{self.name} have rested! Actual stamina: {self.hp}")

    def attack_enemy(self):
        return f"The hero {self.name} attacked causing X damage."
  
  