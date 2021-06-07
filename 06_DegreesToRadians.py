import math


def angle_conversion(input, to_degrees_or_radians):

    if to_degrees_or_radians == "radians":
        radian = ((math.pi) / 180) * float(input)
        return radian

    if to_degrees_or_radians == "degrees":
        degrees = float(input) * (180 / math.pi)
        return degrees


# Main Routine
for item in range(0, 2):
    radians = angle_conversion(input("Degrees: "), "radians")
    print("Radians: {}".format(radians))

for item in range(0, 2):
    degrees = angle_conversion(input("Radians: "), "degrees")
    print("Degrees: {}".format(degrees))
