# Напишите программу, принимающую на вход целое число, которая выводит True,
#  если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False
#   в противном случае (регистр символов имеет значение).

# Обратите внимание на разные скобки, используемые для обозначения интервалов.
#  В задании используются полуоткрытые и открытые интервалы. Подробнее про это 
#  вы можете прочитать, например, на википедии (полуинтервал, промежуток).

# Sample Input 1:

# 20
# Sample Output 1:

# True
# Sample Input 2:

# -20
# Sample Output 2:

# False




a = int(input())

if (-15 < a <= 12) or (14 < a < 17) or (19 <= a < float('+inf')):
	print ('True')
else:
	print ('False')



#
# n = int(input())
# print(-15 < n <= 12 or 14 < n < 17 or 19 <= n)



#
# n = int(input())
# print( (n in range(-14, 13)) or (n in range(15, 17)) or (n >= 19) )


#
# x=int(input())
# print(x > -15 and not (x in [13, 14, 17, 18]))


#
# print((lambda x: -15 < x <= 12 or 14 < x < 17 or x >= 19)(int(input())))



#
# exec("print( -15<{0}<=12 or 14<{0}<17 or {0}>=19 )".format(int(input())))