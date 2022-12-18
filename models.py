import random
from exceptions import EnemyDown, GameOver
from settings import LIST_OF_VARIANTS, INITIAL_PLAYER_HEALTH, ATTACK_CH, DEFENSE_CH, \
    WARNING_MSG, SUCCESSFUL_ATTACK_MSG, SUCCESSFUL_DEFENCE_MSG, FAILED_ATTACK_MSG, FAILED_DEFENCE_MSG, DRAW_MSG


class Enemy:
    level = 0
    health = 0

    def __init__(self) -> None:
        """Enemy health points"""
        Enemy.level += 1
        Enemy.health += 1

    def decrease_health(self) -> None:
        """Decrease enemy health by 1 health point after successful attack"""
        self.health = self.health - 1
        if self.health < 1:
            raise EnemyDown("Enemy defeated")

    def select_attack(self):
        """Random selecting of the type of attack"""
        choosing_enemy_attack = LIST_OF_VARIANTS[random.randint(0, 2)]
        return choosing_enemy_attack

    def select_defence(self):
        """Random selecting of the type of defence"""
        choosing_enemy_defence = LIST_OF_VARIANTS[random.randint(0, 2)]
        return choosing_enemy_defence


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.player_health = INITIAL_PLAYER_HEALTH
        self.score = 0

    def decrease_health(self):
        """Decrease player health by 1 health point after successful attack"""
        self.player_health = self.player_health - 1
        if self.player_health < 1:
            raise GameOver("You are defeated!")

    def select_attack(self):
        """Selecting ot the type of attack by player"""
        try:
            choose_attack = LIST_OF_VARIANTS[int(input(ATTACK_CH)) - 1]
            return choose_attack
        except IndexError:
            print(WARNING_MSG)
            self.select_attack()

    def select_defence(self):
        """Selecting of the type of defence by player"""
        try:
            choose_defence = LIST_OF_VARIANTS[int(input(DEFENSE_CH)) - 1]
            return choose_defence
        except IndexError:
            print(WARNING_MSG)
            self.select_defence()

    def attack(self, other: Enemy):
        """The method correlate player and opponent choices when a player attacks"""
        player = self.select_attack()
        enemy = other.select_defence()
        if player == "ROBBER" and enemy == "WIZARD" or \
            player == "WIZARD" and enemy == "WARRIOR" or \
                player == "WARRIOR" and enemy == "ROBBER":
            self.score += 1
            other.decrease_health()
            print(SUCCESSFUL_ATTACK_MSG)
        elif player == enemy:
            print(DRAW_MSG)
        else:
            print(FAILED_ATTACK_MSG)

    def defence(self, other: Enemy):
        """The method correlate player and opponent choices when a player defends"""
        player = self.select_defence()
        enemy = other.select_attack()
        if player == "ROBBER" and enemy == "WIZARD" or\
            player == "WIZARD" and enemy == "WARRIOR" or\
                player == "WARRIOR" and enemy == "ROBBER":
            print(SUCCESSFUL_DEFENCE_MSG)
        elif player == enemy:
            print(DRAW_MSG)
        else:
            self.decrease_health()
            print(FAILED_DEFENCE_MSG)
            print(f"You how have {self.player_health} health points.")

