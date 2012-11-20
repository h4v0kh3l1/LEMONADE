# Initialize global variables
import random
# Position is (Mine, player2, player3)
positions = []
lastRound = []
totalPoints = []
round = 0

opp1_stab = -1
opp2_stab = -1

target = 0
nextPosition = 0;
# Helper functions
def norm(val):
    if val % 12 == 0:
        return 12
    return val % 12

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

# Look through history, and think
# Calculate stability of players (likelihood not to jump)
lastPos1 = 0
lastPos2 = 0
runLen1 = 0
runLen2 = 0
nom1 = 0
denom1 = 0
nom2 = 0
denom2 = 0
for (pp, opp1, opp2) in positions:
    if pp == 0:
        continue;
    if opp1 == lastPos1:
        runLen1 += 1
    else:
        if runLen1 == 1:
            denom1 += 1
        elif runLen1 == 2:
            nom1 += 1
            denom1 += 1
        elif runLen1 > 2:
            nom1 += (runLen1-1)*runLen1
            denom1 += (runLen1-1)*runLen1
        runLen1 = 1;
        lastPos1 = opp1
    if opp2 == lastPos2:
        runLen2 += 1
    else:
        if runLen2 == 1:
            denom2 += 1
        elif runLen2 == 2:
            nom2 += 1
            denom2 += 1
        elif runLen2 > 2:
            nom2 += (runLen2-1)*runLen2
            denom2 += (runLen2-1)*runLen2
        runLen2 = 1;
        lastPos2 = opp2
if runLen1 == 1:
    denom1 += 1
elif runLen1 == 2:
    nom1 += 1
    denom1 += 1
elif runLen1 > 2:
    nom1 += (runLen1-1)*runLen1
    denom1 += (runLen1-1)*runLen1

if runLen2 == 1:
    denom2 += 1
elif runLen2 == 2:
    nom2 += 1
    denom2 += 1
elif runLen2 > 2:
    nom2 += (runLen2-1)*runLen2
    denom2 += (runLen2-1)*runLen2

if denom1 == 0:
    opp1_stab = 0
else:
    opp1_stab = nom1/denom1
if denom2 == 0:
    opp2_stab = 0
else:
    opp2_stab = nom2/denom2
    
    
    
    

if (round == 0): 
    nextPosition = int(random.random()*12+1)
    print(nextPosition)
    exit()
    
# Target across of player w/ lower cumulative score.
(pp_score, opp1_score, opp2_score) = totalPoints[round]
(pp_pos, opp1_pos, opp2_pos) = positions[round]
if opp1_score == opp2_score:
    target = (random.random()<.5)
elif opp1_score < opp2_score:
    target = 1
else:
    target = 2

if target == 1:
    if random.random() < opp1_stab:
        # Stable, go after across
        nextPosition = norm(opp1_pos - 6)
    else:
        # Not stable, stay in place
        nextPosition = norm(pp_pos)
else:
    if random.random() < opp2_stab:
        nextPosition = norm(opp2_pos - 6)
    else:
        nextPosition = norm(pp_pos)
print nextPosition
