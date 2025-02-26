class Vehicle:
    __COLOR_VARIANTS = ['Веселенький','Шершавенький','розовастенький','грустный']
    def __init__(self,owner,model,engine_power,color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        print(f'Модель:{self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя:{self.__engine_power}')
    def get_color(self):
        print(f'Цвет:{self.__color}')
    def get_owner(self):
        print(f'Владелец:{self.owner}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        self.get_owner()
    def set_color(self,new_color):
        self.new_color = new_color
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
                return self.__color
            else:
                continue
        print(f'Нельзя сменить цвет на {self.new_color}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Веселенький','Шершавенький','розовастенький','грустный']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('ШЕРШАВЕНЬКИЙ')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()