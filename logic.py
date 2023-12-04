from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_GradeCalc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.input_total.setFocus()
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.label_result.setVisible(False)

        self.scores = []
        self.num_students = 0
        self.best = 0
        self.grade = ''

    def save_data(self, scores, best):
        filename = 'student_scores.py'
        with open(filename, 'w') as file:
            file.write(f'Best Score: {best}\n')
            file.write('Student Scores: ')
            for score in scores:
                file.write(f'{score}')
                file.write(', ')

    def clear(self):
        self.input_1.clear()
        self.input_2.clear()
        self.input_3.clear()
        self.input_4.clear()
        self.input_total.clear()
        self.label_result.clear()

    def get_scores(self):
        num1 = self.input_1.text().strip()
        num2 = self.input_2.text().strip()
        num3 = self.input_3.text().strip()
        num4 = self.input_4.text().strip()
        input_list = [num1, num2, num3, num4]


        try:
            self.num_students = int(self.input_total.text())
            scores = [int(num) for num in input_list if num]
            if len(scores) != self.num_students:
                self.label_result.setText(f'Number of students must be {self.num_students}.')
                return None

        except ValueError:
            self.label_result.setText(f'Must enter integers.')
            return None

        self.best = max(scores)
        return scores, self.best

    def update_score(self):
        self.get_scores()

    def submit(self):
        self.label_result.setVisible(True)
        result = self.get_scores()

        if result is not None:
            scores, best = result
            self.show_result(best)
        else:
            return

    def show_result(self, best):
        counter = 1
        result_text = ""
        scores, _ = self.get_scores()
        for score in scores:
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

            result_text += f'Student {counter} score is {score} and grade is {grade}\n'
            counter += 1

        self.label_result.setText(f'Results: \n\n{result_text}  \n\t    Best Grade: {best}')