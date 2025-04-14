# main.py
import importlib.util
import os

# get the absolute path to the final game script
file_path = os.path.join("1-7_repeat_draw", "Jv5e.py")

# load the module dynamically
spec = importlib.util.spec_from_file_location("final_game", file_path)
final_game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(final_game)

# run the game
final_game.start_message()
final_game.play(final_game.hands, final_game.results)