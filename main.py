def Grade(score, best):
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


num_students = int(input('Total number of students: '))

scores = []
student_scores = []

counter = 1

while True:
    scores = input(f'Enter {num_students} score(s): ').split()
    if len(scores) >= num_students:
        scores = scores[:num_students]
        break

for score in scores:
    student_scores.append(int(score))

best = max(student_scores)

for score in student_scores:
    grade = Grade(score, best)
    print(f'Student {counter} score is {score} and grade is {grade}')
    counter += 1

