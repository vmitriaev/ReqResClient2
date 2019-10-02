# ReqResClient2

Конструкторы:
request_constructor
endpoint_constructor
body_constructor
error_constructor
counter
response_constructor
sender
dict_constructor

endpoint_constructor
1. какой сервис?
2. какой метод? если get, то какие параметры передать в url?
на выходе: готовый url запроса с методом

body_constructor
1. что передать?
на выходе: готовый json запроса

counter
1. сколько раз вызвать?
на выходе: количество обращений к сервису

request_constructor
1. вызов counter - запоминает сколько обращений - создает список, в который последовательно добавляются url и body
2. вызов endpoint_constructor - формирует url запроса
3. вызов body_constructor - формирует тело запроса (если метод get или delete, то формирует пустое тело)
на выходе: список запросов в виде словаря

sender
1. последовательная отправка запросов согласно полученному словарю request_constructor
на выходе: последовательный список ответов в виде словаря, который содержит:
status_code
error_code
time (ms)
response_body 

response_constructor
1. последовательное преобразование словаря sender в читаемый красивый вид
на выходе: ответы на отправленные запросы

error_constructor
на выходе: обрабатывает ошибку и выводит на экран

dict_constructor
на выходе: абстрактный словарь


Модули:
main
constructors

main
основной интерфейс клиента, отсюда запускается request_constructor, сюда приходит результат от response_constructor