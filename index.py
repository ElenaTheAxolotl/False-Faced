# detective game heheheheheh

from title_and_game_start import title_screen

scene_count = 0

# Dictionary ig (Object JSON)

player = {
    "suspicion": 0,
    "inventory": []
}

def raise_suspicion(sus):
    player["suspicion"] = player["suspicion"] + sus

# to start the game mwahahahaha
title_screen()