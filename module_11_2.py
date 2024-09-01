# -*- coding: utf-8 -*-
import inspect
import pprint

def introspection_info(obj):
    # Тип объекта
    obj_type = type(obj).__name__

    # Модуль
    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'Built-in'

    # Атрибуты и методы
    obj_dir = dir(obj)

    # Разделение атрибуты и методы
    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr))]
    methods = [method for method in obj_dir if callable(getattr(obj, method))]

    # Результат словарём
    introspection_result = {
        'type': obj_type,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods
    }

    return  introspection_result


# Пример работы:
number_info = introspection_info(42)
pprint.pprint(number_info)
print('\n # *********************************************** \n' )

# ***********************************************

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greed(self):
        return f"Привет, меня зовут {self.name} и мне {self.age} лет(года)"

person = Person("Александр", 30)

person_info = introspection_info(person)
pprint.pprint(person_info)