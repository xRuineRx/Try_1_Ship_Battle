# Дано:
# В данном задании не испрользованны классы, я понятия не имею как вставить объект класса на игральную доску
# При выводе кораблей на поле, игрок МОЖЕТ вставить все корабли в одно место без ограничений ( у компьютера такая возможность отстуствует)
# Сдаю в таком виде по скольку даже если я выполню задание чрез циклы, есть подозрение ,что без использования классов, его не примут.
# Жду обратную связь
#_________________________________________________________________________________________________________





os_X_0 = ["  ",[1],[2],[3],[4],[5],[6]]
os_Y_1 = [[1],["O"],["O"],["O"],["O"],["O"],["O"]]
os_Y_2 = [[2],["O"],["O"],["O"],["O"],["O"],["O"]]
os_Y_3 = [[3],["O"],["O"],["O"],["O"],["O"],["O"]]
os_Y_4 = [[4],["O"],["O"],["O"],["O"],["O"],["O"]]
os_Y_5 = [[5],["O"],["O"],["O"],["O"],["O"],["O"]]
os_Y_6 = [[6],["O"],["O"],["O"],["O"],["O"],["O"]]

import copy

os_X_0_2_pole = copy.deepcopy(os_X_0)
os_Y_1_2_pole = copy.deepcopy(os_Y_1)
os_Y_2_2_pole = copy.deepcopy(os_Y_2)
os_Y_3_2_pole = copy.deepcopy(os_Y_3)
os_Y_4_2_pole = copy.deepcopy(os_Y_4)
os_Y_5_2_pole = copy.deepcopy(os_Y_5)
os_Y_6_2_pole = copy.deepcopy(os_Y_6)

# Ячейка коробля - ■
# Всего 7 кораблей : 1 корабль(3■),2 корабля(2■),4 корабля(1■)
# Расстояние между кораблями строго 1 клетка


### Класс корабля
### Кодовые имена коробля:
###Корабль 3 лычки - "lvl_3" и т.д.
class Ship:
    def __init__(self, name, length, mark = "■"):
        self.name = name
        self.length = length
        self.mark = mark

    def get_length(self):
        return self.length * list(self.mark)

    def parking(self):
        for x in self.get_length():
            return self.get_length()

#1 корабль 3 лычки
lvl_3_1 = Ship(name ="3 лычки_1",length = 3 , mark = "■")

#2 корабля по 2 лычки
lvl_2_2 = Ship(name ="2 лычки_2",length = 2 , mark = "■")
lvl_2_1 = Ship(name ="2 лычки_1",length = 2 , mark = "■")

#4 корабля по 1 лычке
lvl_1_4 = Ship(name ="1 лычки_4",length = 1 , mark = "■")
lvl_1_3 = Ship(name ="1 лычки_3",length = 1 , mark = "■")
lvl_1_2 = Ship(name ="1 лычки_2",length = 1 , mark = "■")
lvl_1_1 = Ship(name ="1 лычки_1",length = 1 , mark = "■")

#________________________________________________________________________________________
#Вставка кораблей на поле
#Нужно выбрать место вставки, запрос будет большого корабля к малому.
#Выбор размещения коробля сделаем поэтапно. Потребуется выбор места где будет расположен,
#а для короблей 3 и 2 лычек еще важно выбрать горизонтально или вертикально.
#________________________________________________________________________________________
#Для корабля 3 лычки: (ВСЕГО НУЖЕН 1 КОРАБЛЬ НА ПОЛЕ)

#Запрос на ввод данных
##Vert = "Vert"
##Gor = "Gor"
##ans = input("Вертикально или горизонтально вы хотите разместить корабль?: Впишите Vert или Gor: ")
##
##
##try:
##    os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
##    os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
##except ValueError:
##    print("Вводите пожалуйста числа, а не буквы!")

##Работает корректно
##Важное замечание, при выборе ячеек начала тела короблая ячеек 5 и 6,
##будут выбраны ближайшие к ним ячейки,чтобы остаться в рамках поля.
def ship_lvl_3_add(ans,os_Y_inp,os_X_inp):
    #если вертикально
    if ans == Vert:
        try:
            if os_Y_inp == 1:
                if os_X_inp <= 4:
                    os_Y_1[os_X_inp] = "■"
                    os_Y_1[os_X_inp + 1] = "■"
                    os_Y_1[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_1[os_X_inp] = "■"
                    os_Y_1[os_X_inp + 1] = "■"
                    os_Y_1[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_1[os_X_inp] = "■"
                    os_Y_1[os_X_inp - 1] = "■"
                    os_Y_1[os_X_inp - 2] = "■"
                    
            elif os_Y_inp == 2:
                if os_X_inp <= 4:
                    os_Y_2[os_X_inp] = "■"
                    os_Y_2[os_X_inp + 1] = "■"
                    os_Y_2[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_2[os_X_inp] = "■"
                    os_Y_2[os_X_inp + 1] = "■"
                    os_Y_2[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_2[os_X_inp] = "■"
                    os_Y_2[os_X_inp - 1] = "■"
                    os_Y_2[os_X_inp - 2] = "■"
                    
            elif os_Y_inp == 3:
                if os_X_inp <= 4:
                    os_Y_3[os_X_inp] = "■"
                    os_Y_3[os_X_inp + 1] = "■"
                    os_Y_3[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_3[os_X_inp] = "■"
                    os_Y_3[os_X_inp + 1] = "■"
                    os_Y_3[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_3[os_X_inp] = "■"
                    os_Y_3[os_X_inp - 1] = "■"
                    os_Y_3[os_X_inp - 2] = "■"
                    
            elif os_Y_inp == 4:
                if os_X_inp <= 4:
                    os_Y_4[os_X_inp] = "■"
                    os_Y_4[os_X_inp + 1] = "■"
                    os_Y_4[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_4[os_X_inp] = "■"
                    os_Y_4[os_X_inp + 1] = "■"
                    os_Y_4[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_4[os_X_inp] = "■"
                    os_Y_4[os_X_inp - 1] = "■"
                    os_Y_4[os_X_inp - 2] = "■"
                    
            elif os_Y_inp == 5:
                if os_X_inp <= 4:
                    os_Y_5[os_X_inp] = "■"
                    os_Y_5[os_X_inp + 1] = "■"
                    os_Y_5[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_5[os_X_inp] = "■"
                    os_Y_5[os_X_inp + 1] = "■"
                    os_Y_5[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_5[os_X_inp] = "■"
                    os_Y_5[os_X_inp - 1] = "■"
                    os_Y_5[os_X_inp - 2] = "■"
                    
            elif os_Y_inp == 6:
                if os_X_inp <= 4:
                    os_Y_6[os_X_inp] = "■"
                    os_Y_6[os_X_inp + 1] = "■"
                    os_Y_6[os_X_inp + 2] = "■"
                    
                elif os_X_inp == 5:
                    os_Y_6[os_X_inp] = "■"
                    os_Y_6[os_X_inp + 1] = "■"
                    os_Y_6[os_X_inp - 1] = "■"
                    
                elif os_X_inp == 6:
                    os_Y_6[os_X_inp] = "■"
                    os_Y_6[os_X_inp - 1] = "■"
                    os_Y_6[os_X_inp - 2] = "■"
            elif os_Y_inp > 6 or os_Y_inp < 0:
                print("Неверное задано значение, еще раз.")
        except IndexError:
            print("Вводите число в правильном диапазоне!")
        except:
            print("Что то пошло не так , убедитесь что вы вводили числа")

    #если горизонтально расположен корабль
    elif ans == Gor:
        try:
            if os_Y_inp == 1:
                os_Y_1[os_X_inp] = "■"
                os_Y_2[os_X_inp] = "■"
                os_Y_3[os_X_inp] = "■"
                
            elif os_Y_inp == 2:
                os_Y_2[os_X_inp] = "■"
                os_Y_3[os_X_inp] = "■"
                os_Y_4[os_X_inp] = "■"
                
            elif os_Y_inp == 3:
                os_Y_3[os_X_inp] = "■"
                os_Y_4[os_X_inp] = "■"
                os_Y_5[os_X_inp] = "■"
                
            elif os_Y_inp == 4:
                os_Y_4[os_X_inp] = "■"
                os_Y_5[os_X_inp] = "■"
                os_Y_6[os_X_inp] = "■"
                
            elif os_Y_inp == 5:
                os_Y_5[os_X_inp] = "■"
                os_Y_6[os_X_inp] = "■"
                os_Y_4[os_X_inp] = "■"
                
            elif os_Y_inp == 6:
                os_Y_6[os_X_inp] = "■"
                os_Y_5[os_X_inp] = "■"
                os_Y_4[os_X_inp] = "■"
                
            elif os_Y_inp > 6 or os_Y_inp < 0:
                print("Неверное задано значение, еще раз.")
        except IndexError:
            print("Вводите чесло в правильном диапазоне!")
        except:
            print("Что то пошло не так , убедитесь что вы вводили числа")


#_________________________________________________________________________________________________________
#Для корабля 2 лычки: (ВСЕГО НУЖНО 2 КОРАБЛЯ НА ПОЛЕ)

#Запрос на ввод данных
##Vert = "Vert"
##Gor = "Gor"
##ans = input("Вертикально или горизонтально вы хотите разместить корабль?: Впишите Vert или Gor: ")
##
##try:
##    os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
##    os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
##except ValueError:
##    print("Вводите пожалуйста числа, а не буквы!")
    
##Работает корректно
def ship_lvl_2_add(ans,os_Y_inp,os_X_inp):
    #если вертикально расположен корабль
    if ans == Vert:
        try:
            if os_Y_inp == 1:
                if os_X_inp <= 5:
                    os_Y_1[os_X_inp] = "■"
                    os_Y_1[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_1[os_X_inp] = "■"
                    os_Y_1[os_X_inp - 1] = "■"
                    
            elif os_Y_inp == 2:
                if os_X_inp <= 5:
                    os_Y_2[os_X_inp] = "■"
                    os_Y_2[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_2[os_X_inp] = "■"
                    os_Y_2[os_X_inp - 1] = "■"
                    
            elif os_Y_inp == 3:
                if os_X_inp <= 5:
                    os_Y_3[os_X_inp] = "■"
                    os_Y_3[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_3[os_X_inp] = "■"
                    os_Y_3[os_X_inp - 1] = "■"
                
            elif os_Y_inp == 4:
                if os_X_inp <= 5:
                    os_Y_4[os_X_inp] = "■"
                    os_Y_4[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_4[os_X_inp] = "■"
                    os_Y_4[os_X_inp - 1] = "■"
                
            elif os_Y_inp == 5:
                if os_X_inp <= 5:
                    os_Y_5[os_X_inp] = "■"
                    os_Y_5[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_5[os_X_inp] = "■"
                    os_Y_5[os_X_inp - 1] = "■"
                
            elif os_Y_inp == 6:
                if os_X_inp <= 5:
                    os_Y_6[os_X_inp] = "■"
                    os_Y_6[os_X_inp + 1] = "■"
                elif os_X_inp == 6:
                    os_Y_6[os_X_inp] = "■"
                    os_Y_6[os_X_inp - 1] = "■"
            
            elif os_Y_inp > 6 or os_Y_inp < 0:
                print("Неверное задано значение, еще раз.")
        except IndexError:
            print("Вводите чесло в правильном диапазоне!")
        except:
            print("Что то пошло не так , убедитесь что вы вводили числа")

    #если горизонтально расположен корабль
    elif ans == Gor:
        try:
            if os_Y_inp == 1:
                os_Y_1[os_X_inp] = "■"
                os_Y_2[os_X_inp] = "■"
            elif os_Y_inp == 2:
                os_Y_2[os_X_inp] = "■"
                os_Y_3[os_X_inp] = "■"
            elif os_Y_inp == 3:
                os_Y_3[os_X_inp] = "■"
                os_Y_4[os_X_inp] = "■"
            elif os_Y_inp == 4:
                os_Y_4[os_X_inp] = "■"
                os_Y_5[os_X_inp] = "■"
            elif os_Y_inp == 5:
                os_Y_5[os_X_inp] = "■"
                os_Y_6[os_X_inp] = "■"
            elif os_Y_inp == 6:
                os_Y_6[os_X_inp] = "■"
                os_Y_5[os_X_inp] = "■"
            elif os_Y_inp > 6 or os_Y_inp < 0:
                print("Неверное задано значение, еще раз.")
        except IndexError:
            print("Вводите чесло в правильном диапазоне!")
        except:
            print("Что то пошло не так , убедитесь что вы вводили числа")

#_________________________________________________________________________________________________________
#Для корабля 1 лычки: (ВСЕГО НУЖНО 4 КОРОБЛЯ НА ПОЛЕ)
#Занимает только 1 клетку, вертикальность или горизонтальность не интересует

#Запрос на ввод данных:
##try:
##    os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
##    os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
##except ValueError:
##    print("Вводите пожалуйста числа, а не буквы!")

##Работает корректно
def ship_lvl_1_add(os_Y_inp,os_X_inp):
    try:
        if os_Y_inp == 1:
            os_Y_1[os_X_inp] = "■"
        elif os_Y_inp == 2:
            os_Y_2[os_X_inp] = "■"
        elif os_Y_inp == 3:
            os_Y_3[os_X_inp] = "■"
        elif os_Y_inp == 4:
            os_Y_4[os_X_inp] = "■"
        elif os_Y_inp == 5:
            os_Y_5[os_X_inp] = "■"
        elif os_Y_inp == 6:
            os_Y_6[os_X_inp] = "■"
        elif os_Y_inp > 6 or os_Y_inp < 0:
            print("Неверное задано значение, еще раз.")
    except IndexError:
        print("Вводите чесло в правильном диапазоне!")
    except:
        print("Что то пошло не так , убедитесь что вы вводили числа")

#_________________________________________________________________________________________________________
#Счетчики выставления всех кораблей на поле
count_lvl_3 = 0
count_lvl_2 = 0
count_lvl_1 = 0

#Теперь вставим все корабли и выведим поле с кораблями
#корабль 3:
while count_lvl_3 < 1:
    Vert = "Vert"
    Gor = "Gor"
    ans = input("Вертикально или горизонтально вы хотите разместить корабль?: Впишите Vert или Gor: ")

    try:
        os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
        os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
    except ValueError:
        print("Вводите пожалуйста числа, а не буквы!")
    ship_lvl_3_add(ans,os_Y_inp,os_X_inp)
    print(os_X_0)
    print(os_Y_1)
    print(os_Y_2)
    print(os_Y_3)
    print(os_Y_4)
    print(os_Y_5)
    print(os_Y_6)
    count_lvl_3 += 1
    
#Корабль 2:
while count_lvl_2 < 2:
    Vert = "Vert"
    Gor = "Gor"
    ans = input("Вертикально или горизонтально вы хотите разместить корабль?: Впишите Vert или Gor: ")

    try:
        os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
        os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
    except ValueError:
        print("Вводите пожалуйста числа, а не буквы!")
    ship_lvl_2_add(ans,os_Y_inp,os_X_inp)
    print(os_X_0)
    print(os_Y_1)
    print(os_Y_2)
    print(os_Y_3)
    print(os_Y_4)
    print(os_Y_5)
    print(os_Y_6)
    count_lvl_2 += 1

#Корабль 1:
while count_lvl_1 < 4:
    try:
        os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
        os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
    except ValueError:
        print("Вводите пожалуйста числа, а не буквы!")
    ship_lvl_1_add(os_Y_inp,os_X_inp)
    print(os_X_0)
    print(os_Y_1)
    print(os_Y_2)
    print(os_Y_3)
    print(os_Y_4)
    print(os_Y_5)
    print(os_Y_6)
    count_lvl_1 += 1
#_________________________________________________________________________________________________________
#Вывод поля на котором корабли и которое мы атакуем:
#Продублируем поле для атаки,концовка _at (атака)
#Позже понадобиться чтоб ИИ ссылался на наше поле для атаки

import copy

os_X_0_at = copy.deepcopy(os_X_0)
os_Y_1_at = copy.deepcopy(os_Y_1)
os_Y_2_at = copy.deepcopy(os_Y_2)
os_Y_3_at = copy.deepcopy(os_Y_3)
os_Y_4_at = copy.deepcopy(os_Y_4)
os_Y_5_at = copy.deepcopy(os_Y_5)
os_Y_6_at = copy.deepcopy(os_Y_6)

 
 
#_________________________________________________________________________________________________________
#_________________________________________________________________________________________________________
#_________________________________________________________________________________________________________
## Вставка кораблей ИИ


#нужен пакет рандома
import random

#Добавим корабль 3 лычки для ИИ
def ship_AI_lvl_3_add(ans,os_Y_inp,os_X_inp):
    #если вертикально
    if ans == "Vert":
        if os_Y_inp == 1:
            if os_X_inp <= 4:
                os_Y_1_2_pole[os_X_inp] = "■"
                os_Y_1_2_pole[os_X_inp + 1] = "■"
                os_Y_1_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_1_2_pole[os_X_inp] = "■"
                os_Y_1_2_pole[os_X_inp + 1] = "■"
                os_Y_1_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_1_2_pole[os_X_inp] = "■"
                os_Y_1_2_pole[os_X_inp - 1] = "■"
                os_Y_1_2_pole[os_X_inp - 2] = "■"
                
        elif os_Y_inp == 2:
            if os_X_inp <= 4:
                os_Y_2_2_pole[os_X_inp] = "■"
                os_Y_2_2_pole[os_X_inp + 1] = "■"
                os_Y_2_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_2_2_pole[os_X_inp] = "■"
                os_Y_2_2_pole[os_X_inp + 1] = "■"
                os_Y_2_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_2_2_pole[os_X_inp] = "■"
                os_Y_2_2_pole[os_X_inp - 1] = "■"
                os_Y_2_2_pole[os_X_inp - 2] = "■"
                
        elif os_Y_inp == 3:
            if os_X_inp <= 4:
                os_Y_3_2_pole[os_X_inp] = "■"
                os_Y_3_2_pole[os_X_inp + 1] = "■"
                os_Y_3_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_3_2_pole[os_X_inp] = "■"
                os_Y_3_2_pole[os_X_inp + 1] = "■"
                os_Y_3_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_3_2_pole[os_X_inp] = "■"
                os_Y_3_2_pole[os_X_inp - 1] = "■"
                os_Y_3_2_pole[os_X_inp - 2] = "■"
                
        elif os_Y_inp == 4:
            if os_X_inp <= 4:
                os_Y_4_2_pole[os_X_inp] = "■"
                os_Y_4_2_pole[os_X_inp + 1] = "■"
                os_Y_4_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_4_2_pole[os_X_inp] = "■"
                os_Y_4_2_pole[os_X_inp + 1] = "■"
                os_Y_4_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_4_2_pole[os_X_inp] = "■"
                os_Y_4_2_pole[os_X_inp - 1] = "■"
                os_Y_4_2_pole[os_X_inp - 2] = "■"
                
        elif os_Y_inp == 5:
            if os_X_inp <= 4:
                os_Y_5_2_pole[os_X_inp] = "■"
                os_Y_5_2_pole[os_X_inp + 1] = "■"
                os_Y_5_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_5_2_pole[os_X_inp] = "■"
                os_Y_5_2_pole[os_X_inp + 1] = "■"
                os_Y_5_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_5_2_pole[os_X_inp] = "■"
                os_Y_5_2_pole[os_X_inp - 1] = "■"
                os_Y_5_2_pole[os_X_inp - 2] = "■"
                
        elif os_Y_inp == 6:
            if os_X_inp <= 4:
                os_Y_6_2_pole[os_X_inp] = "■"
                os_Y_6_2_pole[os_X_inp + 1] = "■"
                os_Y_6_2_pole[os_X_inp + 2] = "■"
                
            elif os_X_inp == 5:
                os_Y_6_2_pole[os_X_inp] = "■"
                os_Y_6_2_pole[os_X_inp + 1] = "■"
                os_Y_6_2_pole[os_X_inp - 1] = "■"
                
            elif os_X_inp == 6:
                os_Y_6_2_pole[os_X_inp] = "■"
                os_Y_6_2_pole[os_X_inp - 1] = "■"
                os_Y_6_2_pole[os_X_inp - 2] = "■"


    #если горизонтально расположен корабль
    elif ans == "Gor":
        if os_Y_inp == 1:
            os_Y_1_2_pole[os_X_inp] = "■"
            os_Y_2_2_pole[os_X_inp] = "■"
            os_Y_3_2_pole[os_X_inp] = "■"
            
        elif os_Y_inp == 2:
            os_Y_2_2_pole[os_X_inp] = "■"
            os_Y_3_2_pole[os_X_inp] = "■"
            os_Y_4_2_pole[os_X_inp] = "■"
            
        elif os_Y_inp == 3:
            os_Y_3_2_pole[os_X_inp] = "■"
            os_Y_4_2_pole[os_X_inp] = "■"
            os_Y_5_2_pole[os_X_inp] = "■"
            
        elif os_Y_inp == 4:
            os_Y_4_2_pole[os_X_inp] = "■"
            os_Y_5_2_pole[os_X_inp] = "■"
            os_Y_6_2_pole[os_X_inp] = "■"
            
        elif os_Y_inp == 5:
            os_Y_5_2_pole[os_X_inp] = "■"
            os_Y_6_2_pole[os_X_inp] = "■"
            os_Y_4_2_pole[os_X_inp] = "■"
            
        elif os_Y_inp == 6:
            os_Y_6_2_pole[os_X_inp] = "■"
            os_Y_5_2_pole[os_X_inp] = "■"
            os_Y_4_2_pole[os_X_inp] = "■"
                



def ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp):
    #если вертикально расположен корабль
    if ans == "Vert":
        if os_Y_inp == 1:
            if os_X_inp <= 5:
                if os_Y_1_2_pole[os_X_inp] != "■":
                    if os_Y_1_2_pole[os_X_inp + 1] != "■":
                        os_Y_1_2_pole[os_X_inp] = "■"
                        os_Y_1_2_pole[os_X_inp + 1] = "■"
                elif os_Y_1_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_1_2_pole[os_X_inp] != "■":
                    if os_Y_1_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                    
            elif os_X_inp == 6:
                if os_Y_1_2_pole[os_X_inp] != "■":
                    if os_Y_1_2_pole[os_X_inp - 1] != "■":
                        os_Y_1_2_pole[os_X_inp] = "■"
                        os_Y_1_2_pole[os_X_inp - 1] = "■"
                elif os_Y_1_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_1_2_pole[os_X_inp] != "■":
                    if os_Y_1_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)

        elif os_Y_inp == 2:
            if os_X_inp <= 5:
                if os_Y_2_2_pole[os_X_inp] != "■":
                    if os_Y_2_2_pole[os_X_inp + 1] != "■":
                        os_Y_2_2_pole[os_X_inp] = "■"
                        os_Y_2_2_pole[os_X_inp + 1] = "■"
                elif os_Y_2_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_2_2_pole[os_X_inp] != "■":
                    if os_Y_2_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                    
            elif os_X_inp == 6:
                if os_Y_2_2_pole[os_X_inp] != "■":
                    if os_Y_2_2_pole[os_X_inp - 1] != "■":
                        os_Y_2_2_pole[os_X_inp] = "■"
                        os_Y_2_2_pole[os_X_inp - 1] = "■"
                elif os_Y_2_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_2_2_pole[os_X_inp] != "■":
                    if os_Y_2_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)

                
        elif os_Y_inp == 3:
            if os_X_inp <= 5:
                if os_Y_3_2_pole[os_X_inp] != "■":
                    if os_Y_3_2_pole[os_X_inp + 1] != "■":
                        os_Y_3_2_pole[os_X_inp] = "■"
                        os_Y_3_2_pole[os_X_inp + 1] = "■"
                elif os_Y_3_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_3_2_pole[os_X_inp] != "■":
                    if os_Y_3_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                    
            elif os_X_inp == 6:
                if os_Y_3_2_pole[os_X_inp] != "■":
                    if os_Y_3_2_pole[os_X_inp - 1] != "■":
                        os_Y_3_2_pole[os_X_inp] = "■"
                        os_Y_3_2_pole[os_X_inp - 1] = "■"
                elif os_Y_3_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_3_2_pole[os_X_inp] != "■":
                    if os_Y_3_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            
        elif os_Y_inp == 4:
            if os_X_inp <= 5:
                if os_Y_4_2_pole[os_X_inp] != "■":
                    if os_Y_4_2_pole[os_X_inp + 1] != "■":
                        os_Y_4_2_pole[os_X_inp] = "■"
                        os_Y_4_2_pole[os_X_inp + 1] = "■"
                elif os_Y_4_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_4_2_pole[os_X_inp] != "■":
                    if os_Y_4_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                    
            elif os_X_inp == 6:
                if os_Y_4_2_pole[os_X_inp] != "■":
                    if os_Y_4_2_pole[os_X_inp - 1] != "■":
                        os_Y_4_2_pole[os_X_inp] = "■"
                        os_Y_4_2_pole[os_X_inp - 1] = "■"
                elif os_Y_4_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_4_2_pole[os_X_inp] != "■":
                    if os_Y_4_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            
        elif os_Y_inp == 5:
            if os_X_inp <= 5:
                if os_Y_5_2_pole[os_X_inp] != "■":
                    if os_Y_5_2_pole[os_X_inp + 1] != "■":
                        os_Y_5_2_pole[os_X_inp] = "■"
                        os_Y_5_2_pole[os_X_inp + 1] = "■"
                elif os_Y_5_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_5_2_pole[os_X_inp] != "■":
                    if os_Y_5_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)

            elif os_X_inp == 6:
                if os_Y_5_2_pole[os_X_inp] != "■":
                    if os_Y_5_2_pole[os_X_inp - 1] != "■":
                        os_Y_5_2_pole[os_X_inp] = "■"
                        os_Y_5_2_pole[os_X_inp - 1] = "■"
                elif os_Y_5_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_5_2_pole[os_X_inp] != "■":
                    if os_Y_5_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            
        elif os_Y_inp == 6:
            if os_X_inp <= 5:
                if os_Y_6_2_pole[os_X_inp] != "■":
                    if os_Y_6_2_pole[os_X_inp + 1] != "■":
                        os_Y_6_2_pole[os_X_inp] = "■"
                        os_Y_6_2_pole[os_X_inp + 1] = "■"
                elif os_Y_6_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_6_2_pole[os_X_inp] != "■":
                    if os_Y_6_2_pole[os_X_inp + 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)

                    
            elif os_X_inp == 6:
                if os_Y_6_2_pole[os_X_inp] != "■":
                    if os_Y_6_2_pole[os_X_inp - 1] != "■":
                        os_Y_6_2_pole[os_X_inp] = "■"
                        os_Y_6_2_pole[os_X_inp - 1] = "■"
                elif os_Y_6_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                elif os_Y_6_2_pole[os_X_inp] != "■":
                    if os_Y_6_2_pole[os_X_inp - 1] == "■":
                        ans = random.choice(["Vert", "Gor"])
                        os_Y_inp =  random.randrange(1,6)
                        os_X_inp =  random.randrange(1,6)
                        ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            


    #если горизонтально расположен корабль
    elif ans == "Gor":
        if os_Y_inp == 1:
            if os_Y_1_2_pole[os_X_inp] != "■":
                if os_Y_2_2_pole[os_X_inp] != "■":
                    os_Y_1_2_pole[os_X_inp] = "■"
                    os_Y_2_2_pole[os_X_inp] = "■"
            elif os_Y_1_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_1_2_pole[os_X_inp] != "■":
                if os_Y_2_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                
        elif os_Y_inp == 2:
            if os_Y_2_2_pole[os_X_inp] != "■":
                if os_Y_3_2_pole[os_X_inp] != "■":
                    os_Y_2_2_pole[os_X_inp] = "■"
                    os_Y_3_2_pole[os_X_inp] = "■"
            elif os_Y_2_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_2_2_pole[os_X_inp] != "■":
                if os_Y_3_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                
        elif os_Y_inp == 3:
            if os_Y_3_2_pole[os_X_inp] != "■":
                if os_Y_4_2_pole[os_X_inp] != "■":
                    os_Y_3_2_pole[os_X_inp] = "■"
                    os_Y_4_2_pole[os_X_inp] = "■"
            elif os_Y_3_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_3_2_pole[os_X_inp] != "■":
                if os_Y_4_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                
        elif os_Y_inp == 4:
            if os_Y_4_2_pole[os_X_inp] != "■":
                if os_Y_5_2_pole[os_X_inp] != "■":
                    os_Y_4_2_pole[os_X_inp] = "■"
                    os_Y_5_2_pole[os_X_inp] = "■"
            elif os_Y_4_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_4_2_pole[os_X_inp] != "■":
                if os_Y_5_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                
        elif os_Y_inp == 5:
            if os_Y_5_2_pole[os_X_inp] != "■":
                if os_Y_6_2_pole[os_X_inp] != "■":
                    os_Y_5_2_pole[os_X_inp] = "■"
                    os_Y_6_2_pole[os_X_inp] = "■"
            elif os_Y_5_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_5_2_pole[os_X_inp] != "■":
                if os_Y_6_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
                
        elif os_Y_inp == 6:
            if os_Y_6_2_pole[os_X_inp] != "■":
                if os_Y_5_2_pole[os_X_inp] != "■":
                    os_Y_6_2_pole[os_X_inp] = "■"
                    os_Y_5_2_pole[os_X_inp] = "■"
            elif os_Y_6_2_pole[os_X_inp] == "■":
                ans = random.choice(["Vert", "Gor"])
                os_Y_inp =  random.randrange(1,6)
                os_X_inp =  random.randrange(1,6)
                ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)
            elif os_Y_6_2_pole[os_X_inp] != "■":
                if os_Y_5_2_pole[os_X_inp] == "■":
                    ans = random.choice(["Vert", "Gor"])
                    os_Y_inp =  random.randrange(1,6)
                    os_X_inp =  random.randrange(1,6)
                    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)


#_________________________________________________________________________________________________________
#Для корабля 1 лычки: (ВСЕГО НУЖНО 4 КОРОБЛЯ НА ПОЛЕ)
#Занимает только 1 клетку, вертикальность или горизонтальность не интересует

#Запрос на ввод данных:
##try:
##    os_Y_inp = int(input("Выберете строку где начнется тело корабля:"))
##    os_X_inp = int(input("Выберете столбец где начнется тело корабля:"))
##except ValueError:
##    print("Вводите пожалуйста числа, а не буквы!")

##Работает корректно
def ship_AI_lvl_1_add(os_Y_inp,os_X_inp):
    if os_Y_inp == 1:
        if os_Y_1_2_pole[os_X_inp] != "■":
            os_Y_1_2_pole[os_X_inp] = "■"
        elif os_Y_1_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp)
            
    elif os_Y_inp == 2:
        if os_Y_2_2_pole[os_X_inp] != "■":
            os_Y_2_2_pole[os_X_inp] = "■"
        elif os_Y_2_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp)
            
    elif os_Y_inp == 3:
        if os_Y_3_2_pole[os_X_inp] != "■":
            os_Y_3_2_pole[os_X_inp] = "■"
        elif os_Y_3_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp)
            
    elif os_Y_inp == 4:
        if os_Y_4_2_pole[os_X_inp] != "■":
            os_Y_4_2_pole[os_X_inp] = "■"
        elif os_Y_4_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp)
            
    elif os_Y_inp == 5:
        if os_Y_5_2_pole[os_X_inp] != "■":
            os_Y_5_2_pole[os_X_inp] = "■"
        elif os_Y_5_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp)
            
    elif os_Y_inp == 6:
        if os_Y_6_2_pole[os_X_inp] != "■":
            os_Y_6_2_pole[os_X_inp] = "■"
        elif os_Y_6_2_pole[os_X_inp] == "■":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_lvl_1_add(os_Y_inp,os_X_inp) 





#_________________________________________________________________________________________________________
#Счетчики выставления всех кораблей на поле
count_AI_lvl_3 = 0
count_AI_lvl_2 = 0
count_AI_lvl_1 = 0

#Теперь вставим все корабли и выведим поле с кораблями
#корабль 3:
ans = random.choice(["Vert", "Gor"])
os_Y_inp =  random.randrange(1,6)
os_X_inp =  random.randrange(1,6)
    
ship_AI_lvl_3_add(ans,os_Y_inp,os_X_inp)
    
count_AI_lvl_3 += 1
    
#Корабль 2:
while count_AI_lvl_2 < 2:
    
    ans = random.choice(["Vert", "Gor"])
    os_Y_inp =  random.randrange(1,6)
    os_X_inp =  random.randrange(1,6)
    
    ship_AI_lvl_2_add(ans,os_Y_inp,os_X_inp)

    count_AI_lvl_2 += 1
    
    
#Корабль 1:
while count_AI_lvl_1 < 4:

    os_Y_inp =  random.randrange(1,6)
    os_X_inp =  random.randrange(1,6)
    
    ship_AI_lvl_1_add(os_Y_inp,os_X_inp)

    count_AI_lvl_1 += 1

if count_AI_lvl_1 == 3:

    os_Y_inp =  random.randrange(1,6)
    os_X_inp =  random.randrange(1,6)
    
    ship_AI_lvl_1_add(os_Y_inp,os_X_inp)

    count_AI_lvl_1 += 1
#__________________________________________________________________________________
# Показ поля с короблями и поля для атаки

lives = (os_Y_1_2_pole.count("■")+os_Y_2_2_pole.count("■")+os_Y_3_2_pole.count("■")+os_Y_4_2_pole.count("■")+os_Y_5_2_pole.count("■")+os_Y_6_2_pole.count("■"))

print("Поле с кораблями поставленными игроком")
print(os_X_0)
print(os_Y_1)
print(os_Y_2)
print(os_Y_3)
print(os_Y_4)
print(os_Y_5)
print(os_Y_6)

print("Поле которое атакует компьютер")
print(os_X_0_at)
print(os_Y_1_at)
print(os_Y_2_at)
print(os_Y_3_at)
print(os_Y_4_at)
print(os_Y_5_at)
print(os_Y_6_at)


print("Поле с кораблями поставленными ИИ")
print(os_X_0_2_pole)
print(os_Y_1_2_pole)
print(os_Y_2_2_pole)
print(os_Y_3_2_pole)
print(os_Y_4_2_pole)
print(os_Y_5_2_pole)
print(os_Y_6_2_pole)


os_X_0_2_at_pole = copy.deepcopy(os_X_0_2_pole)
os_Y_1_2_at_pole = copy.deepcopy(os_Y_1_2_pole)
os_Y_2_2_at_pole = copy.deepcopy(os_Y_2_2_pole)
os_Y_3_2_at_pole = copy.deepcopy(os_Y_3_2_pole)
os_Y_4_2_at_pole = copy.deepcopy(os_Y_4_2_pole)
os_Y_5_2_at_pole = copy.deepcopy(os_Y_5_2_pole)
os_Y_6_2_at_pole = copy.deepcopy(os_Y_6_2_pole)


print("Поле которое атакует игрок")
print(os_X_0_2_at_pole)
print(os_Y_1_2_at_pole)
print(os_Y_2_2_at_pole)
print(os_Y_3_2_at_pole)
print(os_Y_4_2_at_pole)
print(os_Y_5_2_at_pole)
print(os_Y_6_2_at_pole)


#_____________________________________________________________________________________________________
#Функции атаки для Игрока
def ship_attack(os_Y_inp,os_X_inp):
    try:
        if os_Y_inp == 1:
            if os_Y_1_2_pole[os_X_inp] == "■":
                os_Y_1_2_at_pole[os_X_inp] = "X"
            elif os_Y_1_2_at_pole[os_X_inp] == "X" or os_Y_1_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_1_2_pole[os_X_inp] != "■" and os_Y_1_2_pole[os_X_inp] !="X":
                os_Y_1_2_at_pole[os_X_inp] = "T"

            
        elif os_Y_inp == 2:
            if os_Y_2_2_pole[os_X_inp] == "■":
                os_Y_2_2_at_pole[os_X_inp] = "X"
            elif os_Y_2_2_at_pole[os_X_inp] == "X" or os_Y_2_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_2_2_pole[os_X_inp] != "■" and os_Y_2_2_pole[os_X_inp] !="X":
                os_Y_2_2_at_pole[os_X_inp] = "T"
                
        elif os_Y_inp == 3:
            if os_Y_3_2_pole[os_X_inp] == "■":
                os_Y_3_2_at_pole[os_X_inp] = "X"
            elif os_Y_3_2_at_pole[os_X_inp] == "X" or os_Y_3_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_3_2_pole[os_X_inp] != "■" and os_Y_3_2_pole[os_X_inp] !="X":
                os_Y_3_2_at_pole[os_X_inp] = "T"
                
        elif os_Y_inp == 4:
            if os_Y_4_2_pole[os_X_inp] == "■":
                os_Y_4_2_at_pole[os_X_inp] = "X"
            elif os_Y_4_2_at_pole[os_X_inp] == "X" or os_Y_4_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_4_2_pole[os_X_inp] != "■" and os_Y_4_2_pole[os_X_inp] !="X":
                os_Y_4_2_at_pole[os_X_inp] = "T"

        elif os_Y_inp == 5:
            if os_Y_5_2_pole[os_X_inp] == "■":
                os_Y_5_2_at_pole[os_X_inp] = "X"
            elif os_Y_5_2_at_pole[os_X_inp] == "X" or os_Y_5_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_5_2_pole[os_X_inp] != "■" and os_Y_5_2_pole[os_X_inp] !="X":
                os_Y_5_2_at_pole[os_X_inp] = "T"

        elif os_Y_inp == 6:
            if os_Y_6_2_pole[os_X_inp] == "■":
                os_Y_6_2_at_pole[os_X_inp] = "X"
            elif os_Y_6_2_at_pole[os_X_inp] == "X" or os_Y_6_2_at_pole[os_X_inp] == "T":
                print("Ход по точке был выполнен!")
                try:
                    os_Y_inp = int(input("Выберете строку для атаки: "))
                    os_X_inp = int(input("Выберете столбец для атаки: "))
                except ValueError:
                    print("Вводите пожалуйста числа, а не буквы!")
                except:
                    print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
                    ship_attack(os_Y_inp,os_X_inp)
            elif os_Y_6_2_pole[os_X_inp] != "■" and os_Y_6_2_pole[os_X_inp] !="X":
                os_Y_6_2_at_pole[os_X_inp] = "T"
                
        elif os_Y_inp > 6 or os_Y_inp < 0:
            print("Неверное задано значение, еще раз.")
    except IndexError:
        print("Вводите число в правильном диапазоне!")
    except:
        print("Что то пошло не так , убедитесь что вы вводили числа")
        
#Функция атаки ИИ
def ship_AI_attack(os_Y_inp,os_X_inp):
    if os_Y_inp == 1:
        if os_Y_1[os_X_inp] == "■":
            os_Y_1_at[os_X_inp] = "X"
        elif os_Y_1_at[os_X_inp] == "X" or os_Y_1_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_1[os_X_inp] != "■" and os_Y_1[os_X_inp] !="X":
            os_Y_1_at[os_X_inp] = "T"

        
    elif os_Y_inp == 2:
        if os_Y_2[os_X_inp] == "■":
            os_Y_2_at[os_X_inp] = "X"
        elif os_Y_2_at[os_X_inp] == "X" or os_Y_2_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_2[os_X_inp] != "■" and os_Y_2[os_X_inp] !="X":
            os_Y_2_at[os_X_inp] = "T"
            
    elif os_Y_inp == 3:
        if os_Y_3[os_X_inp] == "■":
            os_Y_3_at[os_X_inp] = "X"
        elif os_Y_3_at[os_X_inp] == "X" or os_Y_3_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_3[os_X_inp] != "■" and os_Y_3[os_X_inp] !="X":
            os_Y_3_at[os_X_inp] = "T"
            
    elif os_Y_inp == 4:
        if os_Y_4[os_X_inp] == "■":
            os_Y_4_at[os_X_inp] = "X"
        elif os_Y_4_at[os_X_inp] == "X" or os_Y_4_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_4[os_X_inp] != "■" and os_Y_4[os_X_inp] !="X":
            os_Y_4_at[os_X_inp] = "T"

    elif os_Y_inp == 5:
        if os_Y_5[os_X_inp] == "■":
            os_Y_5_at[os_X_inp] = "X"
        elif os_Y_5_at[os_X_inp] == "X" or os_Y_5_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_5[os_X_inp] != "■" and os_Y_5[os_X_inp] !="X":
            os_Y_5_at[os_X_inp] = "T"

    elif os_Y_inp == 6:
        if os_Y_6[os_X_inp] == "■":
            os_Y_6[os_X_inp] = "X"
        elif os_Y_6_at[os_X_inp] == "X" or os_Y_6_at[os_X_inp] == "T":
            os_Y_inp =  random.randrange(1,6)
            os_X_inp =  random.randrange(1,6)
            ship_AI_attack(os_Y_inp,os_X_inp)
        elif os_Y_6[os_X_inp] != "■" and os_Y_6[os_X_inp] !="X":
            os_Y_6_at[os_X_inp] = "T"

#Счетчики атаки
#Всего у нас 11 штук квадратов "■". Игра будет идти пока один из игроков не сведет количество "■" к нулю

lives_Hum = (os_Y_1_at.count("■")+os_Y_2_at.count("■")+os_Y_3_at.count("■")+os_Y_4_at.count("■")+os_Y_5_at.count("■")+os_Y_6_at.count("■"))
lives_AI = (os_Y_1_2_pole.count("■")+os_Y_2_2_pole.count("■")+os_Y_3_2_pole.count("■")+os_Y_4_2_pole.count("■")+os_Y_5_2_pole.count("■")+os_Y_6_2_pole.count("■"))

##Атака компьютера
while lives_Hum > 0 and lives_AI > 0:
    os_Y_inp = random.randrange(1,6)
    os_X_inp = random.randrange(1,6)

    ship_AI_attack(os_Y_inp,os_X_inp)
    
    print(os_X_0_at)
    print(os_Y_1_at)
    print(os_Y_2_at)
    print(os_Y_3_at)
    print(os_Y_4_at)
    print(os_Y_5_at)
    print(os_Y_6_at)
    
    lives_Hum = (os_Y_6_at.count("■")+os_Y_5_at.count("■")+os_Y_4_at.count("■")+os_Y_3_at.count("■")+os_Y_2_at.count("■")+os_Y_1_at.count("■"))
    while lives_Hum < 0:
        print("Компьютер победил!")
        break
##Атака игрока 
    try:
        os_Y_inp = int(input("Выберете строку для атаки: "))
        os_X_inp = int(input("Выберете столбец для атаки: "))
    except ValueError:
        print("Вводите пожалуйста числа, а не буквы!")
    except:
        print("Вводите числа в диапазоне от 1 до 6, убедитесь что вводите именно цифры")
    ship_attack(os_Y_inp,os_X_inp)
    
    print(os_X_0_2_at_pole)
    print(os_Y_1_2_at_pole)
    print(os_Y_2_2_at_pole)
    print(os_Y_3_2_at_pole)
    print(os_Y_4_2_at_pole)
    print(os_Y_5_2_at_pole)
    print(os_Y_6_2_at_pole)

    lives_AI = (os_Y_1_2_pole.count("■")+os_Y_2_2_pole.count("■")+os_Y_3_2_pole.count("■")+os_Y_4_2_pole.count("■")+os_Y_5_2_pole.count("■")+os_Y_6_2_pole.count("■"))
    while lives_AI <= 0:
        print("Игрок победил!")
        break
