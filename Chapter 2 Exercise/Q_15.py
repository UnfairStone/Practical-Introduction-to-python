print('Exercise 15')

aheight = eval(input('Please state how high you would like your A to be: '))
awidth = eval(input('Please state how wide you would like your A to be: '))
topa = int(aheight*0.25)
bottoma = int(aheight*0.5)

#Top of Letter 'A'
print('*'*awidth)

for i in range(topa):
    print('*',' '*(awidth-2),'*',sep='')

print('*'*awidth)

#Bottom of Letter 'A'

for i in range(bottoma):
    print('*',' '*(awidth-2),'*',sep='')


