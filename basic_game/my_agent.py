from battleground.agent import Agent
import random


class MyAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move(self, state):
        move = random.randint(1, 100)
        # print("I move: {}".format(move))
        return {"value": move}
