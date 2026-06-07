savings = int(input('Сколько вы хотите положить денег в банк: '))
interest = int(input('Под какой процент вы кладете деньги: ')) / 100
time = int(input('На сколько лет вы хотите положить деньги в банк: '))

def calculate_savings(savings, interest, time):
    '''
вычисляем итоговую сумму вклада с процентами
принимает значения накоплений, процент и время, на которое мы делаем вклад
возвращает итогувую сумму
'''
    for t in range(time):
        savings += savings*interest
        
    return savings


def bank(s, i=0.02, t=1):
    '''
расчитываем вклад
принимает значения суммы вклада, процент, срок вклада
возвращаем итоговую сумму вклада или False если процент превышает 5%
'''
    if i > 0.05:
        print('слишком большой процент, максимальный 5% годовых')
        return False

    savings = calculate_savings(s, i, t)
    return savings

total_saving = bank(savings, interest, time)
if total_saving:
    print(f'Ваш итоговый счёт в банке: {total_saving}')

