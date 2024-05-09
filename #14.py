# переопределяем только __str__, показывая человеко-читаемое строковое представление объекта,
# __repr__ оставляем дефолтным, в котором будет показан тип объекта и его адрес.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Марка: {self.brand}   Модель: {self.model}'

car = Car('VW', 'Passat')
print(car)  # выведет: 'Марка: VW   Модель: Passat'
print(repr(car)) # выведет тип объекта и его адрес