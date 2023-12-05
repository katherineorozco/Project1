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
        self.entry_counter = 1

    def save_data(self, scores, best):
        """Save student scores to a file."""
        filename = 'student_scores.py'
        with open(filename, 'a') as file:
            file.write(f'Entry: {self.entry_counter}\n')
            file.write(f'Best Score: {best}\n')
            file.write('Student Scores: ')
            for score in scores:
                file.write(f'{score}')
                file.write(', ')
            self.entry_counter += 1
            file.write('\n\n')

    def clear(self):
        """Clear input fields and result label."""
        self.input_1.clear()
        self.input_2.clear()
        self.input_3.clear()
        self.input_4.clear()
        self.input_total.clear()
        self.label_result.clear()

    def get_scores(self):
        """Get and validate student scores."""
        num1 = self.input_1.text().strip()
        num2 = self.input_2.text().strip()
        num3 = self.input_3.text().strip()
        num4 = self.input_4.text().strip()
        input_list = [num1, num2, num3, num4]

        try:
            self.num_students = int(self.input_total.text())
            scores = [int(num) for num in input_list if num]

            for score in scores:
                if not 0 <= score <= 100:
                    self.label_result.setText('Score must be between 0 and 100')
                    return None

            if not (1 <= self.num_students <= 4):
                self.label_result.setText('Number of students must be between 1 and 4.')
                return None

            if len(scores) != self.num_students:
                self.label_result.setText(f'Number of scores must be {self.num_students}.')
                return None

        except ValueError:
            self.label_result.setText('Must enter valid integers.')
            return None

        self.best = max(scores)
        return scores, self.best

    def update_score(self):
        """Update student scores."""
        self.get_scores()

    def submit(self):
        """Submit and display results."""
        self.label_result.setVisible(True)
        result = self.get_scores()

        if result is not None:
            scores, best = result
            self.show_result(best)
            self.save_data(scores, best)
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