from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

    student_scores, best = window.get_scores()
    window.save_data(student_scores, best)


if __name__ == '__main__':
    main()

