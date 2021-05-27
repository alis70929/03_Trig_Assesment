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


''' for item in range(0, 2):
    side_length = num_check("Side Length: ", None) '''
for item in range(0, 4):
    first_angle = num_check("First angle:", 90)
