def printLine (text = ''):
    print('X {: ^47} X'.format(text))

def printSelTitle (text = '', title = None):
    print('X{: ^9}'.format(text), end = ""),

def printSelCheck (text = '', title = None):
    print('X   [ ]   '.format(text), end = "")

def printBorder (title = None):
    print('X' * 51)

def printBox (*lines, title = None, showBottomBorder = False):
    printBorder(title)
    printLine()
    for line in lines:
        printLine(line)
    printLine()
    if showBottomBorder:
        printBorder()

printBox('TASK MANAGER - TASK SELECTION')
printBox('READY TO START?', '-' * 21, "PRESS THE 'ENTER'",\
         'KEY TO BEGIN!', '-' * 21, showBottomBorder = True)
printSelTitle('TASK1'), printSelTitle('TASK2'),\
        printSelTitle('TASK3'), printSelTitle('TASK4'),\
        printSelTitle('TASK5'), print("X")
printSelCheck(), printSelCheck(), printSelCheck(),\
                 printSelCheck(), printSelCheck(), print("X")
printBorder() 