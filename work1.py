from datetime import datetime

class Romana:
    def __init__(self, name=None, surname=None, year_of_birth=None):
        self._info = {
            'name': name,
            'surname': surname,
            'year_of_birth': year_of_birth
        }

    def get_course(self):
        birth_year = self._info['year_of_birth']
        if birth_year is None:
            return "Рік народження не вказано"

        start_age = 15
        current_year = datetime.now().year
        course = current_year - (birth_year + start_age)

        if course < 1:
            return "Ще не студент"
        elif course > 4:
            return "College completed"
        return course

    def fullname_list(self):
        return [self._info['name'], self._info['surname']]

# Приклад використання
student = Romana("Романа", "Мухамадієва", 2008)
print("Курс:", student.get_course())
print("Ім'я та прізвище:", student.fullname_list())
