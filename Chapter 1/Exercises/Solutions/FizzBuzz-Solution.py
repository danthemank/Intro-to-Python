# FizzBuzz game exersize
# The game rules are as follows:
# 1. Count from 1 to 100
# 2. Every number evenly divisable by 3 is "Fizz"
# 3. Every number evently divisable by 5 is "Buzz"
# 4. Every number evenly dibisable by 3 and by 5 is "FizzBuzz"

BottomRange = 1
TopRange = 100

while(BottomRange < TopRange):
    if(BottomRange % 3 == 0 and BottomRange % 5 == 0):
        print "FizzBuzz"
    elif(BottomRange % 3 == 0):
        print "Fizz"
    elif(BottomRange % 5 == 0):
        print "Buzz"
    else:
        print BottomRange
    BottomRange += 1