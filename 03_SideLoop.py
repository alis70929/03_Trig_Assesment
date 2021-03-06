# checks if flaot is greater than 0 and less than or equal to upper bound
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
def get_sides():
    side_list = []
    for item in range(0, 3):
        side_list.append("")

    valid = False
    while not valid:
        given_sides = 0

        side_list[0] = num_check("Vertical side length: ", None)
        if side_list[0] != "":
            given_sides += 1

        side_list[1] = num_check("Horizontal side length: ", None)
        if side_list[1] != "":
            given_sides += 1

        if given_sides == 2:
            return [side_list, given_sides]

        side_list[2] = num_check("Hypotenuse side length: ", None)

        if given_sides >= 1:
            return[side_list, given_sides]
        else:
            print("please enter at least one side")


for item in range(0, 4):
    sides_values = get_sides()
sides = sides_values[0]
given_sides_amount = sides_values[1]
