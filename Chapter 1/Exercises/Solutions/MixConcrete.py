#This program will tell the user if the conditions are correct for concrete to settle

#functions
def checkTemp(currentTemp):
    #define constants
    theCeiling = 100
    theFloor = 32

    #Make decision
    if(currentTemp > theFloor and currentTemp < theCeiling):
        print "Begin mix"
    else:
        print "Don't mix"

def checkMix():
    #define constants
    percentWater = 40

    #Convert gallons to a percentage
    totalMixture = water + mixture
    thePercent = totalMixture / water

    #Make decision
    if(thePercent == percentWater):
        print "Mixture is good"

    else:
        print "Mixture is no good"

#start program
print "This program will tell the user if the conditions are correct for concrete to settle."

theTemp = raw_input("What is the current temperature?")
checkTemp(theTemp)

waterInput = raw_input("What is the number of gallons of water?")
mixInput = raw_input("What is the number of gallons of mixture?")

checkMix(waterInput, mixInput)