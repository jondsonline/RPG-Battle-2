import random

class Creature():
    def __init__(self, hp, ac, dam):
        self.max_hit_points = hp
        self.hit_points = hp
        self.armor_class = ac
        self.attack_damage = dam
        self.alive = True

    def take_damage(self, dam):
        self.hit_points -= dam
        if self.hit_points < 1:
            self.alive = False

    def attack_roll(self):
        roll = random.randint(1, 10)
        return roll

    def to_hit(self, target_ac):
        if self.attack_roll() >= target_ac:
            return True
        else:
            return False

    def damage_roll(self):
        roll = random.randint(1, self.attack_damage)
        return roll



class Player(Creature):
    def __init__(self, hp, ac, dam):
        super().__init__(hp, ac, dam)
        self.healing = 5
        self.level = 1

    def heal(self):
        heal_chance = random.randint(1, self.healing)

        if heal_chance == 1:
            print("The healing spell backfires! You take 1 point of damage!")
            self.take_damage(1)
        else:
            self.hit_points += heal_chance
            if self.hit_points > self.max_hit_points:
                self.hit_points = self.max_hit_points
            print("Your healing spell heals {} hit points.".format(heal_chance))

    def level_up(self):
        self.level += 1
        print("\nYou are now at level {}".format(self.level))

        increased_stat = random.randint(1, 10)

        if increased_stat >= 1 and increased_stat <= 5:
            hp_increase = random.randint(2, 5)
            self.max_hit_points += hp_increase
            self.hit_points = self.max_hit_points
            print("Your maximum hit points increases by {}!".format(hp_increase))
        elif increased_stat >= 6 and increased_stat <= 8:
            self.attack_damage += 1
            print("Your attack damage increases by 1!")
        elif increased_stat == 9:
            self.healing += 1
            print("Your healing skill increases by 1!")
        elif increased_stat == 10:
            if self.armor_class < 8:
                self.armor_class += 1
                print("Your armor class increases by 1!")
            else:
                self.max_hit_points += 6
                self.hit_points = self.max_hit_points
                print("Your maximum hit points increases by 6!")

class Monster(Creature):
    def __init__(self, hp, ac, dam):
        super().__init__(hp, ac, dam)
        self.level = 1

    def level_up(self):
        self.level += 1
        self.alive = True

        self.max_hit_points += random.randint(2, 4)
        self.hit_points = self.max_hit_points
        attack_increase_chance = random.randint(1, 2)
        if attack_increase_chance == 1:
            self.attack_damage += 1

