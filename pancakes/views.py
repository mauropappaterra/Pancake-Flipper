from django.shortcuts import render
import flipper


# Create your views here.

def index (request):
    return render(request,'index.html')

def flip (request, string):

    row = ''
    k = ''

    for char in string:
        if (char.isalpha()):
            row += char
        else:
            k += char

    k = int(k)

    row = row.replace('x', '+')
    row = row.replace('o', '-')

    #FOR TESTING ONLY
    #print (row)
    #result = flipper.pancakeFlipper(['+','+','-','+','+','-','+','+','+'],3)[0]
    #stepByStep = flipper.pancakeFlipper(['+','+','-','+','+','-','+','+','+'],3)[1]
    result = flipper.pancakeFlipper(list(row),k)[0]
    stepByStep = flipper.pancakeFlipper(list(row),k)[1]

    context = {'row': row, 'k': k, 'result': result, 'stepByStep': stepByStep}

    return render(request, 'flip.html', context)