class Eleve:

    def __init__(self, d_name,d_level,d_age=2):
        self.name = d_name
        self.age = d_age
        self.grade = 0
        self.level = d_level

    def add_grade(self, grade):
        self.grade += grade

    def sub_grade(self, grade):
        self.grade -= grade
        if self.grade < 0:
            self.grade = 0

eleve1 = Eleve(d_name="Assi", d_level=1, d_age=10)
eleve2 = Eleve(d_name="Babs", d_level="CM2")

print(eleve1.name, eleve1.age, eleve1.grade, eleve1.level)  # Output: Assi 0 0 1
print(eleve2.name, eleve2.age, eleve2.grade, eleve2.level)  # Output: Babs 0 0 CM2

eleve1.add_grade(3)
eleve2.add_grade(13)
eleve2.sub_grade(2)

print(eleve1.name, eleve1.age, eleve1.grade, eleve1.level)  # Output: Assi 0 0 1
print(eleve2.name, eleve2.age, eleve2.grade, eleve2.level)  # Output: Babs 0 0 CM2

