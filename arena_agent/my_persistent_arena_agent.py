from battleground.agent import Agent
import random


class MyPersistentAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def move_options_to_list(move_options):
        """
        :param move_options: from get_move_options(gladiator_index)
        :return: list of move options, from which an agent can directly select
        """
        options_list = []
        option = []

        def to_dict(list_of_tuples):
            return {t[0]: t[1] for t in list_of_tuples}

        def options_culling(arg):
            if isinstance(arg, list):
                for element in arg:
                    options_culling(element)
                    del option[-1]
            elif isinstance(arg, dict):
                # the dict is unordered, but we first need to cull the description of the option
                # before nesting further. The dict has len == 2, so it's cheap.
                for k, v in arg.items():
                    if not isinstance(v, list):
                        option.append((k, v))
                for k, v in arg.items():
                    if isinstance(v, list):
                        if isinstance(v[0], dict):  # v is list of dicts
                            options_culling(v)
                        else:  # v is list of values
                            # they keys are strings, and for the last list of options they are given as
                            #   'values': [ ... ]
                            # removing the plural 's' gives the singular form which appears in the move dict
                            # ASSUMPTION: A KEY THAT ENDS ON 's' IS IN PLURAL FORM
                            if k[-1] is 's':
                                key = k[:-1]
                            else:
                                key = k
                            for value in v:
                                option.append((key, value))
                                options_list.append(to_dict(option))
                                del option[-1]
            else:  # will never be reached
                option.append(arg)
                options_list.append(to_dict(option))
                del option[-1]
            return None

        options_culling(move_options)
        return options_list

    def move(self, state):
        """
        This agent can also play the bunnies game and the basic games.
        :param state: state of the game
        :return: dict of chosen move
        """
        move = {}

        if state is not None:
            if "move_options" in state:
                options = state["move_options"]
                options_list = self.move_options_to_list(options)
                move = random.choice(options_list)
            else:
                # default values
                move["name"] = "stay"
                move["target"] = None
                move["value"] = 1
                print("Agent is taking default values.")

        return move

    def observe(self, state):
        memory = self.get_memory(default=None)
        # after initialization or if something made it forget:
        self.set_memory(memory)
