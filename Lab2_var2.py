class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_income(self):
        # Метод возвращает средний доход
        pass

    def get_expenses(self):
        # Метод возвращает средние расходы
        pass

class Preschooler(Person):
    def __init__(self, name, age, gender, hobbies):
        super().__init__(name, age, gender)
        self.hobbies = hobbies

    def get_income(self):
        return 0

    def get_expenses(self):
        return 2000

class Schoolboy(Person):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def get_income(self):
        return 1000

    def get_expenses(self):
        return 3000

class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major

    def get_income(self):
        return 5000

    def get_expenses(self):
        return 8000

class Worker(Person):
    def __init__(self, name, age, gender, job):
        super().__init__(name, age, gender)
        self.job = job

    def get_income(self):
        return 30000

    def get_expenses(self):
        return 25000

# Для демонстрации работы программы, предлагаю пользователю выбрать тип объекта для демонстрации.
print("Выберите тип объекта для демонстрации:")
print("1 - Дошкольник")
print("2 - Школьник")
print("3 - Студент")
print("4 - Работающий")

# Считываем выбор пользователя
choice = input("Введите номер объекта: ")

if choice == '1':
    p = Preschooler("Иван", 5, "мужской", ["рисование", "музыка"])
    print("Средний доход дошкольника: ", p.get_income())
    print("Средние расходы дошкольника: ", p.get_expenses())
elif choice == '2':
    p = Schoolboy("Петр", 12, "мужской", 6)
    print("Средний доход школьника: ", p.get_income())
    print("Средние расходы школьника: ", p.get_expenses())
elif choice == '3':
    p = Student("Ольга", 20, "женский", "Программист")
    print("Средний доход студента: ", p.get_income())
    print("Средние расходы студента: ", p.get_expenses())
elif choice == '4':
    p = Worker("Сергей", 35, "мужской", "IT-специалист")
    print("Средний доход работающего: ", p.get_income())
    print("Средние расходы работающего: ", p.get_expenses())
else:
    print("Некорректный выбор.")