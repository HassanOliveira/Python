from unidecode import unidecode

start = str(unidecode(input('Enter departure city: ')))
final = str(unidecode(input('Enter the final city: ')))
city = str(unidecode(input('Enter a stop city or "exit" to not add: ')))

citys = []
i = 0


def string_manipulation(string):
    manipulated_string = string.lower()
    manipulated_string = string.title()
    return citys.append(manipulated_string)

start = string_manipulation(start)

while city != 'exit':
    string_manipulation(city)
    i = i + 1
    city = str(unidecode(input('Enter a stop city or "exit" to not add: ')))


final = string_manipulation(final)