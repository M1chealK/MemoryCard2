#создай приложение для запоминания инф
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

all_question = []
all_question.append(
    Question('Самое глубокое озеро в России', 'Байкал', 'Онежское', 'Белое' , 'Ладожское')
)
all_question.append(
    Question("Какого цвета нет во влаге России", "зелёного", "белого", "синего", "красного")
)

shuffle(all_question)


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle(' Memory Card')
main_win.resize(500, 300)
main_win.a = 0

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton() 
rbtn_2 = QRadioButton() 
rbtn_3 = QRadioButton() 
rbtn_4 = QRadioButton() 
vopros = QLabel()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4)
button = QPushButton('ОТВЕТИТЬ')

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    vopros.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
ask(all_question[main_win.a])

main_win.total = 1
main_win.score = 0


def otvet():
    if answer[0].isChecked():
        request.setText('Правильно')
        main_win.score += 1

    else:
        request.setText('Не правильно')

def set_answer():
    button.setText('Следующий вопрос')
    AnsGroupBox.show()
    RadioGroupBox.hide()
    otvet()
    print('Всего вопросов', main_win.total)
    print('Правильных ответов',main_win.score)

def click_ok():
    if button.text() == "ОТВЕТИТЬ":
        if answer[0].isChecked() or answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            set_answer()
    else:
        nextanswer()

button.clicked.connect(click_ok)


def nextanswer():
    button.setText('ОТВЕТИТЬ')
    AnsGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    ask(all_question[main_win.a+1])
    main_win.total += 1


layout_ans = QVBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignHCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignHCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignHCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignHCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)




AnsGroupBox = QGroupBox('Результаты теста')
layout_forAnsGroup = QHBoxLayout()
request = QLabel('Правильно/Неправильно')
layout_forAnsGroup.addWidget(request, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_forAnsGroup)

layout_ans.addWidget(vopros, alignment = Qt.AlignHCenter)
layout_ans.addWidget(RadioGroupBox)
layout_ans.addWidget(AnsGroupBox)
layout_ans.addWidget(button, alignment = Qt.AlignHCenter)


AnsGroupBox.hide()
RadioGroupBox.show()

main_win.setLayout(layout_ans)

main_win.show()
app.exec_()


