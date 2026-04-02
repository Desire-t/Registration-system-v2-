#calculating makes and returning average

def calculate_marks(maths, english, french):
    total_marks = maths + english + french
    wieghted_marks = (maths * 4) + (english * 3) + (french * 3)
    coeficient = 10
    average = wieghted_marks / coeficient
    
    return average