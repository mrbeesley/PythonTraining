from student import *

class HighSchoolStudent(Student):

    school_name = "Quinter High School"

    def get_school_name(self):
        return "this is a high school student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"