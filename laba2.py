import os
import itertools

array_of_line = []           # массив для работы со строкой
array_of_beginning = []      # массив для запоминания начала последоватльностей
array_of_repetition = []     # массив для запоминания последовательности
sequence_len = 0             # длина самой длинной последовательности
beginning = 0                # начало последовательности
sequence = 0                 # сама последовательность
len_ser = 1                  # промежуточная переменная

print ('---------- Результат работы программы ----------')
try:
    with open("text.txt", "r") as file_to_work :     # открываем файл
        for line in file_to_work :                   # читаем построчно
            array_of_line = list(line)
            if not array_of_line:                    # проверка пустой файл или нет
                 print('\nФайл text.txt пустой.')
            else:
                for i in range (len(array_of_line) - 1):
                    if (array_of_line[i] >= '0') and (array_of_line[i] <= '9') :
                        if array_of_line[i-1] == array_of_line[i]:
                            len_ser += 1
                            array_of_beginning.append(i)
                            array_of_repetition.append(array_of_line[i])
                            if  len_ser > sequence_len:
                                sequence_len = len_ser
                                beginning = array_of_beginning[0]
                                if sequence_len != len(array_of_repetition):
                                    array_of_repetition.append(array_of_repetition[0])
                                else:
                                    sequence = ''.join(array_of_repetition)
                        else:
                            len_ser = 1
                            array_of_beginning.clear()
                            array_of_repetition.clear()
        if sequence == 0:        
            print('Файл не содержит цифр, добавьте или измените файл.')
        else:
            print ('Самая длинная последовательность - ', sequence)
            print ('Длина последовательности - ', sequence_len)
            print ('Позиция с которой началась последовательность - ', beginning)

                        
except FileNotFoundError:                             # исключаем ошибку 'файл не найден'
  print ("\nФайл в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
