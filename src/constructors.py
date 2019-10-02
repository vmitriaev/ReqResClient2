def error_constructor(message):
    '''Вывод сообщения об ошибке'''
    errorMessage = ('ERROR: ' + message)
    lines = '-' * len(errorMessage)
    return '\n' + lines + '\n' + errorMessage + '\n' + lines + '\n'

def counter(count):
    '''Запоминает количество'''
    return count

r = counter(input('Введи число, а я запомню! Число: '))
print('Ага! Твое число: ' + str(r))