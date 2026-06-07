def build_house(idea, colors):
    house = False
    roof_color = colors[0]
    house_color = colors[1]
    door_color = colors[2]
    roof = idea[0]
    walls = idea[1]
    door = idea[2]

    while not house:
        roof_status = build_roof(roof, roof_color)
        walls_status = build_walls(walls, house_color)
        door_status = build_doors(door, door_color)

        if roof_status == True and walls_status == True and door_status == True:
            house = True
            print('Дом построен!')

    return house


def build_roof(roof, roof_color):
    '''
    получает: roof - данные для крыши, roof_color - данные для цвета крыши
    возвращает: bool
    '''
    return True

def build_walls(walls, walls_color):
    '''
    получает: walls - данные для стен, walls_color - данные для цвета стен
    возвращает: bool
    '''
    return True

def build_doors(door, door_color):
    '''
    получает: door - данные для двери, door_color - данные для цвета двери
    возвращает: bool
    '''
    return True



idea = ('roof', 'walls', 'door')
colors = ('brown', 'yellow', 'blue')
print(build_house(idea, colors))
