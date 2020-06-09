"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
print('Введите длинных трех отрезков')
a = float(input('Длина отрезка А: '))
b = float(input('Длина отрезка В: '))
c = float(input('Длина отрезка С: '))

if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c:
        print('Это равностронний треугольник')
    elif a == b or a == c or b == c:
        print('Это равнобедренный треугольник')
    else:
        print('Это разностронний треугольник')

else:
    print('Из заданных отрезков треугольника не получится!')


