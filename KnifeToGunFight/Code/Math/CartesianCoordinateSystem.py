import enum

from Utilities.CollisionDetection import MoveDirection

## Identifies a quadrant in the cartesian coordinate system.
## \author  Jacob Pike
## \date    09/02/2018
class CartesianCoordinateSystemQuadrant(enum.Enum):
    ## 0 to 90 degrees.
    TopRightOrFirstQuadrant = 1
    ## 90 to 180 degrees.
    TopLeftOrSecondQuadrant = 2
    ## 180 to 270 degrees.
    BottomLeftOrThirdQuadrant = 3
    ## 270 to 360 degrees.
    BottomRightOrFourthQuadrant = 4

## The 2D cartesian coordinate system.  Useful for mathematical
## calculations using this familiar system.
## See https://en.wikipedia.org/wiki/Cartesian_coordinate_system.
## \author  Jacob Pike
## \date    09/02/2018
class CartesianCoordinateSystem(object):
    ## Normalizes an angle to be within a range of [0, 360].
    ## \param[in]   angle_in_degrees - The angle in degrees to normalize.
    ## \return  The angle normalized to a range of [0, 360] degrees.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def NormalizeAngle(angle_in_degrees):
        # NORMALIZE THE ANGLE TO A RANGE OF [0, 360].
        MAX_DEGREES_IN_CIRCLE = 360
        normalized_degrees = angle_in_degrees % MAX_DEGREES_IN_CIRCLE

        # The degrees may be negative.
        degrees_negative = (normalized_degrees < 0)
        if degrees_negative:
            # Wrap back around to a non-negative number of degrees.
            normalized_degrees += MAX_DEGREES_IN_CIRCLE

        return normalized_degrees

    ## Determines the quadrant containing the angle in degrees.
    ## \param[in]   angle_in_degrees - The angle in degrees.  Doesn't
    ##      have to be in the range of [0, 360] but will be normalized
    ##      internally to that range.
    ## \return  The CartesianCoordinateSystemQuadrant containing the specified
    ##      angle.  If the angle is on the boundary of a quadrant, the returned
    ##      quadrant may be arbitrary chosen between the two overlapping quadrants.
    ##      If an error occurs, None will be returned.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def GetQuadrant(angle_in_degrees):
        # NORMALIZE THE DEGREES.
        normalized_degrees = CartesianCoordinateSystem.NormalizeAngle(angle_in_degrees)

        # GET THE QUADRANT.
        in_first_quadrant = (0 <= normalized_degrees) and (normalized_degrees <= 90)
        in_second_quadrant = (90 <= normalized_degrees) and (normalized_degrees <= 180)
        in_third_quadrant = (180 <= normalized_degrees) and (normalized_degrees <= 270)
        in_fourth_quadrant = (270 <= normalized_degrees) and (normalized_degrees <= 360)
        if in_first_quadrant:
            return CartesianCoordinateSystemQuadrant.TopRightOrFirstQuadrant
        elif in_second_quadrant:
            return CartesianCoordinateSystemQuadrant.TopLeftOrSecondQuadrant
        elif in_third_quadrant:
            return CartesianCoordinateSystemQuadrant.BottomLeftOrThirdQuadrant
        elif in_fourth_quadrant:
            return CartesianCoordinateSystemQuadrant.BottomRightOrFourthQuadrant
        else:
            return None

    ## Approximates the cardinal direction for an angle in degrees.
    ## This is done by checking which direction the angle "mostly" faces.
    ## \param[in]   angle_in_degrees - The angle in degrees.  Doesn't
    ##      have to be in the range of [0, 360] but will be normalized
    ##      internally to that range.
    ## \return  The approximated cardinal direction (a MoveDirection enum).
    ##      If the angle may overlap with more than one cardinal direction,
    ##      the returned direction may be arbitrary chosen.
    ##      Will be None if an error occurs.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def ApproximateCardinalDirection(angle_in_degrees):
        # NORMALIZE THE DEGREES.
        normalized_degrees = CartesianCoordinateSystem.NormalizeAngle(angle_in_degrees)

        # APPROXIMATE THE CARDINAL DIRECTION.
        # This can be done by looking at the orientation and
        # approximating which of the 4 cardinal directions fit best
        # (reference a unit circle diagram).
        facing_up = (45 <= normalized_degrees) and (normalized_degrees <= 135)
        facing_down = (225 <= normalized_degrees) and (normalized_degrees <= 315)
        facing_left = (135 <= normalized_degrees) and (normalized_degrees <= 225)
        # Note that it's important for this "facing right" check to come last
        # because this is where the degrees of the circle wrap around, meaning
        # an "or" check is necessary.  Alternatively, we could complicate this
        # condition by adding in additional checks for around 360 or 0 degrees.
        facing_right = (315 <= normalized_degrees) or (normalized_degrees <= 45)
        if facing_up:
            return MoveDirection.Up
        elif facing_down:
            return MoveDirection.Down
        elif facing_left:
            return MoveDirection.Left
        elif facing_right:
            return MoveDirection.Right
        else:
            return None
    