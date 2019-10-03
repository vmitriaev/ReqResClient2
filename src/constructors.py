def error_constructor(message):
    '''Вывод сообщения об ошибке'''
    errorMessage = ('ERROR: ' + message)
    lines = '-' * len(errorMessage)
    return '\n' + lines + '\n' + errorMessage + '\n' + lines + '\n'


def counter(count):
    '''Запоминает количество'''
    return count


def low_maker(text):
    lower_text = str(text).lower()
    return lower_text


def endpoint_constructor():
    '''Собирает url запроса'''
    default_url = 'https://reqres.in/api/'
    question_s = input(
        'К какому сервису запрос?' + '\n' + 'Список сервисов: users, unknown, register, login.' + '\n' + 'Значение: ')
    service = low_maker(question_s)
    if service in ('users', 'unknown', 'register', 'login'):
        question_m = input(
            'Какой метод запроса?' + '\n' + 'Список сервисов: get, post, put, patch, delete.' + '\n' + 'Значение: ')
        method = low_maker(question_m)
        if method in ('get', 'put', 'patch', 'delete'):
            if service == 'users':
                if method == 'get':
                    question__m_g = input(
                        'Можно запросить: user_list, single_user, delayed_response.' + '\n' + 'Значение: ')
                    value_m_g = low_maker(question__m_g)
                    if value_m_g == 'user_list':
                        value_user_list = input('Какой номер страницы? Цифра или число: ')
                        if int(value_user_list) > 0:
                            endpoint = default_url + service + '?page=' + str(value_user_list)
                            return endpoint
                        else:
                            return error_constructor('номер страницы может быть только положительным целым числом!')
                    elif value_m_g == 'single_user':
                        value_single_user = input('Какой номер пользователя? Цифра или число: ')
                        if int(value_single_user) > 0:
                            endpoint = default_url + service + '/' + str(value_single_user)
                            return endpoint
                        else:
                            return error_constructor('номер пользователя может быть только положительным целым числом!')
                    elif value_m_g == 'delayed_response':
                        value_delayed_response = input('Какую задержку (сек) ставить? Цифра или число: ')
                        if int(value_delayed_response) > 0:
                            endpoint = default_url + service + '?delay=' + str(value_delayed_response)
                            return endpoint
                        else:
                            return error_constructor('задержка может быть только положительным целым числом!')
                elif method == 'put':
                    question_m_p = input('Данные какого пользователя апдейтим? Цифра или число: ')
                    if int(question_m_p) > 0:
                        endpoint = default_url + service + '/' + question_m_p
                        return endpoint
                    else:
                        return error_constructor('номер пользователя может быть только положительным целым числом!')
                elif method == 'patch':
                    question_m_p = input('Данные какого пользователя апдейтим? Цифра или число: ')
                    if int(question_m_p) > 0:
                        endpoint = default_url + service + '/' + question_m_p
                        return endpoint
                    else:
                        return error_constructor('номер пользователя может быть только положительным целым числом!')
                elif method == 'delete':
                    question_m_d = input('Данные какого пользователя удаляем? Цифра или число: ')
                    if int(question_m_d) > 0:
                        endpoint = default_url + service + '/' + question_m_d
                        return endpoint
                    else:
                        return error_constructor('номер пользователя может быть только положительным целым числом!')
                else:
                    return
            elif service == 'unknown':
                if method == 'get':
                    question_m_g = input('Можно запросить: resource_list, resource_single.' + '\n' + 'Значение: ')
                    value_m_g = low_maker(question_m_g)
                    if value_m_g == 'resource_list':
                        endpoint = default_url + service
                        return endpoint
                    elif value_m_g == 'resource_single':
                        value_resource_single = input('Какой номер? Цифра или число: ')
                        if int(value_resource_single) > 0:
                            endpoint = default_url + service + '/' + str(value_resource_single)
                            return endpoint
                        else:
                            return error_constructor('номер может быть только положительным целым числом!')
                    else:
                        return error_constructor('некорректное значение!')
            else:
                return error_constructor(
                    'метод ' + str(method.upper()) + ' не поддерживается для сервиса ' + str(service.upper()))
        elif method == 'post':
            endpoint = default_url + service
            return endpoint
        else:
            return error_constructor('wrong method ' + str(method).upper())
    else:
        return error_constructor('wrong service ' + str(service).upper())


print(endpoint_constructor())
