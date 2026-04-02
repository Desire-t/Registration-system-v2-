import csv
import os
def save_data():
    name = "tam".title()
    age = 11
    is_file = os.path.exists("student_data.csv")
    with open("student_data.csv", "a", newline="") as file:
        writer =csv.writer(file)
        if not is_file:
            writer.writerow(["Name", "Age"])
            print("File does not exist. I Created a new file automaticaly")
        writer.writerow([name, age])
        print("Saved succesfuly")
save_data()