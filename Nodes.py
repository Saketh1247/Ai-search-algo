from __future__ import annotations


class Nodes:

    def __init__(
        self,
        city: str,
        parent: Nodes = None,
        current_cost: int = 0,
        heuristic_cost: int = 0,
        next_node: Nodes = None
    ):
        self.parent = parent
        self.city = city
        self.current_cost = current_cost
        self.heuristic_cost = heuristic_cost


def show_path(tail_node: Nodes):

    flow = []
    dummy = tail_node

    while dummy:

        flow.append([
            dummy.city,
            {
                'path_cost': dummy.current_cost,
                'heurisitc_cost': dummy.heuristic_cost
            }
        ])

        dummy = dummy.parent

    return flow[::-1]