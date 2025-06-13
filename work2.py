from datetime import datetime

class Romana:
    def __init__(self, name=None, surname=None, year_of_birth=None):
        self.first_name = name
        self.last_name = surname
        self.birth_year = year_of_birth
        self._course = None

    def calculate_course(self):
        if self.birth_year is None:
            return "Рік народження не вказано"

        start_college_age = 15
        current_year = datetime.now().year
        start_year = self.birth_year + start_college_age
        self._course = current_year - start_year

        if self._course < 1:
            return "Ще не студент"
        elif self._course > 4:
            return "Навчання завершене"
        return self._course

    def get_name_parts(self):
        return [self.first_name, self.last_name]


class StudentRomana(Romana):
    def __init__(self, name=None, surname=None, year_of_birth=None,
                 program=None, group_code=None, avg_grade=None):
        super().__init__(name, surname, year_of_birth)
        self.program = program
        self.group_code = group_code
        self.__avg_grade = avg_grade

    def __eligible_for_scholarship(self):
        if self.__avg_grade is None:
            return "Оцінку не вказано"
        return self.__avg_grade >= 8.0

    def scholarship_status(self):
        if self.__eligible_for_scholarship() == True:
            return f"{self.first_name} має стипендію"
        elif self.__eligible_for_scholarship() == False:
            return f"{self.first_name} не має стипендії"
        else:
            return "Неможливо визначити статус стипендії"

    def show_full_info(self):
        return (
            f"{self.first_name} {self.last_name}, "
            f"курс: {self.calculate_course()}, "
            f"група: {self.group_code}, "
            f"спеціальність: {self.program}"
        )


# Тестування
student = StudentRomana("Романа", "Мухамадієва", 2008, "ICT", "22", 9.1)

print("Курс:", student.calculate_course())
print("Ім'я та прізвище:", student.get_name_parts())
print("Стипендія:", student.scholarship_status())
print("Повна інформація:", student.show_full_info())
