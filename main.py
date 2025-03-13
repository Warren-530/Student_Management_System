import time

from Student import Student

print("Loading the data from students.txt", flush=True)
time.sleep(1)
print("Data loaded successfully!")
Student.read()
while True:
    print(
        """Operations used,

    1.Accept Student details
    2.Display Student Details
    3.Search Details of a Student
    4.Delete Details of Student
    5.Update Student Details
    6.Save Records to File
    7.Exit"""
    )

    opt = input("Enter your operation: ")
    print()
    match (opt):
        case "1":
            name = input("Name? ")
            rn = input("RollNo? ")
            m1 = input("Mark1? ")
            m2 = input("Mark2? ")
            student = Student(name, rn, m1, m2)
            print("Student list:")
            student.add()
            print("Student details added sucessfully!\n")

        case "2":
            Student.display()
            print("\nStudent details displayed successfully!\n")

        case "3":
            rn = input("Enter RollNo to be searched: ")
            found = Student.search(rn)
            if found:
                print("Student details has been searched!\n")
            else:
                print("Student details not found!!!")

        case "4":
            rn = input("Enter RollNo to be deleted: ")
            Student.delete(rn)
            print("Student details deleted successfully!\n")

        case "5":
            rn = input("Enter RollNo to be updated: ")
            newrn = input("Enter the new RollNo: ")
            found = Student.update(rn, newrn)
            if found:
                print("Student details updated successfully!\n")
            else:
                print("Student details not found!!!")

        case "6":
            Student.savefile()
            print("Students details saved successfully!")

        case "7":
            print("Thank you!\n")
            break
