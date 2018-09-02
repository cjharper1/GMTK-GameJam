import math

from Math.Vector2 import Vector2
from ThirdParty.astar import AStar

## Pathfinding class to determine the shortest path between two
## positions on the game map.
## Inherits from the third-party class AStar and implements required methods.
## \author  Tom Rogan
## \date    09/01/2018
class Pathing(AStar):
    def __init__(self, level_map):
        self.Map = level_map
        self.Destination = None

    ## Determines the shortest path between two positions on the game map.
    ## \param[in] start_grid_position - A grid position as a Vector2 of column and row index.
    ## \param[in] destination_grid_position - The destination as a Vector2 of column and row index.
    ## \return  A list of Vector2 objects tracing the shortest path, with the first element
    ##      being start_grid_position, or None if no path could be found.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def GetPath(self, start_grid_position, destination_grid_position):
        self.Destination = destination_grid_position
        return self.astar(start_grid_position, self.Destination)

    ## Determines the direct distance between two positions on the game map.
    ## \param[in] start_grid_position - A grid position as a Vector2 of column and row index.
    ## \param[in] destination_grid_position - The destination as a Vector2 of column and row index.
    ## \return  The distance between the grid positions.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def GetDirectDistanceBetweenGridPositions(self, start_grid_position, destination_grid_position):
        # Determine how many columns apart the two locations are.
        column_delta = (destination_grid_position.X - start_grid_position.X)

        # Determine how many rows apart the two locations are.
        row_delta = (destination_grid_position.Y - start_grid_position.Y)

        # Treat the start and destination as two corners of a triangle.
        # The direct distance between them is the hypotenuse of the triangle.
        #
        # start
        #     |\
        #     | \
        #     |  \
        #     |   \
        #     |    \
        #     |-----destination
        return math.hypot(column_delta, row_delta)

    ## For a given grid position, determines the list of neighboring grid positions
    ## that are reachable and not occupied by a game object.
    ## \param[in] grid_position - A grid position as a Vector2 of column and row index.
    ## \return  The list of neighbors as Vector2 objects.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def neighbors(self, grid_position):
        # Get the possible neighbors of the position.
        neighbors = [
            Vector2(grid_position.X, grid_position.Y - 1),
            Vector2(grid_position.X, grid_position.Y + 1),
            Vector2(grid_position.X - 1, grid_position.Y),
            Vector2(grid_position.X + 1, grid_position.Y)]
        accessible_neighbors = []
        for neighbor in neighbors:
            # Check whether this position is within map bounds and unoccupied.
            in_x_bounds = (0 <= neighbor.X < self.Map.MapWidth)
            in_y_bounds = (0 <= neighbor.Y < self.Map.MapHeight)
            unoccupied = (neighbor.X, neighbor.Y) not in self.Map.Map
            is_destination = (neighbor == self.Destination)
            if in_x_bounds and in_y_bounds and (unoccupied or is_destination):
                accessible_neighbors.append(neighbor)

        return accessible_neighbors

    ## Computes an estimated distance between a grid position and the goal.
    ## \param[in] start_grid_position - A grid position as a Vector2 of column and row index.
    ## \param[in] destination_grid_position - The destination as a Vector2 of column and row index.
    ## \return  The scalar distance to the goal.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def heuristic_cost_estimate(self, start_grid_position, destination_grid_position):
        return self.GetDirectDistanceBetweenGridPositions(start_grid_position, destination_grid_position)

    ## Computes the distance between two neighboring positions on the grid.
    ## \param[in] grid_position - A grid position as a Vector2 of column and row index.
    ## \param[in] neighbor_grid_position - Another grid position as a Vector2 of column and
    ##      row index. Guaranteed to belong to the list returned by neighbors(grid_position).
    ## \return  The scalar distance between the positions.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def distance_between(self, grid_position, neighbor_grid_position):
        # Two neighboring grid tiles are always directly adjacent.
        return 1
