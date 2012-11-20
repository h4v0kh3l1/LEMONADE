# Initialize global variables
# Position is (Mine, player2, player3)
positions = []
lastRound = []
totalPoints = []
round = 0

# Helper functions
def norm(val):
    return val % 12;

# Read file
prev = open('previous.txt','r')
prevStr = prev.read()
dataStr = prevStr.splitlines()

for argStr in dataStr:
    args = argStr.split("\t");
    if (len(args) == 1):
        round = int(args[0].split(" ")[1])
    else:
        positions.append((int(args[0]),int(args[1]),int(args[2])))
        lastRound.append((int(args[3]),int(args[4]),int(args[5])))
        totalPoints.append((int(args[6]),int(args[7]),int(args[8])))

# Lood through history, and think



# If player is across, stay across
if (positions[round-1][0] == norm(positions[round-1][1]-6) or
    positions[round-1][0] == norm(positions[round-1][2]-6)):
    print positions[round-1][0]
    
# If other across,     

# If collision, hold ground

# If prolonged collision, sandwich

# If sandwiched, random jump

# If offer sandwich threat, shift away

# If offer sandwich, hold ground

# If players equilateral, hold ground

# If players are 

#TODO what are other player's strategies?