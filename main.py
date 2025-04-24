class GroupFullException(Exception):
    def __init__(self, message="Группа начисливает 10 студентов"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} age"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, test: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            return
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group: {self.number}\n{all_students}'


gr = Group('PD1')

for i in range(10):
    try:
        student = Student('Male', 20+i, f'Name{i}', f'LastName{i}', f'RB{i}')
        gr.add_student(student)
    except GroupFullException as e:
        print(f"Нельзя добавлять больше 10ти студентов {i}: {e}")

print(gr)