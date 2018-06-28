from battleground.agent import Agent
import random


class MyAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move(self, state):
        move = {}

        if state is not None:
            if "move_options" in state:
                options = state["move_options"]
                if "values" in options:
                    move["value"] = random.choice(options["values"])
            else:
                # default value
                move["value"] = random.randint(1, 100)
                print("Agent is taking default values.")

        return move
