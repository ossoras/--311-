# -*- coding: utf-8 -*-
"""лаба 1(лавицкий)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ocCcGm-7luQXSR0YDno2ngTjYva-Z0Jp
"""

a=5
b=int(input())
print('1)',a*b)

a=int(input())
b=int(input())
print('2)',(a+b)**2)

a=15
c=int(input())
b=10
print('3)',(a+b)//c)

a=int(input())
b=int(input())
print('4)',a**2+2*a*b+b*2)

a=int(input())
b=int(input())
с=int(input())
print('5)','s=',a*b//2,'    ','p=',a+b+c

a=int(input())
b=int(input())
print('6)',((a**3 + 14)//5)* b)

a=int(input())
n=int(input())
print('7)',a**2//n)

a=float(input())
b=float(input())
print('1)',a//b)
a=int(input())
b=int(input())
print('2)',a*b)
a=int(input())
b=int(input())
print('3)',a%b)

n=int(input())
if n>=86400:
  den=n//86400
  n=n%86400
if n>=3600:
  chas=n//3600
  n=n%3600
if n>60:
  min=n//60
print('дни)',den,',часы)',chas,',минутки)',min,'༼ つ ◕_◕ ༽つ')

n=(input())
a=int(n)+int(n+n)+int(n+n+n)
print(a,'(づ￣ ³￣)づ')