import os


class Student:
    studList = []

    def __init__(self, name, rollNo, m1, m2):
        self.name = name
        self.rollNo = rollNo
        self.m1 = m1
        self.m2 = m2

    def add(self):
        Student.studList.append(self)

    @staticmethod
    def display():
        c = 1
        for x in Student.studList:
            print(c, "...............")
            print("Name:", x.name)
            print("RollNo:", x.rollNo)
            print("Mark1:", x.m1)
            print("Mark2:", x.m2)
            print()
            c = c + 1

    @staticmethod
    def search(rollNo):
        found = False
        for x in Student.studList:
            if x.rollNo == rollNo:
                print("Name:", x.name)
                print("RollNo:", x.rollNo)
                print("Mark1:", x.m1)
                print("Mark2:", x.m2)
                print()
                found = True
        return found

    @staticmethod
    def delete(rollNo):
        Student.studList = [x for x in Student.studList if x.rollNo != rollNo]

    @staticmethod
    def update(rollNo, newRollNo):
        found = False
        for x in Student.studList:
            if x.rollNo == rollNo:
                x.rollNo = newRollNo
                found = True
        return found

    @staticmethod
    def read():
        if not os.path.exists("students.txt"):
            f = open("students.txt", "x")
            f.close()
        Student.studList.clear()
        line_count = 0
        with open("students.txt", "r") as file:
            line_count = sum(1 for line in file)

        f = open("students.txt", "r")
        for x in range(line_count):
            text = f.readline().strip()
            ls = text.split(",")
            stud = Student(ls[0], ls[1], ls[2], ls[3])
            Student.studList.append(stud)
        f.close()

    @staticmethod
    def savefile():
        if not os.path.exists("students.txt"):
            f = open("students.txt", "x")
            f.close()

        f = open("students.txt", "w")
        for x in Student.studList:
            f.write(f"{x.name},{x.rollNo},{x.m1},{x.m2}\n")
        f.close()
