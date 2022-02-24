#задание 1
class Date:
    def __init__(self, string):
        self.date = string

    @classmethod
    def date_to_int(cls, obj):
        return obj.date.split('-')

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

a = Date('09-02-1996')
print(Date.date_to_int(a))

#задание 2 (не получилось реализовать, мои мысли по этому заданию)
class Number:
    def __init__(self):
        num_1 = input('Введите первое число:')
        num_2  = input('Введите второе число:')
        if num_1 or num_2 > 0:
            return (num_1 / num_2)
        else:
            return (f"Деление на ноль недопустимо")

num = Number()
print(num())

#задание 3
class NotNumber(ValueError):
    pass

my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не число!', ex)
print(my_list)


#задание 4, 5, 6
from datetime import datetime

class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self,t]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number) +', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))

    def give_to_depot(self, equipment, other):
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)

    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))

class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)

class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)


store1 = Depot('Main warehouse')
store2 = Depot('Small warehouse')
a = Printer('HP',345678,100)
b = Scanner('Epson',123456,4000)


print(a)
print(b)


store1.take_to_depot(a)
store1.take_to_depot(b)


store1.give_to_depot(a,store2)

store1.list_equipments()
store2.list_equipments()

#задание 7

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)



