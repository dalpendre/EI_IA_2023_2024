
from abc import ABC, abstractmethod

from agents.state import State
from agents.action import Action


class Problem(ABC):

    def __init__(self, initial_state: State):
        self.initial_state = initial_state
        self.heuristic = None

    @abstractmethod
    def get_actions(self, state: State) -> list:
        pass

    @abstractmethod
    def get_successor(self, state: State, action: Action) -> State:
        pass

    @abstractmethod
    def is_goal(self, state: State) -> bool:
        pass

    def compute_path_cost(self, path: list) -> int:
        cost = 0
        for action in path:
            cost += action.cost
        return cost
