
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def to_dict(self):
        return {"roll_no": self.roll_no, "name": self.name}
