#formater is a formated string, when used with format().
# the {} are replaced with the arguments that are passed. 

    # what this code is doing: 
        # 1. Takes the string string
        # 2. Call its format function, which is similar to telling it to do a command line
            # command named format.
        # 3. Pass to format four arguments, which match up with four {}s in the string
        #    variable. This is like passing arguments to the command line format.
        # 4. The result of calling string is a new string that has the {}s replaced with the 
        #   four variables. This is what print is now printing out

string = '{} "\n" {} "\n" {} "\n" {}'

print(string.format(1, 2, 3, 4))
print(string.format("one", 'two', 'three', 'four'))
print(string.format(True, False, False, False))
print(string, string, string, string)
print(string.format(
    "somebody once told me",
    "that the world was going to roll me",
    "I aint the sharpest tool in the shed",
    "she was looking kind of dumb with her finger and her thumb in the shape of an L on her forhead"
))
