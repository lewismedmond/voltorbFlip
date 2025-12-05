from main import play_one_game
from agents.rl_agent import RLPlayer


GAME_SIZE = 5
rl_player = RLPlayer(5)  # initialise rl agent
for games_played in range(10):
    play_one_game(5, games_played, rl_player, True)