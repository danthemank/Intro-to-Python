# Define your own function
def my_function():
    print "Hello From My Function!"

# Accept arguments into your function
def my_function_with_args(username, greeting):
    print "Hello %s! I wish you %s."%(username, greeting)

# Return a value from your function
def sum_two_numbers(a, b):
    return a + b

# Call your function
my_function();

# Call your function and pass it arguments
my_function_with_args("Carl", "good day")

# Return a value from your function
print sum_two_numbers(10,40)

###################

# Recursive Function
# def rec_func(num) :
#     print num
#     if(num < 10) :
#         num += 1
#         rec_func(num) #Function calls itself
#
# # Call Function
# rec_func(0)