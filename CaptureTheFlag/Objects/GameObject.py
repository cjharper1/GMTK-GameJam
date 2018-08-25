## Represents an object in the game world. All objects are currently assumed to be the same size.
## Objects are tracked by their top-left most pixel because the game window expects the position of the
## upper left most pixel as the starting location for where the object will be drawn.
## \author  CJ Harper
## \date    08/25/2018
class GameObject(object):
    ## The width of a a game object in pixels.
    WidthPixels = 32
    ## The height of a game object in pixels.
    HeightPixels = 32

    ## Constructor.
    ## \param[in]   initial_x_position - The initial X position of this object.
    ## \param[in]   initial_y_position - The initial Y position of this object.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, initial_x_position, initial_y_position):
        ## The current X position of this object.
        self.XPosition = initial_x_position
        ## The current Y position of this object.
        self.YPosition = initial_y_position

    ## Determines if a given x and y coordinate is within the boundary or touching the 
    ## boundary of this object (i.e. the check is inclusive in mathematical notation it would 
    ## be [a,b] rather than (a,b)). This can be used for collision detection.
    ## \param[in]   x_position - The X position of the coordinate to check.
    ## \param[in]   y_position - The Y position of the coordinate to check.
    ## \return  True if the coordinate is in the bounds of this object. False otherwise.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def InBounds(self, x_position, y_position):
        # DETERMINE THE BOUNDARY OF THIS OBJECT.
        max_x_boundary = self.XPosition + self.WidthPixels
        max_y_boundary = self.YPosition + self.HeightPixels

        # DETERMINE IF THE GIVEN POINT IS IN THE BOUNDS OF THIS OBJECT.
        x_coordinate_is_in_x_bounds = (self.XPosition <= x_position <= max_x_boundary)
        y_coordinate_is_in_y_bounds = (self.YPosition <= y_position <= max_y_boundary)
        point_is_in_bounds = (x_coordinate_is_in_x_bounds and y_coordinate_is_in_y_bounds)

        return point_is_in_bounds
