# Google Code Jam 
# flipper.py
# Created by Mauro J. Pappaterra on 29 of September 2017.

X = '+'
O = '-'

def pancakeFlipper(row, k):
    """Receives a row of pancakes as a string and a number of simultaneous flips k
    returns a tuple with a string with the number of flips to have all pancakes smiley
    side up or a message if there is no solution, and a string with a step by step solution
    e.g. '---+-++-' 3 => 3
    e.g. '+++++' 4 => 0
    e.g. '-+-+-' 4 => IMPOSSIBLE"""
    length = len (row)
    endList = length - k
    flips = 0;
    impossible = False

    stepByStep = " Start:   " + str(row)+ "\n"

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

        stepByStep = stepByStep.replace(X, '<img src= "../static/img/happy.png" alt="+" width="30px">')
        stepByStep = stepByStep.replace(O, '<img src= "../static/img/plain.png" alt="-" width="30px">')

        return (str(flips), stepByStep)
    else:
        return ("IMPOSSIBLE", stepByStep)


def flip (char):
    "Toggles X to O and O to X"
    if (char == O):
        return X
    elif (char == X):
        return O

# FOR TESTING ONLY
# print (pancakeFlipper(['+','+','-','+','+','-','+','+','+'],3)[0])
# print (pancakeFlipper(['+','+','-','+','+','-','+','+','+'],3)[1])