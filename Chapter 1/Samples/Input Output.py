# input() takes input as a command which allows for python functions and math equations and could create a vulnerability

print "Remember to wrap your input in double quotes!"
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are " + str(age) + " years old, " + name + "!")

# raw_input takes input in as a string by default and you can cast a data type to it, then strip the new line
# iString = raw_input( "Type a string: " ).rstrip( '\n' )
# iInt = int( raw_input( "Type an int: " ).rstrip( '\n' ) )
# iFloat = float( raw_input( "Type a float: " ).rstrip( '\n' ) )
#
# print iString
# print iInt
# print iFloat