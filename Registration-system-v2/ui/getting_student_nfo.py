def get_student_info():
    while True:
        name = input("Enter Name: ").strip().title()
        if any(char.isdigit() for char in name):
            print("You entered a number or digit in the name")
            
        elif name:
            break
        else:
            print("Invalid: Name cannot be empty")
    while True:
        try:
            age = int(input("Enter Age: "))
            if  age <= 20:
                break
            elif age <= 14:
                print("Sorry you are a minor")
            else:
                print("Ineligable. ")
        except ValueError:
            print("Invalid input in age. Please Enter a Number.")
        
    while True:
        matricule = input("Enter Matricule: ").strip()
        
        if not matricule:
            print("Matricule field cannot be empty.")
            
        elif len(matricule) == 6:
            break
        elif len(matricule) > 6:
            print("You have surpassed the matricule lenght.")
        else:
            print("Invalid matricule lenght. Please enter your 6 figure matricule")
    
    return name, age, matricule

get_student_info()

