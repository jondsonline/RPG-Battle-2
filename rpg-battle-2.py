# rpg-battle.py
#
# A simple game involving a rpg battle
# between the player and a monster.

from charclass import *

pc = Player(20, 6, 6)
monster = Monster(12, 6, 5)

def player_attacks():
    player_hits = pc.to_hit(monster.armor_class)

    if player_hits == True:
        damage = pc.damage_roll()

        print("You hit the monster for {} point(s) of damage.".format(damage))

        monster.take_damage(damage)
    else:
        print("You miss!")


def monster_attacks():
    monster_hits = monster.to_hit(pc.armor_class)

    if monster_hits == True:
        damage = monster.damage_roll()

        print("The monster hits you for {} point(s) of damage.".format(damage))

        pc.take_damage(damage)
    else:
        print("The monster misses!")


def pc_still_alive():
    if not pc.alive:
        print("You are killed!")
        return False
    else:
        return True


# THE GAME ROUTINE

game_continues = True

while game_continues:

    combat_continues = True
    combat_round = 0
    player_levels_up = True

    while combat_continues:
        combat_round += 1
        print("\nLevel {} - Round {}".format(pc.level, combat_round))
        print("-----------------------------------------------------")
        print("Player: HP = {}/{}, AC = {}, Damage = 1d{}, Heal = 1d{}".format(pc.hit_points, pc.max_hit_points,
                                                                  pc.armor_class, pc.attack_damage, pc.healing))
        print("Monster: HP = {}/{}, AC = {}, Damage = 1d{}".format(monster.hit_points, monster.max_hit_points,
                                                                   monster.armor_class, monster.attack_damage))
        print("-----------------------------------------------------")

        action = input("Do you want to (A)ttack, (H)eal, or (R)un? ").lower()

        print()

        if action == "a":  # attack
            player_attacks()

            if not monster.alive:
                print("You kill the monster!")
                combat_continues = False
            else:
                monster_attacks()
                combat_continues = pc_still_alive()

        elif action == "h":
            pc.heal()
            if not pc_still_alive():

                combat_continues = False
            else:
                monster_attacks()

            combat_continues = pc_still_alive()

        elif action == "r":
            print("You attempt to flee the battle!")
            monster_attacks()

            if pc_still_alive():
                print("You successfully escape and the battle is over!")

            player_levels_up = False
            combat_continues = False

        else:
            print("I don't recognize that command.")
            combat_round -= 1

    if not pc.alive:
        game_continues = False
    else:

        play_again = input("\nDo you want to play again (Y/N)? ")

        if play_again.upper() != "N":
            monster.level_up()
            pc.hit_points = pc.max_hit_points
            if player_levels_up:
                pc.level_up()
        else:
            print("Thanks for playing!")
            game_continues = False
