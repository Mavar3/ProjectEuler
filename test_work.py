print("\n\nЭто будет проект по задачам Эйлера!\n\n")

# -----------------------------------------------
# ---------------------Задача №1------------------
# -----------------------------------------------

print("Первая задача!")
print("\"Числа, кратные 3 или 5, в пределах 1 000\":", end=" ")

summa = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        summa += i

print("Ответ \"" + str(summa) + "\" является верным" + "\n")

# ------------------------------------------------
# ---------------------Задача №2------------------
# -----------------------------------------------

print("Вторая задача!")
print("\"Чётные числа Фибоначчи, в пределах 4 000 000\":", end = " ")

fibonach = [1, 2]   #Первые два члена последовательности Фибоначи
i = 1               #Позиция последнего текущего элемента
summa = 0             #Сумма всех чётных элементов

while fibonach[i] < 4000000:
    if fibonach[i] % 2 == 0:
        summa += fibonach[i]
    fibonach += [fibonach[i] + fibonach[i-1]]
    i += 1
    
print("Ответ \"" + str(summa) + "\" является верным" + "\n")

# ------------------------------------------------
# ---------------------Задача №3------------------
# -----------------------------------------------

'''
number = 600851475143
test_number = 13195     # Его делители должны быть 5, 7, 13 и 29

print('Третья задача!'
print('\"Наибольший простой делитель чила ' + str(number) + '\":', end = " ")

def Zadch3(number):


    for i in range (int(number / 2), 1, -1):       #Простые числа 
        for j in range (3, i + 1, 2):                   #На которые может делиться
            if i % j != 0:                              #Наше основное число.
                continue                                #Поэтому (number + 1) / 2
            elif i == j:
                if number % i == 0:
                    print(i)
                    return
                break
            else:
                break     

Zadch3(number)
'''

# ------------------------------------------------
# ---------------------Задача №4------------------
# -----------------------------------------------

print ("Четвёртая задача!")
print("\"Наибольшее произведение-палиндром\":", end = " ")

def Task4():   
    '''Наибольшее произведение-палиндром среди трёхзначных чисел'''

    palindrome = list()
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            if str(i * j)[::1] == str(i * j)[::-1]:
                    palindrome += [i * j]
                    
                    
    print("Ответ \"" + str(max(palindrome)) + "\" является верным" + "\n")
    
Task4()

# ------------------------------------------------
# ---------------------Задача №5------------------
# -----------------------------------------------

print ("Пятая задача!")
print("\"Наименьшее кратное\":", end = " ")

# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# Думает 2 минуты 4 секунды

def Task5(number):
    # Какое самое маленькое число делится нацело на все числа от 1 до 20?
    
    list_of = list()
    
    for i in range(number, int(number / 2), -1):
        list_of.append(i)

    counter = 0

    while counter < len(list_of):
        counter = 0
        number += 1
        for i in list_of:
            if number % i == 0:
                counter += 1
            else:
                break
        
    print("Ответ \"" + str(number) + "\" является верным" + "\n")

number = 20
Task5(number)

# ------------------------------------------------
# ---------------------Задача №6------------------
# -----------------------------------------------

print ("Шестая задача!")
print("\"Разность между суммой квадратов и квадратом суммы\":", end = " ")

def Task6(number):
    
    summ = 0
    sum_kvad = 0
    
    for i in range (1, number + 1):
        summ += i
        sum_kvad += i**2
        
    print("Ответ \"" + str(abs(sum_kvad - summ**2)) + "\" является верным" + "\n")

number = 100
Task6(number)

# ------------------------------------------------
# ---------------------Задача №7------------------
# -----------------------------------------------

print ("Седьмая задача!")
print("\"10001-ое простое число\":", end = " ")

def Task7(number):
    
    counter = 1
    main_counter = 1
    score = 0

    while main_counter < number:
        counter += 2
        for i in range(3, counter + 1, 2):
            if counter % i != 0:
                continue
            elif counter == i:
                main_counter += 1
                score = i
                break
            else:
                break
    print("Ответ \"" + str(score) + "\" является верным" + "\n")

number = 10001
Task7(number)

# ------------------------------------------------
# ---------------------Задача №7------------------
# -----------------------------------------------

print ("Седьмая задача!")
print("\"Наибольшее произведение в последовательности\":", end = " ")

def Task8(number, qulity):

    maxx = 0
    # max_sequence = list()

    for score in range(qulity, len(number), 1):
        
        promez = 1
        # sequence = list()

        # for i in range(qulity):
            # sequence.append(i)

        for j in range (score, score - qulity, -1):
            promez *= int(number[j])
            # sequence[j % qulity] = number[j]
        if maxx < promez:
            maxx = promez
            # max_sequence = sequence.copy()
        
    print("Ответ \"" + str(maxx) + "\" является верным" + "\n")    

qulity = 13
number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
Task8(number, qulity)