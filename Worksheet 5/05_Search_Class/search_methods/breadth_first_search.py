
from utils.node_queue import NodeQueue
from search_methods.graph_search import GraphSearch
from search_methods.node import Node
from agents.state import State


class BreadthFirstSearch(GraphSearch):

    def __init__(self):
        super().__init__()
        self._frontier = NodeQueue()

    # TODO
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        if successor not in self._explored and not self._frontier.__contains__(successor):
            self._frontier.append(Node(successor, parent))

    def __str__(self):
        return "Breadth first search"