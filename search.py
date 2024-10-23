"""
Motion planning on a rectangular grid using A* search
"""

from random import random
from random import seed
from queue import PriorityQueue
from copy import deepcopy

def is_valid(position, grid):
  x, y = position
  if x < 0 or x >= num_rows:
    return False 
  if y < 0 or y >= num_cols:
    return False
  return grid[x][y] == 0


class State(object):

    def __init__(self, start_position, goal_position, start_grid):
        self.priority = 0
        self.position = start_position
        self.goal = goal_position
        self.grid = start_grid
        self.total_moves = 0

    #--- Fill in the rest of the class...
    def manhattan_distance(self):
      x1,y1 = self.position
      x2, y2 = self.goal
      return abs(x1 - x2) + abs(y1 - y2)
    

    def __lt__(self, other):
      return self.priority < other.priority

    def __eq__(self, other):
      if self.position == other.position:
        return True
      return False


def create_grid():

    # Start with a num_rows by num_cols grid of all zeros
    grid = [[0 for c in range(num_cols)] for r in range(num_rows)]

    # Put ones around the boundary
    grid[0] = [1 for c in range(num_cols)]
    grid[num_rows - 1] = [1 for c in range(num_cols)]

    for r in range(num_rows):
        grid[r][0] = 1
        grid[r][num_cols - 1] = 1

    # Sprinkle in obstacles randomly
    for r in range(1, num_rows - 1):
        for c in range(2, num_cols - 2):
            if random() < obstacle_prob:
                grid[r][c] = 1;

    # Make sure the goal and start spaces are clear
    grid[1][1] = 0
    grid[num_rows - 2][num_cols - 2] = 0

    return grid


def print_grid(grid):

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                print(' ', end='')
            else:
                print(grid[r][c], end='')
        print('')

    print('')

    return 


def main():
    """
    Use A* search to find a path from the upper left to the lower right
    of the puzzle grid
    """


    # Setup the randomized grid
    grid = create_grid()
    print_grid(grid)

    # Initialize the starting state and priority queue
    start_position = (1, 1)
    goal_position = (num_rows - 2, num_cols - 2)
    start_state = State(start_position, goal_position, grid)
    start_state.grid[1][1] = '*'

    # A* priority: implement the Manhattan distance in the State class
    priority = start_state.total_moves + start_state.manhattan_distance()

    queue = PriorityQueue()
    queue.put((0, start_state))

    visited = {}

    while not queue.empty():
        priority, state = queue.get()

        if state.position == state.goal:
            print("Found goal! :)")
            print_grid(state.grid)
            return

        # Only skip if we've found a better path to this position
        if state.position in visited and visited[state.position] <= state.total_moves:
            continue

        # Update the best cost to reach this position
        visited[state.position] = state.total_moves

        # Try each possible move
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (state.position[0] + d[0], state.position[1] + d[1])

            if not is_valid(new_position, grid):
                continue

            successor = State(new_position, state.goal, deepcopy(state.grid))
            successor.total_moves = state.total_moves + 1
            successor.grid[new_position[0]][new_position[1]] = '*'

            # Compute f = g + h for A*
            g_score = successor.total_moves  # Cost from start to current
            h_score = successor.manhattan_distance()  # Estimated cost to goal
            f_score = g_score + h_score

            queue.put((f_score, successor))

    print("No path found.")
  
  
    queue.put((priority, start_state))



if __name__ == '__main__':

    seed(0)

    #--- Easy mode

    # Global variables
    # Saves us the trouble of continually passing them as parameters 
    num_rows = 8
    num_cols = 16
    obstacle_prob = .20

    for trial in range(5):
        print('\n\n-----Easy trial ' + str(trial + 1) + '-----')
        main()

    #--- Uncomment the following sets of trials when you're ready

    #--- Hard mode
    num_rows = 15
    num_cols = 30
    obstacle_prob = .30

    for trial in range(5):
        print('\n\n-----Harder trial ' + str(trial + 1) + '-----')
        main()

    #--- INSANE mode
    num_rows = 20
    num_cols = 60
    obstacle_prob = .35

    for trial in range(5):
        print('\n\n-----INSANE trial ' + str(trial + 1) + '-----')
        main()
