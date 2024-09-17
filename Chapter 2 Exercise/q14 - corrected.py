print('Exercise 14')

diamond =  eval(input('Please state how tall your triangle must be - select an odd number: '))
diamondtip = int(diamond*0.5)

for i in range(diamondtip):
    print('*'*((i+1)+i))

print('*'*(diamond))
    
for i in range(diamondtip):
    print('*'*(diamond-((i+1)+(i+1))))
