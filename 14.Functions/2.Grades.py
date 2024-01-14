def from_num_to_text(grade):
    if 2<=grade<=2.99:
        grade='Fail'
    elif 3<=grade<3.5:
        grade='Poor'
    elif 3.5<=grade<4.5:
        grade='Good'
    elif 4.5<=grade<5.5:
        grade='Very Good'
    elif 5.5<=grade<=6:
        grade='Excellent'
    else:
        grade='Invalid value'
    return grade

earned_grade=float(input())
print(from_num_to_text(earned_grade))