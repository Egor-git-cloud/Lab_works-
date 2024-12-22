#Задача 1 
#def greet(n):
#    return('Дарова, ' + str(n) + '!')
#print(greet(input('Введи имя: ')))


#def square(n):
#    return('Его квадрат - ' + str(n**2))
#print(square(int(input("Введи число: "))))


# def max_of_two(x, y):
#    return('Большее из них - ' + str(max(x,y)))
# print(max_of_two(int(input("Введи первое число: ")),int(input("Введи второе число: ")) ))

#Задача 2
# def describe_person(name, age=30):
#    print( 'Тебя зовут ', name,'. Тебе возможно ', age)
# describe_person('bob',12)
#

#Задача 3
# def is_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return'False'
#         else:
#             return 'True'
# print(is_prime(int(input())))

a = [int(x) for x in range(101)]#список от 0 до 100
def shag(a,x):#(название массива, шаг зануления)
    for i in range(0,len(a),x):
        a[i]=0
    print(a)
shag(a,3)