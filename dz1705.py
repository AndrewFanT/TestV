# В коде происходит выбор между двумя доступными фигурами (круг или прямоугольник)
# И далее происходит вычисление их площадей

# Сейчас это плохой код: всё в куче, без декомпозиции и абстракции
# Исправь этот код используя декомпозицию, абстракцию и абстракцию через параметризацию

def calk_circle():
    radius = float(input("Введите радиус: "))
    pi = 3.14
    area1 = pi * radius ** 2
    return area1
    
def calk_rectangle():
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    area = a * b
    return area1


def view_circle():
    area = calk_circle()
    print(f"Площадь круга: {area}")

def view_rectangle():
    area = calk_rectangle()
    print(f"Площадь прямоугольника: {area}")
    

shape = input("Введите фигуру (circle, rectangle): ")
if shape == "circle":
    view_circle()
    
elif shape == "rectangle":
   view_rectangle()
    
else:
    print("Неизвестная фигура")
