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
                if response > 0 and response <= upper_bound:
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


# side_length = num_check("Side Length: ", None)
first_angle = num_check("First angle:", 89.9)
for item in range(0, 3):
    second_angle = num_check("Second Angle: ", 90 - first_angle)
