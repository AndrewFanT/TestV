player = '*'
place = [['_', '*', '_'],
         ['_','_','_'],
         ['_','_','_']]
print(place)
row = 0
col = 1
place[row][col] = player
ogr1 = len(place[row])
com = str(input())
while com != 'выход':
    
    if com == 'влево':
        if col == 0:
            print('дальше нельзя')
        else:
            place[row][col] = '_'
            col = col - 1
            
    if com == 'вправо':
        if col == 2:
            print('дальше нельзя')
        else:
            place[row][col] = '_'
            col = col + 1
            
    if com == 'вверх':
        if row == 0:
            print('дальше нельзя')
        else:
            place[row][col] = '_'
            row = row - 1
            
    if com == 'вниз':
        if row == 2:
            print('дальше нельзя')
        else:
            place[row][col] = '_'
            row = row + 1
            
    place[row][col] = player
    print(place)
    com = str(input())
    
