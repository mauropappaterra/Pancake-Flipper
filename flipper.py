# Google Code Jam 
# flipper.py
# Created by Mauro J. Pappaterra on 29 of September 2017.


X = 'x'
O = 'o'

def pancakeFlipper(row, k):
    """Receives a row of pancakes as a string and a number of simultaneous flips k
    returns a string with the number of flips to have all pancakes smiley
    side up or a message if there is on solution and a string with a step by step solution
    e.g. '---+-++-' 3 => 3
    e.g. '+++++' 4 => 0
    e.g. '-+-+-' 4 => IMPOSSIBLE"""
    length = len (row)
    endList = length - k
    flips = 0;
    impossible = False

    stepByStep = " Start:  " + str(row)+ "\n"

    for index, pancake in enumerate (row):
        if ((pancake != X) and (endList - index >= 0)):
            aux = 0

            while (aux < k): # flips k pancakes to the right
                row[index + aux] = flip(row[index + aux])
                aux +=1

            flips += 1

            stepByStep += "Flip " + str(flips) + ":  " + str(row)+ "\n"

        elif ((pancake != X) and (endList - index < 0) and (endList > 1)): # negative index for out of bounds
            aux = 0

            while (aux < k):  # flips k pancakes to the left
                row[index - aux] = flip(row[index - aux])
                aux += 1

            flips += 1
            stepByStep += "Flip " + str(flips) + ":  " + str(row) + "\n"

        else:
            if (pancake != X):
                impossible = True
                stepByStep = "There is no solution for this layout"

    for pancake in row:
        if (pancake != X):
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
    if (char == O):
        return X
    elif (char == X):
        return O

# FOR TESTING ONLY
#print (pancakeFlipper(['x','x','o','x','x','o','x','x','x'],3)[0])
#print (pancakeFlipper(['x','x','o','x','x','o','x','x','x'],3)[1])