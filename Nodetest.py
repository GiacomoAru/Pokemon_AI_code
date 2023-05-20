from poke_env import *
from poke_env.player import *

gg = player = RandomPlayer(
        player_configuration=PlayerConfiguration("bot_username", "bot_password"),
        server_configuration=ShowdownServerConfiguration,
    )
