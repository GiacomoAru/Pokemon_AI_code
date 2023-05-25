import asyncio
import tabulate

from poke_env.player import *
from poke_env.stats import *
from poke_env import player_configuration 

import MyUtils
import AIPlayers

async def main():
    # We create three random players
    
    '''
    agent = AIPlayers.RandomAttack(battle_format='gen9randombattle')
    print(agent._username)
    await agent.accept_challenges(None, 1)
    agent.reset_battles()'''
    
    
    
    players = [
        RandomPlayer(max_concurrent_battles=10),
        AIPlayers.RandomAttack(max_concurrent_battles=10),
        AIPlayers.LowestBP(max_concurrent_battles=10),
        SimpleHeuristicsPlayer(max_concurrent_battles=10),
        MaxBasePowerPlayer(max_concurrent_battles=10)
    ]
    
    cross_evaluation = await cross_evaluate(players, n_challenges=20)


    # Defines a header for displaying results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])
    print(table)

    # Displays results in a nicely formatted table.
    print(tabulate.tabulate(table))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())   
    #asyncio.run(main())