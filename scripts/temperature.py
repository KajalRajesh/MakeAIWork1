temp = eval(input('The temperature is :'))
f_temp = ((9/5)*temp)+32
print(f'In fahrenheit, that is {f_temp}', '.')
if f_temp > 212:
    print('The temperature is so high')
else:
    print('The temperature is low')