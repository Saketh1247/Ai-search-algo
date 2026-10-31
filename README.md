# AI Search Algorithms

A Python library implementing classic graph-search algorithms over an Indian cities road map. Given a start city and a goal city, each algorithm finds a route through the graph while demonstrating different search strategies.

## Algorithms

| Algorithm | Class | Strategy | Optimal? |
|---|---|---|---|
| **Breadth-First Search** | `BFS` | FIFO queue — explores level by level | ✅ (unweighted) |
| **Depth-First Search** | `DFS` | LIFO stack — explores as deep as possible first | ❌ |
| **Uniform-Cost Search** | `UCS` | Priority queue by cumulative path cost | ✅ |
| **Greedy Best-First Search** | `GBFS` | Priority queue by heuristic (straight-line estimate) | ❌ |
| **A\*** | `A_star` | Priority queue by *f(n) = g(n) + h(n)* | ✅ (with admissible heuristic) |

## Project Structure

```
.
├── src/ai/
│   ├── __init__.py          # Package entry point & CLI demo
│   ├── Map.py               # Graph data, heuristic table, Map class
│   ├── Nodes.py             # Node representation & path reconstruction
│   ├── ModelTemplate.py     # Abstract base class for all agents
│   └── agents.py            # BFS, DFS, UCS, GBFS, A* implementations
├── test/
│   └── test_Map.py          # Tests for the Map class
├── pyproject.toml
└── README.md
```

## Requirements

- Python ≥ 3.14
- [uv](https://docs.astral.sh/uv/) (recommended package manager)

## Quick Start

```bash
# Install dependencies
uv sync

# Run the CLI demo (all algorithms: Chennai → Indore)
uv run ai
```

### Use as a Library

```python
from ai import Nodes, Map, BFS, UCS, A_star, show_path

start = Nodes(city="Chennai")
route_map = Map(start_node=start, goal="Indore", path=True, heuristic=True)

goal_node = A_star(Map=route_map).explore()

for city, costs in show_path(goal_node):
    print(f"{city}: {costs}")
```

## Running Tests

```bash
uv run python -m pytest test/
```

## How It Works

1. **Map** — wraps a weighted adjacency list of 22 Indian cities and an optional straight-line-distance heuristic table (currently defined for Indore as the goal).
2. **Nodes** — each node stores its city name, parent pointer, cumulative path cost, and heuristic cost.
3. **Agents** — each algorithm inherits from `ModelTemplate` and implements `explore()`, returning the goal `Node` (or `-1` if unreachable). Call `show_path()` on the result to reconstruct the route.

## License

This project is unlicensed. Feel free to use it for learning and experimentation.
