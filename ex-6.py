
# there are 10 different types of people. 
    #the value is an integer
types_of_people = 10

#formated string using the variable with an integer value
x = f"There are {types_of_people} types of people."

# 1/4 adding  a string to variable to add to a string
binary = "binary"

#2/4
do_not = "don't"

#formated string using the previous string vars
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}" 

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side" 

print(w + e)

