n = int(input("Введите число: ")) #ввод числа
f1=0 #первое число для вычисления чисел Фибоначчи
f2=1 #второе число для вычисления чисел Фибоначчи
f_sum=0 #сумма двух чисел
while f_sum<n:#если число Фибоначчи меньше заданного числа
    print(f_sum) #вывод Фибаначчи
    f_sum=f1+f2 #вычисление суммы
    f1=f2 #приравниваем первое число со вторым
    f2=f_sum #приравниваем второе с суммой