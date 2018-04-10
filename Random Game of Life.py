import numpy as np
import matplotlib.pyplot as plt
from random import randint
def main():

    
    
    rows = input("Please enter the number of rows: ")   # asks the user for number of rows

    try :
        rows = int(rows)         # checks for a valid input
    except ValueError:
        rows = validChoice(rows)


    columns = input("Please enter the number of columns: ")    # asks the user for number of columns

    try :
        columns = int(columns)      # checks for valid column input
    except ValueError:
        columns = validChoice(columns)

    print ("")


    board = (makeBoard(rows, columns))   # calls makeboard function and saves in board variable as list

    print ("Indexing starts at 0 ")

    print ("")


    for i in range(1, rows-1):
        for j in range(1, columns-1):
            board[i][j]=randint(0,1)
        
    # Asks for the number of iterations to run
    iterations = input("How many iterations should I run? ")
    try:
        iterations = int(iterations)  # Asks for a valid iterations input if needed.
    except ValueError:
        iterations = validChoice(iterations)

    print ("")

    print ("Starting Board: ")

    print ("")

    #printBoard(board) #Prints the starting board

    print ("")

    iteration = 0 # iteration starts at 1

    while iterations > 0 :      # Uses while loop to run through the iterations

        print ("Iteration", iteration, ":")

        print ("")

        iteration = iteration + 1 # adds iteration everytime
        
        iterations = iterations - 1  # subtracts 1 iteration each time the program runs through each iteration
        plt.figure(figsize=(9,9))
        plt.imshow(board, interpolation='nearest',cmap=plt.cm.binary)
        plt.show()

        board = nextIteration(board)  # runs board through iteration to see which cells will live and which will die

        board = fixBoard(board)  # corrects the board up to 0s and 1s     

        #printBoard(board)  # prints board

        print ("")
        
        
        
        
        
def sigmoid(s):
   return 1/(1+np.exp(-s))
# turns 2 into a 0 because those cells died
# turns 3 into a 1 because those cells became alive
# returns boad with just 0s and 1s
def fixBoard(board):

    for i in range(len(board)):   # Uses for loop to go through each list inside list

        for x in range(len(board[0])): # Uses for loop to go through each index inside the list

            if board[i][x] == 2:
                board[i][x] = 0
            if board[i][x] == 3:
                board[i][x] = 1
    return (board)

# This function runs the game through each iteration
# Converts cells that will become alive next round to 3
# Converts cells that will become dead next round to 2
# Only checks specific cells for for cells around the edge of the board
# Uses nested for loops to go through each index
# Uses nested if  statements to check which cells around it are alive
# Input board with 0s and 1s returns board with 0s 1s 2s and 3s
def nextIteration(board):
   A=0
   B=0
   C=0
   D=0
   E=0
   F=0
   G=0
   H=0
   I=0    
   
   
     
   Rows = len(board)
   cols = len(board[0])

   for x in range(Rows):

        for i in range(cols):

            A=0
            B=0
            C=0
            D=0
            E=0
            F=0
            G=0
            H=0
            I=0 

            if (x == 0) and (i == 0):
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    I=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1
                    

            if (x == 0) and (0 < i < (len(board[0])-1)):
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    I=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    D=1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    C=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (x == 0) and (i == (len(board[0])-1)):

                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    C=1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    D=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (0 < x < (len(board)-1)) and (i == 0):

                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    E=1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    G=1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    I=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (0 < x < (len(board)-1)) and (0 < i < (len(board[0])-1)):

                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    B=1
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    E=1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    G=1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    I=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    D=1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    C=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (0 < x < (len(board)-1)) and (i == (len(board[0])-1)):
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    E=1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    B=1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    C=1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    D=1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    F=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (x == (len(board)-1)) and (i == 0):

                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    E=1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    G=1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if ( x == (len(board)-1)) and ( i == (len(board[0])-1)):

                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                   E=1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    B=1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    C=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1

            if (x == (len(board)-1)) and (0 < i < (len(board[0])-1)):
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                   C=1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    B=1
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    E=1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    G=1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    H=1
                if (board[x][i] == 1) or (board[x][i] ==2):
                    A=1
                    
            weights = {
            'node_1': np.array([-0.9063053, 0.44659176, 0.44659758, 0.44629902, 0.44651622, 0.4465556, 0.4473008, 0.44592547, 0.44704]),
            'node_2': np.array([-11.69597, 2.7016246, 2.7015557, 2.7015069, 2.7015061, 2.7016337, 2.7015085, 2.701625, 2.701467]),
            'node_3': np.array([0.08057535, -0.5072613, -0.5080015, -0.5064938, -0.5069153, -0.5076292, -0.50714386, -0.506816, -0.50620925]),
    
            'node_4': np.array([-28.348368, 22.53932, 7.2918983]),
            'node_5': np.array([19.044556, -7.9657435, -26.220287]),
            'node_6': np.array([0.0765617, 8.050791, -3.2905123]),
    
            'output_node': np.array([21.631903, 18.647995, -29.761766])
            }

            input_data = np.array([A, B, C, D, E, F, G, H, I])

            node1input = (input_data * weights['node_1']).sum()
            node1output = sigmoid(node1input)
            

            node2input = (input_data * weights['node_2']).sum()
            node2output = sigmoid(node2input)

            node3input = (input_data * weights['node_3']).sum()
            node3output = sigmoid(node3input)

            hiddenLayer1outputs = np.array([node1output, node2output, node3output])

            node4input = (hiddenLayer1outputs * weights['node_4']).sum()
            node4output = sigmoid(node4input)

            node5input = (hiddenLayer1outputs * weights['node_5']).sum()
            node5output = sigmoid(node5input)

            node6input = (hiddenLayer1outputs * weights['node_6']).sum()
            node6output = sigmoid(node6input)

            hidden_layer_2_outputs = np.array([node4output, node5output, node6output])

            model_input = (hidden_layer_2_outputs * weights['output_node']).sum()
            model_output = sigmoid(model_input)


            if (board[x][i] == 1):
                    if (model_output<0.5):
                        board[x][i] = 2
                    if (model_output>0.5):
                        board[x][i] = 1
                        
            if (board[x][i] == 0):
                    if (model_output<0.5):
                        board[x][i] = 0
                    if (model_output>0.5):
                        board[x][i] = 3

   return (board)

# Asks the user for while cells they want to turn on
# Input board return Board
# Returns q if user doesn't want to turn on any more cells 
def move(board, rows, columns):

    #Asks for the row
    row = input("Please enter the row of a cell to turn on or q to exit: ")

    if row == "q" :
        return ("q")    # Checks for a valid choice of input by the user 
    else:
        try :
            row = int(row)
        except ValueError:
            row = validChoice(row)
        while row >= rows :
            row = validChoice(row)
    #Asks for the column
    col = input("Please enter a column for that cell: ")

    try :
        col = int(col)
    except ValueError:    # Checks for valid input
        col = validChoice(col)
    while col >= columns:
        col = validChoice(col)

    board[row][col] = 1

    return (board)

# Takes the board and prints it out to the user
# Leaves 0s and 0s and 1s to Xs
def printBoard(board):

    for i in range(len(board)): # uses for loop to go through each index

        for x in range(len(board[0])):

            if (board[i][x]) == 0:
                print (0, end="")
            elif (board[i][x]) == 1:
                print (1, end="")
        print ("")
        

# Makes the board by using append method and lists    
def makeBoard(rows, columns):

    list2 = []  # this is the main list
    column = columns

    while rows > 0:
        list1 = []   # this is each list that will be inside the list

        while column > 0:
            list1.append(0)
            column = column - 1

        list2.append(list1)
        rows = rows - 1
        column = columns

    return (list2)
# Checks for valid user Input
# If letters keeps asking until a number is input
def validChoice(number):

    number = input("Please enter a valid choice: ")
    try :
        number = int(number)
    except ValueError:
        number = validChoice(number)

    return (number)




main()

           

           
   