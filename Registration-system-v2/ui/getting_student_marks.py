def get_marks():
    while True:
        try:
            maths = float(input("Maths: "))
            
            if 0 <= maths <=20:
                break
            
            else:
                print("You surpased the marks range. (Enter Marks btwn 1 -20)")
        except ValueError:
            print("Invalid input. Enter a number")
    while True:
        try:
            english = float(input("English: "))
            if 0 >= english <=20:
                break
            
            else:
                print("You surpased the marks range. (Enter Marks btwn 1 -20)")
        except ValueError:
            print("Invalid input. Enter a number (btwn 1 -20)")
    
    while True:
        try:
            french = float(input("Freanch: "))
            if 0 >= french <=20:
                break
            
            else:
                print("You surpased the marks range. (Enter Marks btwn 1 -20)")
        except ValueError:
            print("Invalid input. Enter a number (btwn 1 -20)")
    return maths, english, french

