class CarPark:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self.max):
            return self.max
            self.n += 1
        raise StopIteration




# Создаем объект
auto = CarPark(max)

max = ['VW', 'BMW', 'Honda']


# Создаем итератор из объекта
i = iter(max)


# Используем next для перехода к следующему элементу итератора

print(next(i))
print(next(i))
print(next(i))

#print(next(i)) # генерируется исключение StopIteration