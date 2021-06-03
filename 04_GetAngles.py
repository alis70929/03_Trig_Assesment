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


def get_angles():
    angle_data = ["", ""]
    angle_data[0] = num_check("Angle A: ", 90)
    if angle_data[0] != "":
        return angle_data

    angle_data[1] = num_check("Angle B: ", 90)
    if angle_data[1] != "":
        return angle_data

    if angle_data[0] == "" and angle_data[1] == "":
        print("Please Enter 2 sides or 1 angle")
        return "Invalid Input"


# Main Routine
angles = "Invalid Input"
while angles == "Invalid Input":
    given_sides = int(input("Given Sides: "))

    if given_sides == 1:
        angles = get_angles()
    else: 
        angles = ["", ""]