print("\n\nЭто будет проект по задачам Эйлера!\n\n")

#-----------------------------------------------
#---------------------Задача №1------------------
#-----------------------------------------------

print('''Первая задача!
\"Числа, кратные 3 или 6, в пределах 1 000\":''', end=" ")

sum = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i

print("Ответ \"" + str(sum) + "\" является верным" + "\n")

#------------------------------------------------
#---------------------Задача №2------------------
#-----------------------------------------------

print('''Вторая задача!
\"Чётные числа Фибоначи, в пределах 4 000 000\":''', end=" ")

fibonach = [1, 2]   #Первые два члена последовательности Фибоначи
i = 1               #Позиция последнего текущего элемента
sum = 0             #Сумма всех чётных элементов

while fibonach[i] < 4000000:
    if fibonach[i] % 2 == 0:
        sum += int(fibonach[i])
    fibonach += [(int(fibonach[i]) + int(fibonach[i-1]))]
    i += 1
print("Ответ \"" + str(sum) + "\" является верным" + "\n")

#------------------------------------------------
#---------------------Задача №3------------------
#-----------------------------------------------

number = 600851475143
test_number = 13195     #Его делители должны быть 5, 7, 13 и 29

print('''Третья задача!
\"Наибольший простой делитель чила ''' + str(number) + "\":", end = " ")

def Zadch3(number):

    all_numbers = list()                    #Спиок всех чисел
    all_numbers_fin = list()
    all_numbers_position = list()
    i = 0

    for numbers in range(2, number + 1):    #Составление списка от 2 до n
        all_numbers += [numbers]            #Элементов, для дальнейшего нахождения простых чисел
        all_numbers_position += [True]      #Индексы элементов
    while all_numbers[i] < number:
        j = all_numbers[i] + i
        while j < number - 1:
            all_numbers_position[j] = False
            j += all_numbers[i]
        i += 1
    for position in range(number -1):
        if all_numbers_position[position]:
            all_numbers_fin += [all_numbers[position]]
    print(all_numbers_fin, end = ' ')
        

    #print(all_numbers_position)

Zadch3(number)