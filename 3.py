class House:
    def __init__(self, address, floor, rooms, square):
        self.address = address
        self.floor = floor
        self.rooms = rooms
        self.square = float(square)  # Преобразуем площадь в число

    def print_info(self):
        print(f'Адрес: {self.address}\nЭтаж: {self.floor}\nКоличество комнат: {self.rooms}\nПлощадь: {self.square}')


house_1 = House('ул. Пушкина 10', '2', '3', '85.5')
house_2 = House('ул. Лермонтова 5', '5', '2', '65.2')
house_3 = House('ул. Толстого 15', '8', '4', '120.3')

house_1.print_info()
house_2.print_info()
house_3.print_info()

houses = [house_1, house_2, house_3]
desired_square = 100.0

for house in houses:
    if house.square > desired_square:
        house.print_info()