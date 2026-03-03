class Hero:

    total_heroes = 0 

    def __init__(self, hero_name, hp, combat_class, attack):
        self.name = hero_name
        self.hp = hp
        self.max_hp = hp
        self.combat_class = combat_class
        self.attack = attack

        Hero.total_heroes += 1
  
    def attack_enemy(self):
        return f"The hero {self.name} attacked causing X damage."
  
  