#print random numbers between 1 and 10 for a user input number of times - github demo

import random

print "This program will print out as many random numbers between 1 and 10 as you want."
print "How many random numbers do you want?"
y = raw_input();
y = int(y)

count = 0

while( count <= y) :
    #x = random.random() * 10
    #print "Cast"
    #print int(x)
    randint = random.randint(0,10)
    print "RandInt"
    print randint
    count = count + 1