
# #Задание 1
# def read(n, type = 'all'):
#     if type == 'str':
#         with open(n, 'r') as file:
#             for i in file:
#                 print(i)
#     if type == 'all':
#         with open(n, 'r') as file:
#             print(file.read())
# read('example.txt')







#Задание 3
# def read(n, type = 'all'):
#     try:
#         if type == 'str':
#             with open(n, 'r') as file:
#                 for i in file:
#                     print(i)
#         if type == 'all':
#             with open(n, 'r') as file:
#                 print(file.read())
#     except FileNotFoundError:
#         print('<!!!FileNotFoundError!!!>')
#         print('Ты чё то попутал конкретно')
# read('example.txt')
