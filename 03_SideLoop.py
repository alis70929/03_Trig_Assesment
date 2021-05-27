# checks if flaot is greater than 0 and less than or equal to upper bound
def num_check(question, upper_bound=None):

    if upper_bound is not None:
        error = "please enter a number greater than 0 and lower than or equal to {}".format(upper_bound)
    else:
        error = "please enter any number greater than 0"

    valid = False
    while not valid:
        try:
            response = float(input(question))

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


side_list = []
valid = False
while not valid:
    Vertical = num_check("Vertical side length", None)
    Horizontal = num_check("Horizontal side length", None)
    Hypotenuse = num_check("Hypotenuse side length: ", None)
