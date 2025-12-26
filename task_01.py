# dictionary with student name and marks
students={
    "Alen":{"English":75,"Maths":65,"Physics":68},
    "Chethas":{"English":88,"Maths":72,"Physics":81},
    "Arjun":{"English":65,"Maths":57,"Physics":59},
}
def fetch_marks(students_data,student_name):
    try:
        if not isinstance(students_data,dict):
            raise TypeError("Students data must be a dictionary")
        if not isinstance(student_name,str):
            raise TypeError("Student name must be a string")
        if student_name not in students_data:
            raise KeyError(f"Student '{student_name}' not exist")

        return students_data[student_name]
    except (KeyError,TypeError) as error:
        print(f"Error:{error}")




try:
    user_input=input("Enter Student's name: ")
    marks=fetch_marks(students,user_input)
    if marks:
        print(f"Marks of {user_input}:")
        for key,val in marks.items():
            print(f"{key}={val}")
    else:
        print()
except (KeyError,TypeError,Exception) as err:
    print(f"Something went wrong:{err}")














