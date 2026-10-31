from .Nodes import Nodes, show_path
from .Map import Map
from .agents import BFS, DFS, UCS, GBFS, A_star


def main() -> None:
    print("Hello from ai!")

    start_city = "Chennai"
    goal_city = "Indore"  # heuristic_mapping only has entries for Indore as goal

    # (label, agent class, needs path cost, needs heuristic cost)
    algorithms = [
        ("BFS", BFS, False, False),
        ("DFS", DFS, False, False),
        ("UCS", UCS, True, False),
        ("GBFS", GBFS, False, True),
        ("A*", A_star, True, True),
    ]

    for label, agent_cls, needs_path, needs_heuristic in algorithms:
        start_node = Nodes(city=start_city)
        route_map = Map(
            start_node=start_node,
            goal=goal_city,
            path=needs_path,
            heuristic=needs_heuristic
        )
        agent = agent_cls(Map=route_map)
        goal_node = agent.explore()

        print(f"\n--- {label}: {start_city} -> {goal_city} ---")
        if goal_node == -1:
            print("No path found")
        else:
            path = show_path(goal_node)
            for city, costs in path:
                print(f"  {city}: {costs}")


if __name__ == "__main__":
    main()
