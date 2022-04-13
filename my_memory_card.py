from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

class Question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

q1=Question("In what year was the grear fire of London?", "1666", "1999", "1062", "666")
q2=Question("In what year was Moscow founded?", "1047", "1666", "147", "2012")
q3=Question("What is the powerhouse of the cell?", "mytochondria", "heart", "nucleus", "oven")
q4=Question("What is Force divided by mass?", "acceleration", "distance", "power", "speed")
q5=Question("What is the integral of sin(x)?", "-cos(x)", "tan(x)", "cos(x)", "-sin(x)")

q_list = [q1,q2,q3,q4,q5]




def show_ans():
        gbox1.hide()
        gbox2.show()
        ans_b.setText("Next Question")
        main_win.questions_asked += 1
        if answers[0].isChecked():
                label2.setText("Correct!")
                main_win.correct_ans += 1
                label4.setText("Correct answers: "+str(main_win.correct_ans))
        else:
                label2.setText("Incorrect, sorry.")
        label5.setText("User rating: "+str(100*main_win.correct_ans/main_win.questions_asked)+" %") 
def show_qst():
        gbox2.hide()
        gbox1.show()
        ans_b.setText("Answer")
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)

def test():
        if ans_b.text() == "Answer":
                show_ans()
        else:
                next_qst()
def ask(q: Question):
        shuffle(answers)
        label1.setText(q.question)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        label3.setText(q.right_answer)
        show_qst()


def next_qst():
        shuffle(q_list)
        main_win.current_qst = main_win.current_qst + 1
        if main_win.current_qst >= len(q_list):
                main_win.current_qst = 0
        q = q_list[main_win.current_qst]
        ask(q)


app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card App")
main_win.move(400,300)
main_win.resize(400,300)
main_win.current_qst = -1
main_win.correct_ans = 0
main_win.questions_asked = 0

label1 = QLabel("--A very difficult question goes here.--")
gbox1 = QGroupBox("Answer options")
gbox2 = QGroupBox("Correct answer:")
label2=QLabel("--Correct/Incorrect--")
label3=QLabel("--correct answer written here--")
label4=QLabel("Correct answers: 0")
label5=QLabel("User rating: 0%")

v4 = QVBoxLayout()
v4.addWidget(label2)
v4.addWidget(label3)
gbox2.setLayout(v4)


ans_b = QPushButton("Answer")
RadioGroup = QButtonGroup()
b1=QRadioButton("Option 1")
b2=QRadioButton("Option 2")
b3=QRadioButton("Option 3")
b4=QRadioButton("Option 4")
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)
answers=[b1,b2,b3,b4]

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
h1=QHBoxLayout()

v1.addWidget(label4,alignment=Qt.AlignRight)
v1.addWidget(label5,alignment=Qt.AlignRight)
v1.addWidget(label1)
v1.addWidget(gbox1)
v1.addWidget(gbox2)
v1.addWidget(ans_b, stretch=3)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
gbox1.setLayout(h1)


main_win.setLayout(v1)

#ask("In what year was the grear fire of London", "1666", "1999", "1062", "666")
gbox2.hide()
shuffle(q_list)
ans_b.clicked.connect(test)
next_qst()

main_win.show()
app.exec()
