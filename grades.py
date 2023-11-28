def calculate_grade(score, best):
    if score >= best - 10:
        grade = 'A'
    elif score >= best - 20:
        grade = 'B'
    elif score >= best - 30:
        grade = 'C'
    elif score >= best - 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade