import math


def angle_conversion(input, to_degrees_or_radians):

    if to_degrees_or_radians == "radians":
        radian = input * ((math.pi) / 180)
        return radian

    if to_degrees_or_radians == "degrees":
        degrees = input * 180 / math.pi
        return degrees

# Main Routine
