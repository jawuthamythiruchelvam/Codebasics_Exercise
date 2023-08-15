class Teacher:
    def teacher_action(self):
        print("i can teach")
class Engineer:
    def engineer_action(self):
        print("i can code")

class Youtuber:
    def youtuber_action(self):
        print("i can make videos")
class person(Teacher,Engineer,Youtuber):
    pass

o=person()
o.teacher_action()
o.engineer_action()
o.youtuber_action()
