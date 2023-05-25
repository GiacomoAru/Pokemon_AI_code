from poke_env.player import *
import random

class RandomAttack(Player):
    def choose_move(self, battle):
        if battle.available_moves:
            best_move = random.choice(battle.available_moves)
            return self.create_order(best_move)
        return self.choose_random_move(battle)
    
class LowestBP(Player):
    def choose_move(self, battle):
        if battle.available_moves:
            best_move = min(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)
        return self.choose_random_move(battle)