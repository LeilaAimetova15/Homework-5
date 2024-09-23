immutable_var = (1, 2, 3, 'Hello', 5.5)
print(immutable_var)
#immutable_var[0] = 15
#Элементы кортежа неизменяемы, так как кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных.
mutable_list = ([5, 10], 'a', 'b', 3.2)
mutable_list[0][0] = 25
print(mutable_list)
