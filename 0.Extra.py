#importing libraries
import numpy as np
import heapq
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

#creating Dubai City grid
class DubaiCityGrid:
  # Define  spot type with symbol and color  and a mark
    SPOT_TYPES = {
        'landmark': {'symbol': 'L', 'color': 'red', 'marker': 's'},
        'beach': {'symbol': 'B', 'color': 'cyan', 'marker': '^'},
        'park': {'symbol': 'P', 'color': 'green', 'marker': 'p'},
        'museum': {'symbol': 'U', 'color': 'orange', 'marker': '*'},
        'hotel': {'symbol': 'H', 'color': 'blue', 'marker': 'D'},
        'empty': {'symbol': '.', 'color': 'lightgray', 'marker': '.'}
    }
    #initialize  of row 10  and collmn 10
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.grid = np.full((rows, cols), '.', dtype=str)
        self.tourist_spots = {}
        self.initialize_tourist_spots()
        self.tourist_spot_positions = list(self.tourist_spots.keys())
        self.num_spots = len(self.tourist_spot_positions)

    #initalize diffrent tourist spots  with type and position
    def initialize_tourist_spots(self):
        spots = [
            {"name": "Burj Khalifa", "type": "landmark", "description": "World's tallest building", "position": (4, 5)},
            {"name": "Dubai Frame", "type": "landmark", "description": "Iconic frame-shaped structure", "position": (3, 3)},
            {"name": "Palm Jumeirah", "type": "landmark", "description": "Artificial archipelago", "position": (5,8)},
            {"name": "Burj Al Arab", "type": "landmark", "description": "Iconic sail-shaped hotel", "position": (8, 2)},
            {"name": "JBR Beach", "type": "beach", "description": "Popular beach at Jumeirah Beach Residence", "position": (6, 6)},
            {"name": "Kite Beach", "type": "beach", "description": "Known for kitesurfing and water sports", "position": (4,1)},
            {"name": "Dubai Miracle Garden", "type": "park", "description": "Flower garden with over 50 million flowers", "position": (5, 4)},
            {"name": "Zabeel Park", "type": "park", "description": "Large urban park with many attractions", "position": (0, 4)},
            {"name": "Dubai Safari Park", "type": "park", "description": "Wildlife conservation facility", "position": (2, 7)},
            {"name": "Dubai Museum", "type": "museum", "description": "Located in the historic Al Fahidi Fort", "position": (6, 6)},
            {"name": "Museum of the Future", "type": "museum", "description": "Innovative museum showcasing future technologies", "position": (3, 5)},
            {"name": "Etihad Museum", "type": "museum", "description": "Documents the founding of the UAE", "position": (7, 4)},
            {"name": "Atlantis The Palm", "type": "hotel", "description": "Luxury resort on Palm Jumeirah", "position": (7, 0)},
            {"name": "Jumeirah Beach Hotel", "type": "hotel", "description": "Wave-shaped beachfront hotel", "position": (9, 1)},
        ]
        # Placement of spots on specific position
        for spot in spots:
            row, col = spot["position"]
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row, col] = self.SPOT_TYPES[spot["type"]]['symbol']
                self.tourist_spots[(row, col)] = {
                    "name": spot["name"],
                    "type": spot["type"],
                    "description": spot["description"]
                }

    def get_spot_info(self, row, col):
        return self.tourist_spots.get((row, col), None)

    # creating viual representation of graph
    def visualize_grid(self, path=None, title="Dubai Tourist Map (10x10 Grid)"):
        fig, ax = plt.subplots(figsize=(12, 10))
        # Draw grid lines
        for i in range(self.rows + 1):
            ax.axhline(i, color='gray', linestyle='-', alpha=0.3)
        for j in range(self.cols + 1):
            ax.axvline(j, color='gray', linestyle='-', alpha=0.3)
             # Plot each spot with their color and symbol
        legend_handles = []
        spot_types_plotted = set()

          # Add spots to the plot
        for (row, col), spot in self.tourist_spots.items():
            spot_type = spot['type']
            marker = self.SPOT_TYPES[spot_type]['marker']
            color = self.SPOT_TYPES[spot_type]['color']
            ax.scatter(col + 0.5, self.rows - row - 0.5, s=200, marker=marker,
                      color=color, edgecolor='black', linewidth=1, zorder=3)
            name = spot['name']
            ax.text(col + 0.5, self.rows - row - 0.8, name,
                   horizontalalignment='center', verticalalignment='top',
                   fontsize=7, weight='bold', wrap=True)
            if spot_type not in spot_types_plotted:
                patch = mpatches.Patch(color=color, label=spot_type.capitalize())
                legend_handles.append(patch)
                spot_types_plotted.add(spot_type)
        if path is not None:
            path_x = [p[1] + 0.5 for p in path]
            path_y = [self.rows - p[0] - 0.5 for p in path]
            ax.plot(path_x, path_y, color='purple', linewidth=2, marker='o', markersize=4, label='Path')
            legend_handles.append(mpatches.Patch(color='purple', label='Path'))
        ax.set_xlim(0, self.cols)
        ax.set_ylim(0, self.rows)
        ax.set_xticks(np.arange(0.5, self.cols, 1))
        ax.set_yticks(np.arange(0.5, self.rows, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_title(title, fontsize=16, weight='bold')
        ax.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1, 1))
        for i in range(self.rows):
            for j in range(self.cols):
                ax.text(j + 0.1, self.rows - i - 0.2, f"({i},{j})",
                       fontsize=6, alpha=0.5)
        plt.tight_layout()
        return fig, ax

    def save_map(self, filename="dubai_tourist_map.png"):
        fig, ax = self.visualize_grid()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"Map saved as {filename}")

    def show_map(self):
        fig, ax = self.visualize_grid()
        plt.show()

    def get_spot_list(self):
        spot_list = []
        spots_by_type = {}
        for pos, spot in self.tourist_spots.items():
            spot_type = spot["type"]
            if spot_type not in spots_by_type:
                spots_by_type[spot_type] = []
            spots_by_type[spot_type].append((pos, spot))
        for spot_type in sorted(spots_by_type.keys()):
            spot_list.append(f"\n{spot_type.upper()}S:")
            for pos, spot in spots_by_type[spot_type]:
                row, col = pos
                spot_list.append(f"  {spot['name']} at position ({row}, {col}): {spot['description']}")
        return "\n".join(spot_list)

    #implementing A* search
    def find_optimal_route_astar(self):
        start = (0, 0)
        initial_bitmask = 0
        if start in self.tourist_spots:
            index = self.tourist_spot_positions.index(start)
            initial_bitmask |= (1 << index)
        target_bitmask = (1 << self.num_spots) - 1
        heap = []
        initial_h = self._calculate_heuristic(start, initial_bitmask)
        heapq.heappush(heap, (initial_h, 0, start, initial_bitmask, [start]))
        visited = {}
        while heap:
            priority, cost, current_pos, bitmask, path = heapq.heappop(heap)
            if bitmask == target_bitmask:
                return path
            if (current_pos, bitmask) in visited and visited.get((current_pos, bitmask), float('inf')) <= cost:
                continue
            visited[(current_pos, bitmask)] = cost
            for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
                new_row = current_pos[0] + dx
                new_col = current_pos[1] + dy
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    new_pos = (new_row, new_col)
                    new_cost = cost + 1
                    new_bitmask = bitmask
                    if new_pos in self.tourist_spot_positions:
                        index = self.tourist_spot_positions.index(new_pos)
                        if not (new_bitmask & (1 << index)):
                            new_bitmask |= (1 << index)
                    new_h = self._calculate_heuristic(new_pos, new_bitmask)
                    new_priority = new_cost + new_h
                    if (new_pos, new_bitmask) not in visited or new_cost < visited.get((new_pos, new_bitmask), float('inf')):
                        new_path = path + [new_pos]
                        heapq.heappush(heap, (new_priority, new_cost, new_pos, new_bitmask, new_path))
        return None
  #implementaion of Uninformed Search DFS
    def find_optimal_route_dfs(self):
     start = (0, 0)
     initial_bitmask = 0
     if start in self.tourist_spots:
        index = self.tourist_spot_positions.index(start)
        initial_bitmask |= (1 << index)
     target_bitmask = (1 << self.num_spots) - 1
     stack = [(start, initial_bitmask, [start])]
     visited = set()
     visited.add((start, initial_bitmask))
     while stack:
        current_pos, bitmask, path = stack.pop()
        if bitmask == target_bitmask:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = current_pos[0] + dx
            new_col = current_pos[1] + dy
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                new_pos = (new_row, new_col)
                new_bitmask = bitmask
                if new_pos in self.tourist_spot_positions:
                    index = self.tourist_spot_positions.index(new_pos)
                    if not (new_bitmask & (1 << index)):
                        new_bitmask |= (1 << index)
                if (new_pos, new_bitmask) not in visited:
                    visited.add((new_pos, new_bitmask))
                    new_path = path + [new_pos]
                    stack.append((new_pos, new_bitmask, new_path))
     return None


    def _calculate_heuristic(self, current_pos, bitmask):
        max_distance = 0
        for i in range(self.num_spots):
            if not (bitmask & (1 << i)):
                spot_pos = self.tourist_spot_positions[i]
                distance = abs(current_pos[0] - spot_pos[0]) + abs(current_pos[1] - spot_pos[1])
                if distance > max_distance:
                    max_distance = distance
        return max_distance



if __name__ == "__main__":
    dubai = DubaiCityGrid(rows=10, cols=10)
    # dubai.show_map()
    # dubai.save_map()
    # print(dubai.get_spot_list())

    # Find routes using both sreach
    print("\nFinding optimal route using A* search ...")
    path_astar = dubai.find_optimal_route_astar()
    if path_astar:
        print("\nA* route found! Path coordinates:")
        print(path_astar)  # Print the entire path as a list of tuples
    else:
        print("\nNo A* route found.")

    print("\nFinding optimal route using DFS...")
    path_dfs = dubai.find_optimal_route_dfs()
    if path_dfs:
        print("\nBFS route found! Path coordinates:")
        print(path_dfs)  # Print the entire path as a list of tuples
    else:
        print("\nNo BFS route found.")

    # Visualize the paths
    if path_astar:
        print("\nA* route length:", len(path_astar))
        dubai.visualize_grid(path=path_astar, title="Dubai Tourist Map with A* Route")
        plt.show()
    if path_dfs:
        print("\nBFS route length:", len(path_dfs))
        dubai.visualize_grid(path=path_dfs, title="Dubai Tourist Map with BFS Route")
        plt.show()




