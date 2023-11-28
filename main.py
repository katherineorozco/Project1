from grades import calculate_grade

def get_score(num_students):
    while True:
        scores = input(f'Enter {num_students} score(s): ').split()
        if len(scores) >= num_students:
            scores = scores[:num_students]
            break

    student_scores = [int(score) for score in scores]
    best = max(student_scores)

    return student_scores, best

def show_result(student_scores, best):
    counter = 1
    for score in student_scores:
        grade = calculate_grade(score, best)
        print(f'Student {counter} score is {score} and grade is {grade}')
        counter += 1

def main():
    num_students = int(input('Total number of students: '))
    student_scores, best = get_score(num_students)
    show_result(student_scores, best)


if __name__ == '__main__':
    main()

