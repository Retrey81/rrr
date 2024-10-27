from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app
from memo__classes import QuestionsProvider, Question

#Список питань
list = QListWidget()
list.setStyleSheet('''
    QListWidget {background-color: #E0F7FA;border: 1px solid #004D40;font-size: 16px;}
    QListWidget::item {padding: 10px;}
    QListWidget::item:selected {background-color: #4CAF50;color: white;}
''')
questions = []

#Текст питань
question_text = QLabel("Запитання:")
question_input = QLineEdit()
question_input.setStyleSheet('border: 1px solid #9E9E9E; padding: 5px; font-size: 16px;')

answer1_text = QLabel("Правильна відповідь:")
answer1_input = QLineEdit("")
answer1_input.setStyleSheet('border: 1px solid #9E9E9E; padding: 5px; font-size: 16px;')

answer2_text = QLabel("Неправильна відповідь 1:")
answer2_input = QLineEdit("")
answer2_input.setStyleSheet('border: 1px solid #9E9E9E; padding: 5px; font-size: 16px;')

answer3_text = QLabel("Неправильна відповідь 2:")
answer3_input = QLineEdit("")
answer3_input.setStyleSheet('border: 1px solid #9E9E9E; padding: 5px; font-size: 16px;')

answer4_text = QLabel("Неправильна відповідь 3:")
answer4_input = QLineEdit("")
answer4_input.setStyleSheet('border: 1px solid #9E9E9E; padding: 5px; font-size: 16px;')

#Кнопки
edit_btn = QPushButton("Редагувати")
edit_btn.setStyleSheet('background-color: #FFEB3B; color: black; font-size: 16px; padding: 10px; border-radius: 5px;')

save_btn = QPushButton("Додати")
save_btn.setStyleSheet('background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;')

delete_btn = QPushButton("Видалити")
delete_btn.setStyleSheet('background-color: #F44336; color: white; font-size: 16px; padding: 10px; border-radius: 5px;')

start_btn = QPushButton("Почати")
start_btn.setStyleSheet('background-color: #2196F3; color: white; font-size: 18px; padding: 12px; border-radius: 5px;')

def menu () :
    main_line = QVBoxLayout()
    
    main_line.addWidget(QLabel("Редактор питань"), alignment=Qt.AlignCenter)
    
    first_h_line = QHBoxLayout()
    answers_block = create_answers()
    first_h_line.addWidget(list)
    first_h_line.addLayout(answers_block)
    
    main_line.addLayout(first_h_line, stretch=8)
    
    main_line.addStretch(1)
    main_line.addLayout(create_buttons(), stretch=3)
    main_line.addStretch(1)
    
    return main_line

def create_answers () :
    line = QVBoxLayout()
    
    line.addWidget(question_text)
    line.addWidget(question_input)
    
    line.addStretch(1)
    
    line.addWidget(answer1_text)
    line.addWidget(answer1_input)
    
    line.addStretch(1)
    
    line.addWidget(answer2_text)
    line.addWidget(answer2_input)
    
    line.addStretch(1)
    
    line.addWidget(answer3_text)
    line.addWidget(answer3_input)
    
    line.addStretch(1)
    
    line.addWidget(answer4_text)
    line.addWidget(answer4_input)
    
    return line

def create_buttons() :
    line = QVBoxLayout()
    hline = QHBoxLayout()
    
    hline.addWidget(edit_btn)
    hline.addWidget(save_btn)
    hline.addWidget(delete_btn)
    
    line.addLayout(hline)
    line.addWidget(start_btn)
    
    return line

def setQuestionstoMain(provider) :
    global questions
    questions = provider.giveAllQuestions()
    
    for index, question in enumerate(questions):
        item = QListWidgetItem(question.question)
        item.setData(1, index)
        list.addItem(item)

def itemSelect() :
    global questions
    
    item = list.currentItem()
    
    question_input.setText(item.text())
    answer1_input.setText(questions[item.data(1)].right_answer)
    answer2_input.setText(questions[item.data(1)].wrong1)
    answer3_input.setText(questions[item.data(1)].wrong2)
    answer4_input.setText(questions[item.data(1)].wrong3)

def addQuestion() :
    global questions
    
    question = Question(question_input.text(), answer1_input.text(), answer2_input.text(), answer3_input.text(), answer4_input.text())
    questions.append(question)
    
    item = QListWidgetItem(question_input.text())
    item.setData(1, len(questions) - 1)
    list.addItem(item)
    
def editQuestion() :
    global questions
    
    item = list.currentItem()
    
    if item is None :
        return
    
    questions[item.data(1)].question = question_input.text()
    questions[item.data(1)].right_answer = answer1_input.text()
    questions[item.data(1)].wrong1 = answer2_input.text()
    questions[item.data(1)].wrong2 = answer3_input.text()
    questions[item.data(1)].wrong3 = answer4_input.text()
    
    item.setText(questions[item.data(1)].question)

def deleteQuestion() :
    global questions
    
    item = list.currentItem()
    
    if item is None :
        return
    
    questions.pop(item.data(1))
    list.takeItem(list.currentRow())
    
list.itemClicked.connect(itemSelect)
edit_btn.clicked.connect(editQuestion)
save_btn.clicked.connect(addQuestion)
delete_btn.clicked.connect(deleteQuestion)