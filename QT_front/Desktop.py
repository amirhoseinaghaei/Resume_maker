import sys 
import random
import os 
from time import sleep
from PyQt5 import uic , QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent )
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
import f1_rc
from fpdf import FPDF

import numpy as np 

Form  = uic.loadUiType(os.path.join(os.getcwd() , "Desktop_1.ui"))[0]



################################################################################################
#First_form 


def create_form1(personal_info,skills,languages,sum_text,work_experience,education,awards,font):
    pdf = FPDF()
    pdf.add_page()
    '''HEADER'''
    pdf.set_font("Times", size=25 , style="B")
    pdf.set_fill_color(16,78,139)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,10," " + personal_info[0],fill=True,ln=1)
    pdf.set_font("courier", size=15, style="B")

    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, " " + personal_info[1], fill=True,ln=2)

    '''PERSONAL INFO'''
    pdf.set_xy(140,30)
    pdf.set_font("arial", size=18, style="B")
    pdf.set_text_color(28,28,28)
    pdf.set_fill_color(141,238,238)
    pdf.cell(0,15,"Personal Info",fill=True,ln=1)

    pdf.set_draw_color(128,128,128)
    pdf.line(140,42,190,42)

    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=14,style="B")
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 10, "Address", fill=True, ln=1)
    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=12)
    pdf.set_text_color(99,99,99)
    pdf.cell(0, 6, personal_info[2][0] +"_" + personal_info[2][1] , fill=True, ln=1)
    pdf.set_xy(140, pdf.get_y())
    pdf.cell(0, 6, personal_info[2][2], fill=True, ln=1)
    pdf.set_xy(140, pdf.get_y())
    pdf.cell(0, 6, personal_info[2][3], fill=True, ln=1)

    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=14,style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 10, "Phone", fill=True, ln=1)
    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=12)
    pdf.set_text_color(99, 99, 99)
    pdf.cell(0, 6, personal_info[3], fill=True, ln=1)

    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=14,style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 10, "E_mail", fill=True, ln=1)
    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=12)
    pdf.set_text_color(99, 99, 99)
    pdf.cell(0, 6, personal_info[4], fill=True, ln=1)

    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=14,style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 10, "Github", fill=True, ln=1)
    for i in range(len(personal_info[5])-1):
        link = "http://github/" + personal_info[5][0] +"/"+ personal_info[5][i+1]
        pdf.set_xy(140, pdf.get_y())
        pdf.set_font("arial", size=12)
        pdf.set_text_color(99, 99, 99)
        pdf.cell(0, 6, personal_info[5][i+1], fill=True, ln=1,link=link)

    '''SKILLS'''
    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=18, style="B")
    pdf.set_text_color(28, 28, 28)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 15, "Skills", fill=True, ln=1)

    pdf.set_draw_color(128, 128, 128)
    pdf.line(140, pdf.get_y()-4, 190, pdf.get_y()-4)

    for i in range(len(skills[0])):
        pdf.set_fill_color(141, 238, 238)
        pdf.set_xy(140, pdf.get_y())
        pdf.set_font("arial", size=14)
        pdf.set_text_color(99, 99, 99)
        pdf.cell(0, 15,skills[0][i], fill=True, ln=1)
        x = 170
        for j in range(5):
            if j < skills[1][i]:
                pdf.set_fill_color(0, 0, 139)
                pdf.ellipse(x,pdf.get_y()-5,4,4,style="F")
            else:
                pdf.set_fill_color(255,255,255)
                pdf.ellipse(x, pdf.get_y() - 5, 4, 4, style="F")
            x = x + 5

    '''LANGUAGES'''
    pdf.set_xy(140, pdf.get_y())
    pdf.set_font("arial", size=18, style="B")
    pdf.set_text_color(28, 28, 28)
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 15, "Languages", fill=True, ln=1)

    pdf.set_draw_color(128, 128, 128)
    pdf.line(140, pdf.get_y() - 3, 190, pdf.get_y() - 3)

    for i in range(len(languages[0])):
        pdf.set_fill_color(141, 238, 238)
        pdf.set_xy(140, pdf.get_y())
        pdf.set_font("arial", size=14)
        pdf.set_text_color(99, 99, 99)
        pdf.cell(0, 15,languages[0][i], fill=True, ln=1)
        x = 170
        for j in range(5):
            if j < languages[1][i] :
                pdf.set_fill_color(0, 0, 139)
                pdf.ellipse(x,pdf.get_y()-5,4,4,style="F")
            else:
                pdf.set_fill_color(255,255,255)
                pdf.ellipse(x, pdf.get_y() - 5, 4, 4, style="F")
            x = x + 5

    pdf.set_xy(140, pdf.get_y())
    pdf.set_fill_color(141, 238, 238)
    pdf.cell(0, 15, "", fill=True, ln=1)

    '''SUMMARY TEXT'''
    x=10
    y=34
    pdf.set_font(font[0], size=font[1])
    pdf.set_text_color(128, 128, 128)
    for i in range(len(sum_text)):
        if i == 0:
            pass
        else:
            if x + pdf.get_string_width(sum_text[i]) > 115:
                x = 10     
                y = y + font[1]/2
            else:
                x = x + pdf.get_string_width(sum_text[i-1]) + 2

        pdf.set_xy(x,y)
        pdf.cell(pdf.get_string_width(sum_text[i])+1,5,sum_text[i],0,1,"C")

    '''WORK EXPERIENCE'''
    pdf.set_xy(10,pdf.get_y())
    pdf.set_font("arial", size=16)
    pdf.set_text_color(0,0,0)
    pdf.cell(20, 20,"Work Experience", fill=False, ln=1)

    pdf.set_draw_color(128, 128, 128)
    pdf.line(10, pdf.get_y()-5, 130,pdf.get_y()-5)

    for i in range(len(work_experience[1])):
        pdf.set_xy(10,pdf.get_y())
        pdf.set_font(font[0], size=font[1],style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, work_experience[0][i], fill=False, ln=1)
        pdf.set_xy(40 , pdf.get_y() - 10)
        pdf.cell(20, 10, work_experience[1][i], fill=False, ln=1)
        x = 40
        y = pdf.get_y()
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(128, 128, 128)
        for j in range(len(work_experience[2][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(work_experience[2][i][j]) > 115:
                    x = 40
                    y = y + font[1]/2
                else:
                    x = x + pdf.get_string_width(work_experience[2][i][j-1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(work_experience[2][i][j]) + 1, 5, work_experience[2][i][j], 0, 1, "C")

    '''EDUCATION'''
    pdf.set_xy(10, pdf.get_y())
    pdf.set_font("arial", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 20, "Education", fill=False, ln=1)

    pdf.set_draw_color(128, 128, 128)
    pdf.line(10, pdf.get_y()-5, 130, pdf.get_y()-5)

    for i in range(len(education[1])):
        pdf.set_xy(10,pdf.get_y())
        pdf.set_font(font[0], size=font[1],style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, education[0][i], fill=False, ln=1)
        pdf.set_xy(40 , pdf.get_y() - 10)
        pdf.cell(20, 10, education[1][i], fill=False, ln=1)
        pdf.set_xy(40, pdf.get_y()-3)
        pdf.cell(20, 10, "GPA  " + education[2][i], fill=False, ln=1)
        x = 40
        y = pdf.get_y()
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(128, 128, 128)
        for j in range(len(education[3][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(education[3][i][j]) > 115:
                    x = 40
                    y = y + font[1]/2
                else:
                    x = x + pdf.get_string_width(education[3][i][j-1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(education[3][i][j]) + 1, 5, education[3][i][j], 0, 1, "C")

    '''AWARDS AND HONORS'''
    pdf.set_xy(10, pdf.get_y())
    pdf.set_font("arial", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 20, "Awards and Honors", fill=False, ln=1)

    pdf.set_draw_color(128, 128, 128)
    pdf.line(10, pdf.get_y() - 5, 130, pdf.get_y() - 5)

    for i in range(len(awards[1])):
        pdf.set_xy(10,pdf.get_y())
        pdf.set_font(font[0], size=font[1],style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 5, awards[0][i], fill=False, ln=1)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(128, 128, 128)
        pdf.set_xy(40 , pdf.get_y() - 5)
        pdf.cell(20, 5, awards[1][i], fill=False, ln=1)

    pdf.set_display_mode("fullpage")
    pdf.output(f"{personal_info[0]}_form1.pdf")


################################################################################################
#second form 


from fpdf import FPDF

def create_form2(personal_info,education,work_experience,languages,software,font):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(personal_info[0],w=40,h=40)

    '''NAME AND FIELD'''
    pdf.set_xy(120,20)
    pdf.set_font("Times", size=25, style="B")
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(255,255,255)
    pdf.cell(20, 10,personal_info[1], fill=True, ln=1)
    pdf.set_xy(120,30)
    pdf.set_font("courier", size=15, style="B")
    pdf.cell(0, 10, personal_info[2], fill=True, ln=1,align="L")

    '''PERSONAL DETAILS'''
    pdf.set_xy(10,55)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 10, "PERSONAL DETAILS", fill=True, ln=1)

    pdf.set_line_width(1)
    pdf.set_draw_color(0,0,0)
    pdf.line(10,63,200,63)

    pdf.set_xy(20,68)
    pdf.set_font("times", size=15)
    pdf.set_text_color(91,91,91)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "Birth", fill=True, ln=1)
    pdf.set_xy(50,pdf.get_y()-5)
    pdf.cell(20, 5, personal_info[3], fill=True, ln=1)

    pdf.set_xy(20, pdf.get_y()+3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(91, 91, 91)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "Address", fill=True, ln=1)
    pdf.set_xy(50, pdf.get_y() - 5)
    pdf.cell(20, 5, personal_info[4], fill=True, ln=1)

    pdf.set_xy(20, pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(91, 91, 91)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "phone", fill=True, ln=1)
    pdf.set_xy(50, pdf.get_y() - 5)
    pdf.cell(20, 5, personal_info[5], fill=True, ln=1)

    pdf.set_xy(20, pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(91, 91, 91)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "E-Mail", fill=True, ln=1)
    pdf.set_xy(50, pdf.get_y() - 5)
    pdf.cell(20, 5, personal_info[6], fill=True, ln=1)

    '''EDUCATION'''
    pdf.set_xy(10, pdf.get_y())
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 12, "EDUCATION", fill=True, ln=1)

    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y()-3, 200, pdf.get_y()-3)

    for i in range(len(education[1])):
        pdf.set_xy(10,pdf.get_y())
        pdf.set_font(font[0], size=font[1]+2,style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, education[1][i], fill=False, ln=1)
        pdf.set_xy(150 , pdf.get_y()-8)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(255,255,255)
        pdf.set_fill_color(0,0,0)
        pdf.cell(25, 5, education[0][i], fill=True, ln=1)
        pdf.set_xy(10, pdf.get_y())
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(0,0,0)
        pdf.cell(20, 6, education[2][i], fill=False, ln=1)
        x = 40
        y = pdf.get_y()
        pdf.set_font(font[0], size=font[1])
        for j in range(len(education[3][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(education[3][i][j]) > 115:
                    x = 40
                    y = y + font[1]/2
                else:
                    x = x + pdf.get_string_width(education[3][i][j-1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(education[3][i][j]) + 1, 5, education[3][i][j], 0, 1, "C")

    '''WORK EXPERIENCE'''
    pdf.set_xy(10, pdf.get_y())
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 12, "WORK EXPERIENCE", fill=True, ln=1)

    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y() - 3, 200, pdf.get_y() - 3)

    for i in range(len(work_experience[1])):
        pdf.set_xy(10,pdf.get_y())
        pdf.set_font(font[0], size=font[1]+2,style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, work_experience[1][i], fill=False, ln=1)
        pdf.set_xy(150 , pdf.get_y()-8)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(255,255,255)
        pdf.set_fill_color(0,0,0)
        pdf.cell(25, 5, work_experience[0][i], fill=True, ln=1)
        pdf.set_xy(10, pdf.get_y())
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(0,0,0)
        pdf.cell(20, 6, work_experience[2][i], fill=False, ln=1)
        x = 40
        y = pdf.get_y()
        pdf.set_font(font[0], size=font[1])
        for j in range(len(work_experience[3][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(work_experience[3][i][j]) > 115:
                    x = 40
                    y = y + font[1]/2
                else:
                    x = x + pdf.get_string_width(work_experience[3][i][j-1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(work_experience[3][i][j]) + 1, 5, work_experience[3][i][j], 0, 1, "C")

    '''SKILLS'''
    pdf.set_xy(10, pdf.get_y())
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 12, "SKILLS", fill=True, ln=1)

    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y() - 3, 200, pdf.get_y() - 3)

    pdf.set_xy(10, pdf.get_y())
    pdf.set_font(font[0], size=font[1] + 2, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 10, "Languages", fill=False, ln=1)

    pdf.set_xy(120, pdf.get_y()-10)
    pdf.set_font(font[0], size=font[1] + 2, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 10, "Software", fill=False, ln=1)

    y=pdf.get_y()
    for i in range(len(languages[0])):
        pdf.set_xy(10, pdf.get_y())
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 6, languages[0][i], fill=False, ln=1)
        x=40
        for j in range(5):
            if j < languages[1][i] :
                pdf.set_fill_color(0, 0, 139)
                pdf.ellipse(x,pdf.get_y()-5,4,4,style="F")
            else:
                pdf.set_fill_color(128,128,128)
                pdf.ellipse(x, pdf.get_y() - 5, 4, 4, style="F")
            x = x + 5
    pdf.set_y(y)
    for i in range(len(software[0])):
        pdf.set_xy(120, pdf.get_y())
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 6, software[0][i], fill=False, ln=1)
        x=150
        for j in range(5):
            if j < software[1][i] :
                pdf.set_fill_color(0, 0, 139)
                pdf.ellipse(x,pdf.get_y()-5,4,4,style="F")
            else:
                pdf.set_fill_color(128,128,128)
                pdf.ellipse(x, pdf.get_y() - 5, 4, 4, style="F")
            x = x + 5

    pdf.set_display_mode("fullpage")
    pdf.output(f"{personal_info[0]}_form2.pdf")








################################################################################################
# animation

def toggleMenu(self, maxWidth, enable):
    if enable:

        # GET WIDTH
        width = self.frame_left_menu.width()
        maxExtend = maxWidth
        standard = 70

        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
################################################################################################

################################################################################################

# GUI

class Practice(QMainWindow , Form):
    def __init__(self):
        super(Practice , self).__init__()
        self.setupUi(self)
        #         # PAGE 1

        
        self.Btn_Toggle.clicked.connect(lambda: toggleMenu(self, 250, True))

        
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1)  )

        # # PAGE 2
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        # # PAGE 3
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        self.F1_start.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p2))
    
        self.F2_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p3))
        self.F3_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p4))
        self.F3_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p2))
        self.F4_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p5))
        self.F4_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p3))
        self.F5_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p6))
        self.F5_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p4))
        self.F6_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p7))
        self.F6_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p5))
        self.F7_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p8))
        self.F7_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p6))
        self.F8_PREVIOUS.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p7))
        # self.F2_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p3))
        self.F1_NEXT_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_4))
        # self.F3_PREVIOUS_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p2))
        self.F1_NEXT_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_24))
        self.F1_PREVIOUS_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page))
        self.F1_NEXT_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_25))
        self.F1_PREVIOUS_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_4))
        self.F5_NEXT_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_26))
        self.F5_PREVIOUS_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_24))
        self.F6_NEXT_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_28))
        self.F6_PREVIOUS_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_25))
        self.F8_PREVIOUS_5.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_26))
        self.ADD_LANG_F1.clicked.connect((self.add_F_1_language_values))
        self.ADD_SKILL_F1.clicked.connect((self.add_F_1_skill_values))
        self.ADD_EDUCATION_F1_2.clicked.connect((self.add_F_1_education_values))
        self.ADD_WORK_F1_2.clicked.connect((self.add_F_1_work_values))
        self.ADD_AWARD.clicked.connect((self.add_F_1_award_values))
        self.ADD_Repo_F1.clicked.connect((self.add_repo))
        self.ADD_EDUCATION_F1_6.clicked.connect((self.add_F_2_education_values))
        self.ADD_WORK_F1_6.clicked.connect((self.add_F_2_work_values))
        self.ADD_SKILL_F2.clicked.connect((self.add_F_2_skill_values))
        self.ADD_LANG_F2.clicked.connect((self.add_F_2_language_values))
        self.pic_pushButton.clicked.connect(self.selectFile)
        self.final_f1_lang_list = []
        self.lang_list  = []
        self.lang_level_list = []
        self.final_f1_skill_list = []
        self.skill_list  = []
        self.skill_level_list = []
        self.education_list = []
        self.grade_list = []
        self.title_list = []
        self.work_list =[]
        self.award_list = []
        self.title_award_list = []
        self.repo_list =[]
        self.Summary_f1 = []
        self.place_list = []
        self.gpa_list = []
        self.summary_list =[]
        self.summary_list_1 = []
        self.work_date_list = []
        self.award_date_list = []
        self.education_date_list_f2 = []
        self.place_list_f2 = []
        self.title_list_f2 = []
        self.summary_list_f2 = []
        self.education_date_list_w_f2 = []
        self.summary_list_w_f2 = []
        self.title_list_w_f2 = []
        self.place_list_w_f2 = []
        self.skill_list_f2 = []
        self.skill_level_list_f2 = []
        self.lang_level_list_f2 = []
        self.lang_list_f2 = []
        # self.F2_PERSONAL_NEXT_2.clicked.connect(lambda: self.stackedWidget_f1.setCurrentWidget(self.F1_p3))
        # self.horizontalSlider_F1_1.setMinimum(1)
        # self.horizontalSlider_F1_1.setMaximum(5)
        # self.horizontalSlider_F1_1.setTickInterval(1)
        # self.horizontalSlider_F1_1.setTickPosition(QSlider.TicksBelow)
        # self.horizontalSlider_F1_2.setMinimum(1)
        # self.horizontalSlider_F1_2.setMaximum(5)
        # self.horizontalSlider_F1_2.setTickInterval(1)
        # self.horizontalSlider_F1_2.setTickPosition(QSlider.TicksBelow)
        # self.horizontalSlider_F1_3.setMinimum(1)
        # self.horizontalSlider_F1_3.setMaximum(5)
        # self.horizontalSlider_F1_3.setTickInterval(1)
        # self.horizontalSlider_F1_3.setTickPosition(QSlider.TicksBelow)
        # self.horizontalSlider_F1_4.setMinimum(1)
        # self.horizontalSlider_F1_4.setMaximum(5)
        # self.horizontalSlider_F1_4.setTickInterval(1)
        # self.horizontalSlider_F1_4.setTickPosition(QSlider.TicksBelow)
        # self.horizontalSlider_F1_5.setMinimum(1)
        # self.horizontalSlider_F1_5.setMaximum(5)
        # self.horizontalSlider_F1_5.setTickInterval(1)
        # self.horizontalSlider_F1_5.setTickPosition(QSlider.TicksBelow)
        self.skill_slider_f1.setMinimum(1)
        self.skill_slider_f1.setMaximum(5)
        self.skill_slider_f1.setTickInterval(1)
        self.skill_slider_f1.setTickPosition(QSlider.TicksBelow)
        self.lang_slider_f1.setMinimum(1)
        self.lang_slider_f1.setMaximum(5)
        self.lang_slider_f1.setTickInterval(1)
        self.lang_slider_f1.setTickPosition(QSlider.TicksBelow)
        self.lang_slider_f2.setMinimum(1)
        self.lang_slider_f2.setMaximum(5)
        self.lang_slider_f2.setTickInterval(1)
        self.lang_slider_f2.setTickPosition(QSlider.TicksBelow)
        self.F2_NEXT_2.clicked.connect(self.F_1_personal_values)
        self.F1_NEXT_2.clicked.connect(self.F_2_personal_values)
        self.F4_NEXT_2.clicked.connect(self.get_value)
        self.F3_NEXT_2.clicked.connect(self.get_value)
        self.F5_NEXT_2.clicked.connect(self.get_value)
        self.F6_NEXT_2.clicked.connect(self.get_value)
        self.F7_NEXT_2.clicked.connect(self.get_value)
        self.F1_NEXT_2.clicked.connect(self.get_value)
        self.F6_NEXT_6.clicked.connect(self.get_value)
        self.f1_create_button.clicked.connect(self.create_f1)
        self.f1_create_button_5.clicked.connect(self.create_f2)
        self.education_date_list = []
        self.Summary_f1 = self.Summary_F1.toPlainText().split(" ")
        # self.F1_PERSONAL_NEXT.clicked.connect(self.F_2_personal_values)
        # self.F1_PERSONAL_NEXT.clicked.connect(self.F_2_personal_values)
        # self.F2_PERSONAL_NEXT_33.clicked.connect(self.F_3_personal_values)
    
    def add_repo(self):
        
        if self.Repo_line_edit_F1.text() not in self.repo_list:
            self.repo_list.append(self.Repo_line_edit_F1.text())
        self.Repo_line_edit_F1.setText("")


    def selectFile(self):
        self.pic_lineEdit.setText(str(QFileDialog.getOpenFileName()[0]))




      
    def F_1_personal_values(self):
            address = ["Iran" , "Tehran" , "ahadi" , "19"]   
            github = []
            
            github.append(self.Github_F1.text())
            github.extend(self.repo_list)
            self.personal_list = [
            self.First_name_f1.text() + " " + self.Last_name_F1.text() , 
            self.Feild_name_F1.text() , 
            # self.Linkdin_F1.text() ,
            address , 
            self.Phone_F1.text() , 
            self.Email_F1.text() , 
            github , 
            # self.Summary_F1.toPlainText() , 
            ]
            print(self.personal_list)
            github = []
            return self.personal_list


    def F_2_personal_values(self):

            self.personal_list_f2 = [
            self.pic_lineEdit.text(),
            self.First_name_f2.text() + " " + self.Last_name_F2.text() , 
            self.Feild_name_F3_4.text() , 
            self.Month_F2.currentText() + " " +self.Day_F2.text()+ " " +"," +" "+  self.Year_F2.text() ,
            self.Address_F2.text() ,
            self.Phone_F2.text() , 
            self.Email_F2.text() , 

            # self.Summary_F1.toPlainText() , 
            ]
            
















    def add_F_1_language_values(self):
    
            
            if self.lang_line_edit_f1.text() not in self.lang_list :
                self.lang_list.append(self.lang_line_edit_f1.text())
                self.lang_level_list.append(int(self.lang_slider_f1.value()))
                # self.final_f1_lang_list
                # self.final_f1_lang_list = []
                # self.final_f1_lang_list.append(lang_list , lang_level_list )
    def add_F_1_skill_values(self):
        
            
            if self.skill_line_edit_f1.text() not in self.skill_list :
                self.skill_list.append(self.skill_line_edit_f1.text())
                self.skill_level_list.append(int(self.skill_slider_f1.value()))
                # self.final_f1_lang_list = []
                # self.final_f1_lang_list.append(lang_list , lang_level_list )




    def add_F_2_language_values(self):
        
            
            if self.lang_line_edit_f2.text() not in self.lang_list_f2 :
                self.lang_list_f2.append(self.lang_line_edit_f2.text())
                self.lang_level_list_f2.append(int(self.lang_slider_f2.value()))
                # self.final_f1_lang_list
                # self.final_f1_lang_list = []
                # self.final_f1_lang_list.append(lang_list , lang_level_list )
    def add_F_2_skill_values(self):
        
            
            if self.skill_line_edit_f2.text() not in self.skill_list_f2 :
                self.skill_list_f2.append(self.skill_line_edit_f2.text())
                self.skill_level_list_f2.append(int(self.skill_slider_f2.value()))
                # self.final_f1_lang_list = []
                # self.final_f1_lang_list.append(lang_list , lang_level_list )
    def add_F_1_education_values(self):
        

            if self.un_line_edit_f1.text() not in self.grade_list :
                self.education_list = []
                self.grade_list.append(self.un_line_edit_f1.text())
                education_str = self.from_date_edit_f1.text() +  " - "  + self.to_date_edit_f1.text()   
                self.education_date_list.append(education_str)  
                self.place_list.append(self.un_line_edit_f1.text())
                self.gpa_list.append(self.gpa_line_edit_f1.text())
                self.summary_list.append(self.summary_text_edit_f1.toPlainText().split(" "))
                self.education_list.append(self.education_date_list)       
                self.education_list.append(self.place_list)
                self.education_list.append(self.gpa_list)
                self.education_list.append(self.summary_list)
                
            
    def add_F_2_education_values(self):
        

            if self.title_edit_f1.text() not in self.title_list_f2 :
                self.education_list_f2 = []
                self.title_list_f2.append(self.title_edit_f1.text())
                education_str = self.from_date_edit_f1_5.text() +  " - "  + self.to_date_edit_f1_5.text()   
                self.education_date_list_f2.append(education_str)  
                self.place_list_f2.append(self.un_line_edit_f1_5.text())
                self.summary_list_f2.append(self.summary_text_edit_f1_5.toPlainText().split(" "))
                self.education_list_f2.append(self.education_date_list_f2)       
                self.education_list_f2.append(self.title_list_f2)
                self.education_list_f2.append(self.place_list_f2)
                self.education_list_f2.append(self.summary_list_f2)
                
            
















    def add_F_1_work_values(self):


           if self.title_line_edit_f1_2.text() not in self.title_list :
                self.work_list = []
                work_str = self.from_w_date_edit_f1.text() +  " - "  + self.to_w_date_edit_f1.text()   
                self.title_list.append(self.title_line_edit_f1_2.text()) 
                self.work_date_list.append(work_str)  
                self.summary_list_1.append(self.work_summary_text_edit_f1.toPlainText().split(" "))     
                self.work_list.append(self.work_date_list)
                self.work_list.append(self.title_list)
                self.work_list.append(self.summary_list_1)


    def add_F_2_work_values(self):
        

            self.work_list_f2 = []
            self.title_list_w_f2.append(self.title_line_edit_f1_6.text())
            education_str = self.from_w_date_edit_f1_5.text() +  " - "  + self.to_w_date_edit_f1_5.text()   
            self.education_date_list_w_f2.append(education_str)  
            self.place_list_w_f2.append(self.company_line_edit_f1_6.text())
            self.summary_list_w_f2.append(self.work_summary_text_edit_f1_5.toPlainText().split(" "))
            self.work_list_f2.append(self.education_date_list_w_f2)       
            self.work_list_f2.append(self.title_list_w_f2)
            self.work_list_f2.append(self.place_list_w_f2)
            self.work_list_f2.append(self.summary_list_w_f2)
                
            




    def add_F_1_award_values(self):

            if self.award_summary_text_edit_f1.toPlainText() not in self.title_award_list :
                    
                self.award_list = []
                award_str = self.award_date_edit_f1.text()
                self.title_award_list.append(self.award_summary_text_edit_f1.toPlainText()) 
                self.award_date_list.append(award_str)    
                self.award_list.append(self.award_date_list)
                self.award_list.append(self.title_award_list)



    def get_value(self) : 
    #   print(self.personal_list_f2) 
        print(self.lang_list_f2)
        print(self.lang_level_list_f2)
        print(self.skill_list_f2)
        print(self.skill_level_list_f2)
    #     print(self.personal_list)
    #     # print(self.lang_level_list) 
    #     # print(self.skill_list)
    #     # print(self.skill_level_list) 
    #     print(self.education_list)
    #     print()
    #     print()

    def create_f1(self):
        font = ["arial" , 12]
        skills = [self.skill_list , self.skill_level_list ]
        language =  [self.lang_list  , self.lang_level_list ]
        create_form1(self.personal_list,skills,language,self.Summary_f1,self.work_list,self.education_list,self.award_list,font)
    def create_f2(self):
        font = ["arial" , self.fontsize_f2_spinBox.value()]
        skills = [self.skill_list_f2 , self.skill_level_list_f2 ]
        language =  [self.lang_list_f2 , self.lang_level_list_f2 ]
        create_form2(self.personal_list_f2,self.education_list_f2,self.work_list_f2,language,skills,font)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    app.setStyle("Fusion")
    w = Practice()
    w.show()
    sys.exit(app.exec_())
    
    








