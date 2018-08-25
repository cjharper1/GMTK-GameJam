## Represents the goal the player is trying to get the flag into. This is represented by a
## quadrilateral section of the map. Thus, the boundaries of this object are defined as the corners 
## of the object. The user should take care when constructing this object to pass the corrdinates
## in the correct order. Otherwise, the collision detection for this goal may be incorrect.
## \author  CJ Harper
## \date    08/25/2018
class Goal(object):
    ## Constructor.
    ## \param[in]   top_left_corner_coordinate - A tuple representing the top-left corner of the goal.
    ## \param[in]   top_right_corner_coordinate - A tuple representing the top-right corner of the goal.
    ## \param[in]   bottom_left_corner_coordinate - A tuple representing the bottom-left corner of the goal.
    ## \param[in]   bottom_right_corner_coordinate - A tuple representing the bottom-right corner of the goal.
    ## \author  CJ Harper
    ## \date    08/25/2018
    def __init__(
        self, 
        top_left_corner_coordinate, 
        top_right_corner_coordinate, 
        bottom_left_corner_coordinate, 
        bottom_right_corner_coordinate):
        self.TopLeftCorner = top_left_corner_coordinate
        self.TopRightCorner = top_right_corner_coordinate
        self.BottomLeftCorner = bottom_left_corner_coordinate
        self.BottomRightCorner = bottom_right_corner_coordinate
    