
from agents.heuristic import Heuristic
from eightpuzzle.eight_puzzle_state import EightPuzzleState


class HeuristicTilesOutOfPlace(Heuristic):

    def __init__(self):
        super().__init__()

    # TODO
    def compute(self, state: EightPuzzleState) -> float:
        h = 0
        for i in range(state.row):
            for j in range(state.columns):
                if state.matrix[i][j] != 0 and state.matrix[i][j] != self._problem.goal_state.matrix[i][j]:
                    h += 1

        return h

    def __str__(self):
        return "Tiles out of place"
