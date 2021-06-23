import math


# checks if flaot is greater than 0 and less than upper bound
def num_check(question, upper_bound=None):

    if upper_bound is not None:
        error = "please enter a number greater than 0 and lower than or equal to {}".format(upper_bound)
    else:
        error = "please enter any number greater than 0"

    valid = False
    while not valid:
        try:
            response = input(question)

            if response == "":
                return response

            response = float(response)

            if upper_bound is not None:
                if response > 0 and response < upper_bound:
                    return response
                else:
                    print(error)
                    continue
            else:
                if response > 0:
                    return response
                else:
                    print(error)
                    continue
        except ValueError:
            print(error)


# get side information from user, returns sides in a list (Vertical,horizontal hypotenuse) and how many sides are given
def get_triangle_data():
    # store triangle data
    triangle_data = ["", "", "", "", ""]

    valid = False
    while not valid:
        given_sides = 0
        sides_headings = ["Vertical", "Horizontal"]
        for item in range(0, len(sides_headings)):
            triangle_data[item] = num_check("{} side length: ".format(sides_headings[item]), None)
            if triangle_data[item] != "":
                given_sides += 1

            if given_sides == 2:
                return [triangle_data, given_sides]
        if triangle_data[0] != "":
            triangle_data[2] = num_check("Hypotenuse side length", None, triangle_data[0])
        elif triangle_data[1] != "":
            triangle_data[2] = num_check("Hypotenuse side length", None, triangle_data[1])

        if given_sides == 1:

            angles_heading = ["Angle A", "Angle B"]
            for item in range(0, len(angles_heading)):
                triangle_data[item + 3] = num_check("{}:".format(angles_heading[item]))
                if triangle_data[item + 3] != "":
                    return [triangle_data, given_sides]

            if triangle_data[0] == "" and triangle_data[1] == "":
                print("Please Enter 2 sides or 1 angle and a side")
                continue

        elif given_sides == 2:
            return [triangle_data, given_sides]
        else:
            print("please enter at least one side")


def triangle_solver(raw_triangle_data_var):
    given_sides = raw_triangle_data_var[1]
    triangle_data = raw_triangle_data_var[0]

    Vertical = triangle_data[0]
    Horizontal = triangle_data[1]
    Hypotenuse = triangle_data[2]
    Angle_A = triangle_data[3]
    Angle_B = triangle_data[4]

    if given_sides == 2:
        if Vertical != "":
            if Horizontal != "":
                Hypotenuse = math.sqrt(math.pow(Horizontal, 2) + math.pow(Vertical, 2))
                print("Hypotenuse: {:.2f}".format(Hypotenuse))

            elif Hypotenuse != "":
                Horizontal = math.sqrt(math.pow(Hypotenuse, 2) - math.pow(Vertical, 2))
                print("Horizontal: {:.2f}".format(Horizontal))

        elif Horizontal != "" and Hypotenuse != "":
            Vertical = math.sqrt(math.pow(Hypotenuse, 2) - math.pow(Horizontal, 2))
            print("Vertical: {:.2f}".format(Vertical))

        Angle_A = math.degrees(math.asin(Horizontal / Hypotenuse))
        print("Angle A: {:.2f}".format(Angle_A))
        Angle_B = math.degrees(math.asin(Vertical / Hypotenuse))
        print("Angle B: {:.2f}".format(Angle_B))

    elif given_sides == 1:
        if Angle_A != "":
            Angle_B = 90 - Angle_A
            Rad_Angle_A = math.radians(Angle_A)
            if Horizontal != "":
                Vertical = Horizontal / math.tan(Rad_Angle_A)
                Hypotenuse = Horizontal / math.sin(Rad_Angle_A)
            elif Vertical != "":
                Horizontal = Vertical * math.tan(Rad_Angle_A)
                Hypotenuse = Vertical / math.cos(Rad_Angle_A)
            elif Hypotenuse != "":
                Horizontal = Hypotenuse * math.cos(Rad_Angle_A)
                Vertical = Hypotenuse * math.sin(Rad_Angle_A)

        elif Angle_B != "":
            Angle_A = 90 - Angle_B
            Rad_Angle_B = math.radians(Angle_B)
            if Horizontal != "":
                Vertical = Horizontal * math.tan(Rad_Angle_B)
                Hypotenuse = Horizontal / math.cos(Rad_Angle_B)
            elif Vertical != "":
                Horizontal = Vertical / math.tan(Rad_Angle_B)
                Hypotenuse = Vertical / math.sin(Rad_Angle_B)
            elif Hypotenuse != "":
                Horizontal = Hypotenuse * math.sin(Rad_Angle_B)
                Vertical = Hypotenuse * math.cos(Rad_Angle_B)

    triangle_data[0] = Vertical
    triangle_data[1] = Horizontal
    triangle_data[2] = Hypotenuse
    triangle_data[3] = Angle_A
    triangle_data[4] = Angle_B

    return triangle_data


# Main Routine
for item in range(0, 3):
    raw_triangle_data = get_triangle_data()
    refined_triangle_data = triangle_solver(raw_triangle_data)
