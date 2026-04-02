# search

import csv
import os
from ui.input import get_student_name_for_search

def search_student_by_matricule():
    is_student = os.path.exists("student_data.csv")
    if not is_student:
        print("No database found")
        return
    attempt = 4
    while attempt >0:
        matricule = get_student_name_for_search()
        with open("student_data.csv", "r") as file:
            reader =csv.reader(file)
            for row in reader:
                if matricule ==row[1]:
                    print(row)
                    found = True
                    return
                
            if not found:
                    attempt -=1
                    print("\nStudent not found")
                    print(f"You have {attempt} attempt left")
                    
search_student_by_matricule()

# sort

import os
import csv
def sort_student_by_name():
    is_file_found = os.path.exists("student_data.csv")

    if not is_file_found:
            print("File not found")
            return
    with open("student_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
        sorted_students = sorted(data, key=lambda sor: sor[0])
        for s in sorted_students:
            print(s)



#view

import os
import csv
def View_all_students():
    is_file_found = os.path.exists("student_data.csv")
    
    if not is_file_found:
        print("No databse file found.")
        return
    
    with open("student_data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        for student in data:
            print(student)

