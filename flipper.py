# Google Code Jam 
# flipper.py
# Created by Mauro J. Pappaterra on 29 of September 2017.


happy = 'x'
sad = 'o'

def pancakeFlipper(row, k):
    """Receives a row of pancakes as a string and a number of simultaneous flips k
    returns a string with the number of flips to have all pancakes smiley
    side up or a message if there is on solution
    e.g. '---+-++-' 3 => 3
    e.g. '+++++' 4 => 0
    e.g. '-+-+-' 4 => IMPOSSIBLE"""
    length = len (row)
    endList = length - k
    flips = 0;
    impossible = False

    stepByStep = " Start:  " + str(row)+ "\n"

    for index, x in enumerate (row):
        if ((x != happy) and (endList - index >= 0)):
            aux = 0

            while (aux < k): # flips k pancakes to the right
                row[index + aux] = flip(row[index + aux])
                aux +=1

            flips += 1

            stepByStep += "Flip " + str(flips) + ":  " + str(row)+ "\n"

        elif ((x != happy) and (endList - index < 0) and (endList > 1)): # negative index for out of bounds
            aux = 0

            while (aux < k):  # flips k pancakes to the left
                row[index - aux] = flip(row[index - aux])
                aux += 1

            flips += 1
            #FOR TESTING ONLY
            stepByStep += "Flip " + str(flips) + ":  " + str(row) + "\n"

        else:
            if (x != happy):
                impossible = True
                stepByStep = "There is no solution for this layout"

    for x in row:
        if (x != happy):
            impossible = True
            stepByStep = "There is no solution for this layout"

    if (not impossible):
        stepByStep = stepByStep.replace('[',' ')
        stepByStep = stepByStep.replace(']',' ')
        stepByStep = stepByStep.replace(',','')
        stepByStep = stepByStep.replace('\'','')
        #stepByStep = stepByStep.replace('\n','<br>')

        return (str(flips), stepByStep)
    else:
        return ("IMPOSSIBLE", stepByStep)


def flip (char):
    "Toggles + to - and - to +"
    if (char == sad):
        return happy
    elif (char == happy):
        return sad

#print (pancakeFlipper(['x','x','o','x','x','o','x','x','x'],3)[0])
#print (pancakeFlipper(['x','x','o','x','x','o','x','x','x'],3)[1])