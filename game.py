row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
won = False
cross = True
counter = 0

while not won:

    counter +=1
    print(str(row1)+"\n"+str(row2)+"\n"+str(row3))
    row, column = input()
    row, column = int(row), int(column) - 1

    if cross:
        if row == 1:
            row1[column] = 'x'
        elif row == 2:
            row2[column] = 'x'
        else:
            row3[column] = 'x'

    else:
        if row == 1:
            row1[column] = 'o'
        elif row == 2:
            row2[column] = 'o'
        else:
            row3[column] = 'o'

    cross = not cross

    if row1[0] == row1[1] == row1[2]:
        won = True
        winner = row1[0]
        print('running 36')

    if row2[0] == row2[1] == row2[2]:
        won = True
        winner = row2[0]
        print('running 41')

    if row3[0] == row3[1] == row3[2]:
        won = True
        winner = row3[0]
        print('running 46')

    for i in range(3):
        if row1[i-1] == row2[i-1] == row3[i-1]:
             won = True
             winner = row1[i-1]
             print('running 52')

    if row1[0] == row2[1] == row3[2]:
        won = True
        winner = row1[0]
        print('running 57')
        print

    elif row1[2] == row2[1] == row3[0]:
        won = True
        winner = row3[0]
        print('running 63')

    if counter == 9:
        won = True
        winner = 'tie'

    if winner == ' ':
        won = False

print(str(row1)+"\n"+str(row2)+"\n"+str(row3))
if winner != 'tie':
    print(winner, 'has won')
else:
    print('The match ended in a tie!')
