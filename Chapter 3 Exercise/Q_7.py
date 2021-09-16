print('Question 7')

angle = eval(input('Please select an angle between -180 and 180 degrees: '))
angle360 = (180+angle)%360
print('Your degree amount converted into its 360 degree equivalent is: ',angle360)
