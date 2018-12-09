# В Институте биоинформатики между информатиками и биологами устраивается соревнование.
# Победителям соревнования достанется большой и вкусный пирог. В команде биологов a 
# человек, а в команде информатиков — b человек.

# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога
#  любой команде, выигравшей соревнование, при этом каждому участнику этой команды 
#  должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог
#  а слишком мелкие кусочки, нужно найти минимальное подходящее число.

# Напишите программу, которая помогает найти это число. 
# Программа должна считывать размеры команд (два положительных целых числа a и b, 
# 	каждое число вводится на отдельной строке) и выводить наименьшее число d, 
# которое делится на оба этих числа без остатка.

# Sample Input 1:

# 7
# 5
# Sample Output 1:

# 35
# Sample Input 2:

# 15
# 15
# Sample Output 2:

# 15
# Sample Input 3:

# 12
# 16
# Sample Output 3:

# 48



a = int(input())
b = int(input())
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)




#
# a = int(input())
# b = int(input())
# d = a
# while d%b:
#     d += a
# print(d)



#
# a = int(input())
# b = int(input())
# if   a > b:
#       p = a
#       while p % b != 0: p += a
# elif a < b:
#       p = b
#       while p % a != 0: p += b
# else: p = a
# print (p)


#
# a = int(input())
# b = int(input())
# x = a

# while (x % a != 0) or (x % b != 0):
#     x += 1
# print(x)



#
# a,b=int(input()),int(input())
# ab=a*b
# while b!=0:
#     a,b=b,a%b
# out=ab//a
# print(out)



#
# a=int(input())
# b=int(input())
# m=a
# if a==b:   # если оба значения (a и b) равны, выводим сразу это значение, и программа завершается.   
#   print(m)
#            # иначе, при помощи цикла, прибавляем к одному из значений(a или b) его же значение,
# else:      # а+а+... или b+b+...до тех пор, пока сумма не будет кратной введенным значениям a и b 
#   while m%a!=0 or m%b!=0: # ТАКОЙ способ позволяет не прерывать цикл. Ниже пояснение.
#     m=m+a
#   print(m)

     # конструкция m%a!=0 or m%b!=0 - позволяет производить цикл до момента, когда оба условия одновременно
     # станут False. Потому что помним(!!!), что цикл While работает только когда условие в нем True, если 
     # становится False, то блок While перестает работать.
        
     # То есть, знаем что or - это суммирование(0+0=0, 0+1=1, 1+1=1), and - это умножение (0*0=0, 0*1=0, 1*1=1), 
     # not - просто меняет значение на противоположное. В нашем примере у нас or. 
     # Возвращаясь к нашему примеру m%a!=0 or m%b!=0, когда находится общее минимальное делимое число, то? 
     # результат в условие станет следующий - False и False, то есть, False+False, плюсуем потому что or(помним) 
     # а значит 0+0=0, а ноль это False, при котором циклл While прекращает свою работу.
     # А пока он дошел до этого момента, он пербирал, к примеру, такие варианты, 
     # как False+True=True, True+False=True, при которых цикл продолжал работать, потому как True.