from commands import *

class Player:
    def __init__(self, sta, itm, num):
        self.stats = {
            "CURRENT_HP": sta[0],
            "MAXIMUM_HP": sta[1],
            "ATTACK_DAMAGE": sta[2],
            "ATTACK_BONUS": sta[3],
            "DEFENCE": sta[4],
            "CURRENT_MP": sta[5],
            "MAXIMUM_MP": sta[6],
            "MP_REFRESH": sta[7],
            "SPEED": sta[8],
            "ITEM_USES": sta[9]
        }
        self.items = {
            "Spoons": itm[0],
            "Knives": itm[1],
            "Potions": itm[2],
            "Fences": itm[3],
            "Gun": itm[4]
        }

        self.effects = effectList(0,0,0,0,0)
        self.id = num
        self.alive = True
        self.fence_set = False
    def damage(self, amount):
        self.stats["CURRENT_HP"] -= amount
        self.alive = self.stats["CURRENT_HP"] <= 0
    def heal(self, amount):
        self.stats["CURRENT_HP"] += amount
        if self.stats["CURRENT_HP"] > self.stats["MAXIMUM_HP"]:
            self.stats["CURRENT_HP"] = self.stats["MAXIMUM_HP"]
    def next_turn(self):
        if self.effects.adtr > 0:
            self.effects.adtr -= 1
            if self.effects.adtr == 0:
                self.effects.adv = 0
        self.stats["CURRENT_MP"] += self.stats["MP_REFRESH"]
        if self.stats["CURRENT_MP"] > self.stats["MAXIMUM_MP"]:
            self.stats["CURRENT_MP"] = self.stats["MAXIMUM_MP"]