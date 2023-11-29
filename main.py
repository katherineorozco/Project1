from grades import calculate_grade


def get_score(num_students):
    while True:
        try:
            scores = input(f'Enter {num_students} score(s): ').split()
            if len(scores) < num_students:
                raise ValueError(f'Please enter at least {num_students} scores.')

            student_scores = [int(score) for score in scores]
            best = max(student_scores)

            return student_scores, best

        except ValueError as e:
            print(f'Error: {e}')


def show_result(student_scores, best):
    counter = 1
    for score in student_scores:
        grade = calculate_grade(score, best)
        print(f'Student {counter} score is {score} and grade is {grade}')
        counter += 1


def save_to_file(filename, student_scores, best):
    with open(filename, 'w') as file:
        file.write(f'Best Score: {best}\n')
        file.write('Student Scores: ')
        for score in student_scores:
            file.write(f'{score}')
            file.write(', ')


def main():
    filename = 'student_scores.py'

    while True:
        try:
            num_students = int(input('Total number of students: '))
            if num_students <= 0:
                raise ValueError('Number of students must be greater than 0.')

            student_scores, best = get_score(num_students)
            show_result(student_scores, best)
            save_to_file(filename, student_scores, best)
            break
        except ValueError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
