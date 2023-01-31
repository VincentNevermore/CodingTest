board = [["_" for _ in range(10)] for _ in range(10)]
board[0][0] = "*"
current_position = [0,0]
gameRunning = True
path = [[0,0]]


def printBoard():
    print(board)


def playerInput():
    inp = input("Please enter an action: ").lower()
    switch(inp)


def check(position):
    if position[0] < 0 or position[0] > 9 or position[1] <-9 or position[1] >0:
        print("Invalid move. Out of boundary")
        return False
    return True


def switch(action):
    global gameRunning
    global current_position
    global board
    global path
    temp = [0,0]
    if action == "u":
        temp[0] = current_position[0]
        temp[1] = current_position[1] + 1
        res = check(temp)
        if res:
            current_position = temp
            board[-current_position[1]][+current_position[0]] = "*"
            path.append(current_position)
    elif action == "d":
        temp[0] = current_position[0]
        temp[1] = current_position[1] - 1
        res = check(temp)
        if res:
            current_position = temp
            board[-current_position[1]][+current_position[0]] = "*"
            path.append(current_position)
    elif action == "l":
        temp[1] = current_position[1]
        temp[0] = current_position[0] - 1
        res = check(temp)
        if res:
            current_position = temp
            board[-current_position[1]][current_position[0]] = "*"
            path.append(current_position)
    elif action == "r":
        temp[1] = current_position[1]
        temp[0] = current_position[0] + 1
        res = check(temp)
        if res:
            current_position = temp
            board[-current_position[1]][current_position[0]] = "*"
            path.append(current_position)
    elif action == "p":
        print(path)
        printBoard()
    elif action == "e":
        gameRunning = False
    else:
        print("Unknown command")


while gameRunning:
    playerInput()


