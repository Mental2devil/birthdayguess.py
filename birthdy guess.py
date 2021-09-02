b=0
c1 = "Is your birthday is present in Set1?\n" + \
"1 3  5   7\n" + \
"9 11 13 15\n" + \
"17 19 21 23\n" + \
"25 27 29 31\n" + \
"\n Enter 0 for No and 1 for Yes:"
a = int(input(c1))
if a==1:
 b+=1
c2 = "Is your birthday is present in Set2?\n" +\
"2  3  6  7\n"  + \
"10 11 14 15\n" + \
"18 19 22 23\n" + \
"26 27 30 31\n" + \
"\n Enter 0 for No and 1 for Yes:"
a = int(input(c2))

if a==1:
 b+=2

c3 = "Is your birthday is present in Set3?\n" + \
" 4 5  6  7\n" + \
"12 13 14 15\n" + \
"20 21 22 23\n" + \
"28 29 30 31\n" + \
"\n Enter 0 for No and 1 for Yes:"
a = int(input(c3))

if a==1:
 b+=4

c4 = "Is your birthday is present in Set4?\n" + \
" 8 9  10  11\n" + \
"12 13 14  15\n" + \
"24 25 26  27\n" + \
"28 29 30  31\n" + \
"\n Enter 0 for No and 1 for Yes:"
a = int(input(c4))

if a==1:
 b+=8

c5 = "Is your birthday is present in Set5?\n" + \
"16 17 18 19\n" + \
"20 21 22 23\n" + \
"24 25 26 27\n" + \
"28 29 30 31\n" + \
"\n Enter 0 for No and 1 for Yes:"
a = int(input(c5))


if a==1:
 b+=16
print("your brithday is on ",b)
