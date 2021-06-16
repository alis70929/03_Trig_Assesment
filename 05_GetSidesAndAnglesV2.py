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
        sides_headings = ["Vertical", "Horizontal", "Hypotenuse"]
        for item in range(0, len(sides_headings)):
            triangle_data[item] = num_check("{} side length: ".format(sides_headings[item]), None)
            if triangle_data[item] != "":
                given_sides += 1

            if given_sides == 2:
                return triangle_data

        if given_sides == 1:

            angles_heading = ["Angle A", "Angle B"]
            for item in range(0, len(angles_heading)):
                triangle_data[item + 3] = num_check("{}:".format(angles_heading[item]))
                if triangle_data[item + 3] != "":
                    return

            if triangle_data[0] == "" and triangle_data[1] == "":
                print("Please Enter 2 sides or 1 angle and a side")
                continue

        elif given_sides == 2:
            return triangle_data
        else:
            print("please enter at least one side")


# Main Routine
triangle_data = get_triangle_data()
