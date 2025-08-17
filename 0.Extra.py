#importing libraries
import numpy as np
import heapq
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
from itertools import combinations

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
        for i in range(self.rows + 1):
            ax.axhline(i, color='gray', linestyle='-', alpha=0.3)
        for j in range(self.cols + 1):
            ax.axvline(j, color='gray', linestyle='-', alpha=0.3)
        legend_handles = []
        spot_types_plotted = set()
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

# show map
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

    def dfs_shortest_path(self, start_pos, end_pos):
        if start_pos == end_pos:
            return [start_pos]
        queue = deque()
        queue.append( (start_pos, [start_pos]) )
        visited = set()
        visited.add(start_pos)
        while queue:
            current_pos, path = queue.popleft()
            for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
                new_row = current_pos[0] + dx
                new_col = current_pos[1] + dy
                new_pos = (new_row, new_col)
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    if new_pos == end_pos:
                        return path + [new_pos]
                    if new_pos not in visited:
                        visited.add(new_pos)
                        queue.append( (new_pos, path + [new_pos]) )
        return None

    def compute_distance_matrix(self):
        spots = [(0, 0)] + self.tourist_spot_positions
        n = len(spots)
        distance_matrix = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                if i == j:
                    distance_matrix[i][j] = 0
                else:
                    path = self.dfs_shortest_path(spots[i], spots[j])
                    distance_matrix[i][j] = len(path) - 1 if path else 0
        return distance_matrix, spots

   # # Tour iternatiary
    def solve_tsp(self):
        distance_matrix, spots = self.compute_distance_matrix()
        n = len(spots) - 1  # number of tourist spots (excluding start)
        if n == 0:
            return []

        dp = {}
        dp[(0, 0)] = 0  # (current_node, mask) -> cost

        for mask_size in range(0, n + 1):
            for subset in combinations(range(1, n + 1), mask_size):
                mask = 0
                for bit in subset:
                    mask |= 1 << (bit - 1)
                for current_node in range(0, n + 1):
                    if (current_node, mask) not in dp:
                        continue
                    current_cost = dp[(current_node, mask)]
                    for next_spot in range(1, n + 1):
                        if not (mask & (1 << (next_spot - 1))):
                            new_mask = mask | (1 << (next_spot - 1))
                            new_cost = current_cost + distance_matrix[current_node][next_spot]
                            if (next_spot, new_mask) not in dp or new_cost < dp[(next_spot, new_mask)]:
                                dp[(next_spot, new_mask)] = new_cost

        full_mask = (1 << n) - 1
        min_cost = float('inf')
        best_end = -1
        for end in range(1, n + 1):
            if (end, full_mask) in dp and dp[(end, full_mask)] < min_cost:
                min_cost = dp[(end, full_mask)]
                best_end = end

        if best_end == -1:
            return None

        path = []
        current_node = best_end
        current_mask = full_mask
        path.append(current_node)

        for _ in range(n):
            prev_mask = current_mask ^ (1 << (current_node - 1))
            min_prev_cost = float('inf')
            prev_node = -1
            for possible_prev in range(0, n + 1):
                if possible_prev == 0 and prev_mask != 0:
                    continue
                if (possible_prev, prev_mask) in dp:
                    cost = dp[(possible_prev, prev_mask)] + distance_matrix[possible_prev][current_node]
                    if cost < min_prev_cost:
                        min_prev_cost = cost
                        prev_node = possible_prev
            if prev_node == -1:
                break
            path.append(prev_node)
            current_node = prev_node
            current_mask = prev_mask

        path = path[::-1]
        order = [0] + path

        full_path = []
        for i in range(len(order) - 1):
            from_spot = spots[order[i]]
            to_spot = spots[order[i + 1]]
            segment = self.dfs_shortest_path(from_spot, to_spot)
            if i == 0:
                full_path.extend(segment)
            else:
                full_path.extend(segment[1:])
        return full_path

if __name__ == "__main__":
    dubai = DubaiCityGrid(rows=10, cols=10)
    # dubai.show_map()
    # dubai.save_map()
    # print(dubai.get_spot_list())

    print("\nFinding optimal route using TSP...")
    path_tsp = dubai.solve_tsp()
    if path_tsp:
        print("\nTSP route length:", len(path_tsp))
        dubai.visualize_grid(path=path_tsp, title="Dubai Tourist Map with Optimal TSP Route")
        plt.show()
    else:
        print("\nNo TSP route found.")