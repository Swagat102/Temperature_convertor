celsius = float(input('Enter the temperature:'))
fahrenheit = (celsius*1.8) + 32
#print(celsius, 'degree celsius is equal to', fahrenheit, 'degrees fahrenheit')
print('%0.1f degree celsius is equal to %0.1f degree fahrenheit' %(celsius,fahrenheit))

temperature=fahrenheit

if temperature > 104:
    print('The weather is hot')
elif temperature < 54:
    print('The weather is too cold')
else:
    print('The weather is quite pleasant')