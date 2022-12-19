import random

class Person:
    """
        Класс человека. Описывает человека именем, фамилией и возрастом.
    """
    def __init__(self, name: str, surname: str, age: int):
        """
        Инициализация человека.
        """
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Сотрудник {self.__name} {self.__surname}.'

    @staticmethod
    def generate_person():
        """
        Конструктор человека.
        """
        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(20, 80)
        return name, surname, age


class Employee(Person):
    """
        Класс работника. Родитель: Person
    """
    def calc_salary(self):
        """
        метод для расчета з/п. переопределен в каждом из производных классов.
        """
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f' Должность: {self.__class__.__name__}. Зарплата: {self.calc_salary()}'


class Manager(Employee):
    """
    Класс менеджера. Родитель: Employee
    """
    def calc_salary(self):
        """
        Расчет з/п менеджера.
        :return: фиксированная з/п менеджера (13000)
        """
        return 13000


class Agent(Employee):
    """
    Класс агента. Родитель: Employee
    """
    def __init__(self, name: str, surname: str, age: int, sales: int):
        super().__init__(name, surname, age)
        self.__sales = sales

    def calc_salary(self):
        return 5000 + 0.05 * self.__sales


class Worker(Employee):
    """
    Класс рабочего. Родитель: Employee
    """
    def __init__(self, name: str, surname: str, age: int, hours: int):
        super().__init__(name, surname, age)
        self.__hours = hours

    def calc_salary(self):
        return 100 * self.__hours


names = ['Пудж', 'Шадоу', 'Нейчерс', 'Эеарч']
surnames = ['Потанцевал', 'Финд', 'Профет', 'Спирит']

employees = list()

for _ in range(3):
    employees.append(Manager(*Person.generate_person()))

for _ in range(3):
    agent = Agent(*Person.generate_person(), random.randint(2000, 10000))
    employees.append(agent)

for _ in range(3):
    worker = Worker(*Person.generate_person(), random.randint(20, 50))
    employees.append(worker)

for employee in employees:
    print(employee)