def get_student_name_for_search():
    while True:
        matricule = input("\nEnter Your Matricule: ")
        if not matricule:
            print("\nYou dint enter anything. MAtricule field cannot be empty")
        elif len(matricule) ==6:
            break
        elif len(matricule) <6:
            print("\nThe matricule lenght you entered is not valid. ")
            print("Enter a valid matricule number(6 digit and letters)")
        elif len(matricule) >6:
            print("\nYou surpased the valid matricule lenght.")
            print("Re-enter your valid matricule")
        else:
            print("Aborted")
        found = False
    return matricule