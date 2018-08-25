## Represents an object in the game world. All objects are currently assumed to be the same size.
## \author  CJ Harper
## \date    08/25/2018
class GameObject(object):
    ## The width of a a game object in pixels.
    WidthPixels = 32
    ## The height of a game object in pixels.
    HeightPixels = 32

    ## Constructor.
    ## \param[in]   initial_top_left_x_position - The initial top-left corner X position of this object.
    ## \param[in]   initial_top_left_y_position - The initial top-left corner Y position of this object.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(self, initial_top_left_x_position, initial_top_left_y_position):
        ## The top-left corner of the object.
        self.TopLeftCornerPosition = (initial_top_left_x_position, initial_top_left_y_position)
        ## The top-right corner of the object.
        self.TopRightCornerPosition = (initial_top_left_x_position + self.WidthPixels, initial_top_left_y_position)
        ## The bottom-left corner of the object.
        self.BottomLeftCornerPosition = (initial_top_left_x_position, initial_top_left_y_position + self.HeightPixels)
        ## The bottom-right corner of the object.
        self.BottomRightCornerPosition = (initial_top_left_x_position + self.WidthPixels, initial_top_left_y_position + self.HeightPixels)

    ## Moves the object by a set amount of pixels in each direction.
    ## \param[in]   x_movement_in_pixels - The amount of pixels to move the object in the x direction.
    ##      Negative values move left.
    ## \param[in]   y_movement_in_pixels - The amount of pixels to move the object in the y direction.
    ##      Negative values move up.
    def Move(self, x_movement_in_pixels, y_movement_in_pixels):
        coordinate_change = (x_movement_in_pixels, y_movement_in_pixels)
        self.TopLeftCornerPosition = tuple(sum(x) for x in zip(self.TopLeftCornerPosition, coordinate_change))
        self.TopRightCornerPosition = tuple(sum(x) for x in zip(self.TopRightCornerPosition, coordinate_change))
        self.BottomLeftCornerPosition = tuple(sum(x) for x in zip(self.BottomLeftCornerPosition, coordinate_change))
        self.BottomRightCornerPosition = tuple(sum(x) for x in zip(self.BottomRightCornerPosition, coordinate_change))

    ## Determines if a given x and y coordinate is within the boundary or touching the 
    ## boundary of this object (i.e. the check is inclusive in mathematical notation it would 
    ## be [a,b] rather than (a,b)). This can be used for collision detection.
    ## \param[in]   x_position - The X position of the coordinate to check.
    ## \param[in]   y_position - The Y position of the coordinate to check.
    ## \return  True if the coordinate is in the bounds of this object. False otherwise.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def InBounds(self, x_position, y_position):
        # DETERMINE IF THE GIVEN POINT IS IN THE BOUNDS OF THIS OBJECT.
        min_x_bound, min_y_bound = self.TopLeftCornerPosition
        max_x_bound, max_y_bound = self.BottomRightCornerPosition
        x_coordinate_is_in_x_bounds = (min_x_bound <= x_position <= max_x_bound)
        y_coordinate_is_in_y_bounds = (min_y_bound <= y_position <= max_y_bound)
        point_is_in_bounds = (x_coordinate_is_in_x_bounds and y_coordinate_is_in_y_bounds)

        return point_is_in_bounds
