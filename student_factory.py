from student import Student
from repository.model import StudentModel

class StudentFactory:
    @staticmethod
    def student_from_payload(payload):
        return StudentModel(roll_no=payload["roll_no"], name=payload["name"]) 

    @staticmethod
    def student_list_from_payload(payload):
        return [StudentFactory.student_from_payload(student) for student in payload]

    @staticmethod
    def non_orm_student_from_payload(payload):
        return Student(payload["roll_no"],payload["name"])
        

    @staticmethod
    def student_from_db(item):
        return Student(item.roll_no, item.name)

    @staticmethod
    def student_list_from_db(item_list):
        return [StudentFactory.student_from_db(item) for item in item_list]
