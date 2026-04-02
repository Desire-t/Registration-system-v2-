

def get_grade(average):
    
    if average >= 13:
        grade = "A"
    elif average >= 11.5:
        grade = "B"
    elif average >= 10:
        grade = "C"
    else:
        grade = "D"
    return grade