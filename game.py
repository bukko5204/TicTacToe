row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
won = False
cross = True
while not won:
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
    if row1[0] == row1[1] and row1[2] and not ' ':
        won = True
        winner = row1[0]
        print('bug 28')
    elif row2[0] == row2[1] and row2[2] and not ' ':
        won = True
        winner = row2[0]
        print('bug 32')
    elif row3[0] == row3[1] and row3[2] and not ' ':
        won = True
        winner = row3[0]
        print('bug 36')
    for i in range(3):
        if row1[i-1] == row2[i-1] and row3[i-1] and not ' ':
             won = True
             winner = row1[i-1]
             print('bug 41')
    if row1[0] == row2[1] and row3[2] and not ' ':
        won = True
        winner = row1[0]
        print('bug 45')
    elif row1[2] == row2[1] and row3[0] and not ' ':
        won = True
        winner = row3[0]
        print('bug 49')



print(str(row1)+"\n"+str(row2)+"\n"+str(row3))
print(winner, "has won")
