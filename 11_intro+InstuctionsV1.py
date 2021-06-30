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


def intro():
    print("**** Right Angle Triangle Solver ****")
    used_before = yes_no("Do you know how to use this program? (Y/N)")
    if used_before == "yes":
        print("Instructions - \n"
              " - Compare your right angle triangle to the triangle shown below")
        display_triangle()
        print(" - Figure out which sides of your triangle are Vertical, Horizontal, Hypotenuse \n" 
              "   and figure out which angles are angleA and angleB\n "
              " - From there it will ask you for information you have,\n"
              "   if you don't know a side or angle just press <enter>\n"
              " - Enter 'xxx' at any point to get a summary of all your solved triangle data\n"
              "   Which will also be save to a csv file called triangle_data")
        input("Press <enter> when you are ready to continue")
    else:
        return


intro()