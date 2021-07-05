# Import Statements Here
import math
import pandas


# Functions Here
# checks if float is greater than 0.01 or lower bound, and less than upper bound
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
            # error for unit too small for sides
            if response < 0.01 and upper_bound is None:
                print("your input is smaller than 0.01, please convert to a smaller unit of distance before trying again")
                continue
            elif response < 0.01 and upper_bound is not None:
                print("Please round your angle up to at least 0.01")
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


# get triangle information from user returns triangle data in a list
# (Vertical,horizontal, hypotenuse, Angle A, Angle B)
# and how many sides are given
def get_triangle_data():
    # store triangle data
    triangle_data = ["", "", "", "", ""]

    valid = False
    while not valid:
        given_sides = 0
        sides_headings = ["Vertical", "Horizontal"]
        for item in range(0, len(sides_headings)):
            triangle_data[item] = num_check("{} side length: ".format(sides_headings[item]), None)
            if triangle_data[item] == "xxx":
                return "xxx"
            if triangle_data[item] != "":
                given_sides += 1

            if given_sides == 2:
                return [triangle_data, given_sides]

        if given_sides == 1:
            for item in range(0, len(sides_headings)):
                if triangle_data[item] != "":
                    triangle_data[2] = num_check("Hypotenuse side length: ", None, triangle_data[item])
                    if triangle_data[2] == "xxx":
                        return "xxx"
                    if triangle_data[2] != "":
                        given_sides += 1

                    if given_sides == 2:
                        return [triangle_data, given_sides]
        else:
            triangle_data[2] = num_check("Hypotenuse side length: ", None, None)
            if triangle_data[2] == "xxx":
                return "xxx"
            if triangle_data[2] != "":
                given_sides += 1

            if given_sides == 2:
                return [triangle_data, given_sides]

        if given_sides == 1:

            angles_heading = ["Angle A", "Angle B"]
            for item in range(0, len(angles_heading)):
                triangle_data[item + 3] = num_check("{}:".format(angles_heading[item]))
                if triangle_data[item + 3] == "xxx":
                    return "xxx"
                elif triangle_data[item + 3] != "":
                    return [triangle_data, given_sides]

            if triangle_data[0] == "" and triangle_data[1] == "":
                print("Please Enter 2 sides or 1 angle and a side")
                continue

        elif given_sides == 2:
            return [triangle_data, given_sides]
        else:
            print("please enter at least one side")


# Solve Triangle, Returns triangle data in list 
def triangle_solver(raw_triangle_data_var):
    given_sides = raw_triangle_data_var[1]
    triangle_data = raw_triangle_data_var[0]

    # making variables that are eaasier to understand for calculations
    Vertical = triangle_data[0]
    Horizontal = triangle_data[1]
    Hypotenuse = triangle_data[2]
    Angle_A = triangle_data[3]
    Angle_B = triangle_data[4]

    if given_sides == 2:
        if Vertical != "":
            if Horizontal != "":
                Hypotenuse = math.sqrt(math.pow(Horizontal, 2) + math.pow(Vertical, 2))
            elif Hypotenuse != "":
                Horizontal = math.sqrt(math.pow(Hypotenuse, 2) - math.pow(Vertical, 2))

        elif Horizontal != "" and Hypotenuse != "":
            Vertical = math.sqrt(math.pow(Hypotenuse, 2) - math.pow(Horizontal, 2))

        Angle_A = math.degrees(math.asin(Horizontal / Hypotenuse))
        Angle_B = math.degrees(math.asin(Vertical / Hypotenuse))

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

    # Putting it in a list to assign given tags
    temporary_triangle_data = [Vertical, Horizontal, Hypotenuse, Angle_A, Angle_B]
    for item in range(0, len(triangle_data)):
        if triangle_data[item] != "":
            triangle_data[item] = "{} (given)".format(temporary_triangle_data[item])
        else:
            triangle_data[item] = "{:.2f}".format(temporary_triangle_data[item])

    return triangle_data


# loops till response is yes or no
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return item
            elif response == item[0]:
                return item

        print("Please enter yes or no")


# Displays a right angle triangle with labelled sides
# (Horizontal, Vertical, Hypotenuse, AngleA, AngleB)
def display_triangle():
    triangle = "V |\ H \n" \
               "E |A\ Y \n" \
               "R |  \ P \n" \
               "T |   \ O \n" \
               "I |    \ T \n" \
               "C |     \ E \n" \
               "A |      \ N \n" \
               "L |       \ U \n" \
               "  |        \ S \n" \
               "  |________B\ E \n" \
               "  HORIZONTAL \n"
    print(triangle)


# Intro and introduction
def intro():
    print("**** Right Angle Triangle Solver ****")
    used_before = yes_no("Do you know how to use this program? (Y/N): ")
    if used_before == "no":
        
        display_triangle()
        print("Instructions - \n"
              " - Compare your right angle triangle to the triangle shown below\n"
              " - Figure out which sides of your triangle are Vertical, Horizontal, Hypotenuse \n"
              "   and figure out which angles are angleA and angleB\n "
              " - From there it will ask you for information you have must be greater than or equal to 0.01,\n"
              "   if your distances are less than 0.01 than change to a smaller unit of distance before trying again\n"
              "   if you don't know a side or angle just press <enter>\n"
              " - Enter 'xxx' at any point to get a summary of all your solved triangle data\n"
              "   Which will also be save to a csv file called triangle_data")
        input("\n Press <enter> when you have read the instructions")
    else:
        return


# Main Routine
# Setup Lists for dictionary
Verticals = []
Horizontals = []
Hypotenuses = []
Angle_As = []
Angle_Bs = []

# Dictionary for pandas data frame
triangle_data_dictionary = {
    "Vertical": Verticals,
    "Horizontal": Horizontals,
    "Hypotenuse": Hypotenuses,
    "Angle A": Angle_As,
    "Angle B": Angle_Bs
}

# Introduction and instructions
intro()
print()

# loop till exit code entered
loop_counter = 1
raw_triangle_data = ""
while raw_triangle_data != "xxx":
    # Heading
    print("**** Triangle {} ****".format(loop_counter))
    loop_counter += 1

    # Get known triangle data from users
    raw_triangle_data = get_triangle_data()
    # if exit code entered break out of loop
    if raw_triangle_data == "xxx":
        break
    # Solve rest of triangle
    refined_triangle_data = triangle_solver(raw_triangle_data)
    print()

    headings = ["Vertical", "Horizontal", "Hypotenuse", "Angle A", "Angle B"]
    for item in range(0, len(headings)):
        print("{}: {}".format(headings[item], refined_triangle_data[item]))
        triangle_data_dictionary[headings[item]].append(refined_triangle_data[item])
    print()

    # Ask user if they want to continue loop
    continue_loop = yes_no("Do you have another right angle triangle to solve (Y/N): ")
    print()

    if continue_loop == "no":
        break

# Set up data frame
triangle_data_frame = pandas.DataFrame(triangle_data_dictionary)
# set columns in the same way as asked for
triangle_data_frame = triangle_data_frame[["Vertical", "Horizontal", "Hypotenuse", "Angle A", "Angle B"]]

# if there is nothing in the triangle data lists then dont show empty data frame
if len(Verticals) != 0:
    print(triangle_data_frame)
    triangle_data_frame.to_csv("triangle_data.csv")
