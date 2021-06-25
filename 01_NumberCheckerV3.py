# checks if flaot is greater than/equal to 0.01 and less than upper bound, or just greater than given lower bound
def num_check(question, upper_bound=None, lower_bound=None):

    if upper_bound is not None:
        error = "please enter a number greater than 0.01 and lower than {}".format(upper_bound)
    elif lower_bound is not None:
        error = "please enter a number greater than {}".format(lower_bound)
    else:
        error = "please enter any number greater than or equal to 0.01"

    valid = False
    while not valid:
        try:
            response = input(question)

            if response == "xxx":
                return response
            elif response == "":
                return response

            response = float(response)
            if response < 0.01:
                print("your input is smaller than 0.01, consider converting to a smaller unit before trying again")
                continue

            if upper_bound is not None:
                if response < upper_bound:
                    return response

                else:
                    print(error)
                    continue
            elif lower_bound is not None:
                if response > lower_bound:
                    return response
                else:
                    print(error)
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
# for item in range(0, 4):
#   first_angle = num_check("First angle:", 90)
hypotenuse = num_check("Hypotenuse: ", None, 12)
