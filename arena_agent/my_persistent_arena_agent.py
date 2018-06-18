from battleground.agent import Agent
from battleground.games.arena import util
import numpy as np
import random
from collections import defaultdict


class MyPersistentAgent(Agent):
    def __init__(self, **kwargs):
        self.state_dict = {}  # memory for saved states {state: index}
        self.num_states = 0  # number of currently saved states
        self.max_states = 500
        self.state_values = np.zeros(self.max_states)  # values for evaluation of states
        self.last_state_index = None
        self.action_dict = {}  # memory for saved actions {action: index}
        self.num_actions = 0  # number of currently saved actions
        self.max_actions = 20
        self.last_action_index = None
        # transition probabilities to go from state A via action B to state C
        self.transition_probs = np.zeros([self.max_states, self.max_actions, self.max_states])
        super().__init__(**kwargs)

    def get_state_index(self, state):
        """
        Get index of state in state_dict.
        :param state:
        :return:
        """
        positions = tuple([glad['pos'] for glad in state['gladiators']])
        if positions not in self.state_dict:
            self.num_states += 1
            self.state_dict[positions] = self.num_states
        return self.state_dict[positions]

    def get_state_values(self, states):
        for action, index in self.action_dict.items():
            pass

    def update_state_values(self, state, reward):
        pass

    def get_action_index(self, action):
        """
        Get index of action in action_dict. If action is not in action_dict, append new entry.
            {str(action): index}
        :param action: move dict
        :return: index of action in saved action memory
        """
        action_tuple = sorted(tuple(action.items()), key=lambda tup: tup[0])
        action_string = ""
        for key, value in action_tuple:
            action_string += str(key) + str(value)
        if action_string not in self.action_dict:
            self.num_actions += 1
            self.action_dict[action_string] = self.num_actions
        return self.action_dict[action_string]

    def get_state_transition_probs(self, state, action):
        """
        Gives probability distribution over known states in state_dict
        for the action of a given action onto a given state.
        :param state: given state
        :param action: given action
        :return: array of probabilities for known states
        """
        state_index_before = self.get_state_index(state)
        action_index = self.get_action_index(action)
        if state_index_before < self.max_states \
                and action_index < self.max_actions:
            return self.transition_probs[self.get_state_index(state),
                                         self.get_action_index(action)]
        else:
            return np.zeros(self.max_states)

    def update_transition_probs(self, state_index_before, action_index, state_index_after):
        """
        Increases transition probability of state -> action -> state by 1.
        :param state_index_before:
        :param action_index:
        :param state_index_after:
        :return:
        """
        if state_index_before < self.max_states \
                and action_index < self.max_actions \
                and state_index_after < self.max_states:
            self.transition_probs[state_index_before, action_index, state_index_after] += 1

    def decision_function(self, actions, values):
        pass

    def move(self, state):
        """
        This agent can also play the bunnies game and the basic games.
        :param state: state of the game
        :return: dict of chosen move
        """
        move = {}

        state_index = self.get_state_index(state)
        if self.last_action_index is not None and self.last_state_index is not None:
            self.update_transition_probs(self.last_state_index,
                                         self.last_action_index,
                                         state_index)

        # print(self.get_state_index(state))
        # print(self.state_dict)
        # print(self.action_dict)
        # print(self.transition_probs.sum())
        # x = int(np.random.choice([-1, 0, 1]))
        # y = int(np.random.choice([-1, 0, 1]))
        # move = {'target': (x, y), 'type': 'move'}

        if state is not None:
            if "move_options" in state:
                options = state["move_options"]
                options_list = util.move_options_to_list(options)
                move = random.choice(options_list)
            else:
                # default values
                move["type"] = "stay"
                move["value"] = 1
                print("Agent is taking default values.")

        self.last_action_index = self.get_action_index(move)
        self.last_state_index = self.get_state_index(state)

        return move

    def observe(self, state):
        memory = self.get_memory(default=None)
        # after initialization or if something made it forget:
        self.set_memory(memory)
