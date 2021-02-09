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
from form1 import create_form1
from form2 import create_form2
from form3 import create_form3
import numpy as np 
from animation import toggleMenu

Form  = uic.loadUiType(os.path.join(os.getcwd() , "Desktop_1.ui"))[0]




# GUI

class Practice(QMainWindow , Form):
    def __init__(self):
        super(Practice , self).__init__()
        self.setupUi(self)
        self.Subtitle.setEnabled(False)
        self.First_form_b.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.Second_form_b.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Third_form_b.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Btn_Toggle.clicked.connect(lambda: toggleMenu(self, 250, True))
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.F2_NEXT_2.clicked.connect(self.f1_p_next)
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
        self.F1_NEXT_2.clicked.connect(self.f2_p_next)
        self.F3_NEXT_4.clicked.connect(self.f3_p_next)
        self.F1_NEXT_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_24))
        self.F1_PREVIOUS_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page))
        self.F1_NEXT_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_25))
        self.F1_PREVIOUS_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_4))
        self.F5_NEXT_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_26))
        self.F5_PREVIOUS_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_24))
        self.F6_NEXT_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_28))
        self.F6_PREVIOUS_6.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_25))
        self.F8_PREVIOUS_5.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_26))
        self.F3_NEXT_4.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_13))
        self.F1_NEXT_9.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_34))
        self.F1_PREVIOUS_7.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_10))
        self.F1_NEXT_10.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_35))
        self.F1_PREVIOUS_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_13))
        self.F5_NEXT_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_36))
        self.F5_PREVIOUS_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_34))
        self.F6_NEXT_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_38))
        self.F6_PREVIOUS_8.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_35))
        self.F8_PREVIOUS_7.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_36))        
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
        self.ADD_LANG_F2_3.clicked.connect((self.add_F_3_language_values))
        self.ADD_SKILL_F2_3.clicked.connect((self.add_F_3_skill_values))
        self.ADD_EDUCATION_F1_8.clicked.connect((self.add_F_3_education_values))
        self.ADD_WORK_F1_8.clicked.connect((self.add_F_3_work_values))
        self.pic_pushButton.clicked.connect(self.selectFile)
        self.pic_pushButton_1.clicked.connect(self.selectFile1)
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
        self.personal_list_f3 = []
        self.lang_list_f3 = []
        self.lang_level_list_f3 = []
        self.skill_list_f3 = []
        self.skill_level_list_f3 =[]
        self.title_list_f3 =[]
        self.education_date_list_f3 = []
        self.place_list_f3 = []
        self.summary_list_f3 = []
        self.education_date_list_w_f3 = []     
        self.title_list_w_f3 = []
        self.place_list_w_f3 = []
        self.summary_list_w_f3 = []

        self.skill_slider_f3.setMinimum(1)
        self.skill_slider_f3.setMaximum(10)
        self.skill_slider_f3.setTickInterval(1)
        self.skill_slider_f3.setTickPosition(QSlider.TicksBelow)
        self.lang_slider_f3.setMinimum(1)
        self.lang_slider_f3.setMaximum(10)
        self.lang_slider_f3.setTickInterval(1)
        self.lang_slider_f3.setTickPosition(QSlider.TicksBelow)
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
        self.F3_NEXT_4.clicked.connect(self.F_3_personal_values)
        self.F4_NEXT_2.clicked.connect(self.get_value)
        self.F3_NEXT_2.clicked.connect(self.get_value)
        self.F5_NEXT_2.clicked.connect(self.get_value)
        self.F6_NEXT_2.clicked.connect(self.get_value)
        self.F7_NEXT_2.clicked.connect(self.get_value)
        self.F1_NEXT_2.clicked.connect(self.get_value)
        self.F6_NEXT_6.clicked.connect(self.get_value)
        self.F3_NEXT_4.clicked.connect(self.get_value)
        self.F1_NEXT_10.clicked.connect(self.get_value)
        self.F1_NEXT_9.clicked.connect(self.get_value)
        self.F5_NEXT_8.clicked.connect(self.get_value)
        self.F6_NEXT_8.clicked.connect(self.get_value)
        self.f1_create_button.clicked.connect(self.create_f1)
        self.f1_create_button_5.clicked.connect(self.create_f2)
        self.f1_create_button_7.clicked.connect(self.create_f3)
        self.education_date_list = []
        self.Summary_f1 = self.Summary_F1.toPlainText().split(" ")

    

    def f1_p_next(self):
        if self.First_name_f1.text() == "" :
            self.First_name_label_f1.setStyleSheet("color : #FF0000;") 
            if self.Last_name_F1.text() != "" :
                self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_F1.text() != "" :
                self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F1.text() != "" :
                self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F1.text() != "" :
                self.Email_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Github_F1.text() != "" :
                self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
        if self.Last_name_F1.text() == "" :
            self.Last_name_label_f1.setStyleSheet("color : #FF0000;") 
            if self.First_name_f1.text() != "" :
                self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
            if self.Feild_name_F1.text() != "" :
                self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F1.text() != "" : 
                self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F1.text() != "" :
                self.Email_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Github_F1.text() != "" :
                self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
        if self.Feild_name_F1.text() == "" :
            self.Feild_name_label_f1.setStyleSheet("color : #FF0000;")
            if self.First_name_f1.text() != "" :
                self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F1.text() != "" :
                self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F1.text() != "" : 
                self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F1.text() != "" :
                self.Email_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Github_F1.text() != "" :
                self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
        if self.Phone_F1.text() == "" : 
            self.Phone_label_f1.setStyleSheet("color : #FF0000;") 
            if self.First_name_f1.text() != "" :
                self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F1.text() != "" :
                self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_F1.text() != "" :
                self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F1.text() != "" :
                self.Email_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Github_F1.text() != "" :
                self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
        if self.Email_F1.text() == "" :
            self.Email_label_f1.setStyleSheet("color : #FF0000;") 
            if self.First_name_f1.text() != "" :
                self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F1.text() != "" :
                self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_F1.text() != "" :
                self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F1.text() != "" : 
                self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Github_F1.text() != "" :
                self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
        if self.Github_F1.text() == "" :
            self.Github_label_f1.setStyleSheet("color : #FF0000;") 
            if self.First_name_f1.text() != "" :
                self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F1.text() != "" :
                self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_F1.text() != "" :
                self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F1.text() != "" : 
                self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F1.text() != "" :
                self.Email_label_f1.setStyleSheet("color : #bfbfbf;")                          
           

        if  self.First_name_f1.text() != "" and self.Feild_name_F1.text() != "" and self.Github_F1.text() != "" :
              if  self.Last_name_F1.text() != "" and self.Phone_F1.text() != "" and self.Email_F1.text() != "" :
                    self.First_name_label_f1.setStyleSheet("color : #bfbfbf;")
                    self.Last_name_label_f1.setStyleSheet("color : #bfbfbf;") 
                    self.Feild_name_label_f1.setStyleSheet("color : #bfbfbf;") 
                    self.Phone_label_f1.setStyleSheet("color : #bfbfbf;") 
                    self.Email_label_f1.setStyleSheet("color : #bfbfbf;") 
                    self.Github_label_f1.setStyleSheet("color : #bfbfbf;")               
                    self.Address_label_f1.setStyleSheet("color : #bfbfbf;")
                    self.stackedWidget_f1.setCurrentWidget(self.F1_p4)

    def f2_p_next(self):
        if self.First_name_f2.text() == "" :
           
            self.First_name_label_f2.setStyleSheet("color : #FF0000;") 
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Last_name_F2.text() == "" :
            
            self.Last_name_label_f2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Year_F2.text() == "" :
            
            self.Year_label_f2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Day_F2.text() == "" :
            
            self.Day_label_f2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Feild_name_f2.text() == "" :
            
            self.Feild_name_label_f2.setStyleSheet("color : #FF0000;")
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Phone_F2.text() == "" : 
            
            self.Phone_label_f2.setStyleSheet("color : #FF0000;") 
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   

        if self.Email_F2.text() == "" :
            
            self.Email_label_f2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")               
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")   
        
        if self.Address_F2.text() == "" :   
                       
            self.Address_label_f2_2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.pic_lineEdit.text() != "" :
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")
        if self.pic_lineEdit.text() == "" :   
                       
            self.URL_label_f2.setStyleSheet("color : #FF0000;") 
            if self.First_name_f2.text() != "" :
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
            if self.Last_name_F2.text() != "" :
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Phone_F2.text() != "" :
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f2.text() != "" :
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Year_F2.text() != "" :
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Day_F2.text() != "" :
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F2.text() != "" :
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;")  
            if self.Address_F2.text() != "" :
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
    
           

        if self.Address_F2.text() != "" and self.First_name_f2.text() != "" and self.pic_lineEdit.text() != "" :
          if  self.Last_name_F2.text() != "" and self.Phone_F2.text() != "" and self.Email_F2.text() != "" :
            if self.Feild_name_f2.text() != "" and self.Year_F2.text() != ""  and self.Day_F2.text() != "": 
 
                self.First_name_label_f2.setStyleSheet("color : #bfbfbf;")
                self.Last_name_label_f2.setStyleSheet("color : #bfbfbf;") 
                self.Feild_name_label_f2.setStyleSheet("color : #bfbfbf;") 
                self.Phone_label_f2.setStyleSheet("color : #bfbfbf;") 
                self.Email_label_f2.setStyleSheet("color : #bfbfbf;") 
                self.Year_label_f2.setStyleSheet("color : #bfbfbf;")
                self.Day_label_f2.setStyleSheet("color : #bfbfbf;")
                self.URL_label_f2.setStyleSheet("color : #bfbfbf;")
                self.Address_label_f2_2.setStyleSheet("color : #bfbfbf;")
                self.stackedWidget_2.setCurrentWidget(self.page_4)          
    def f3_p_next(self):
        if self.First_name_f3.text() == "" :
           
            self.First_name_label_f3.setStyleSheet("color : #FF0000;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;")  
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;")  

        if self.Last_name_F3.text() == "" :
           
            self.Last_name_label_f3.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;")
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;") 

        if self.Feild_name_f3.text() == "" :
               
            self.Home_phone_label_f3.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;")   

        if self.Phone_F3.text() == "" :
               
            self.Phone_label_f3.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;")  
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;")  

        if self.Email_F3.text() == "" :
               
            self.Email_label_f2_3.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;")
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;") 

        if self.pic_lineEdit_1.text() == "" :
               
            self.URL_label_f2_3.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.Website_F3.text() != "" :
                self.Email_label_f2_4.setStyleSheet("color : #bfbfbf;") 
        if self.Website_F3.text() == "" :
               
            self.Email_label_f2_4.setStyleSheet("color : #FF0000;") 
            if self.First_name_f3.text() != "" :
                self.First_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Last_name_F3.text() != "" :
                self.Last_name_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Feild_name_f3.text() != "" :
                self.Home_phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Phone_F3.text() != "" :
                self.Phone_label_f3.setStyleSheet("color : #bfbfbf;") 
            if self.Email_F3.text() != "" :
                self.Email_label_f2_3.setStyleSheet("color : #bfbfbf;") 
            if self.pic_lineEdit_1.text() != "" :
                self.URL_label_f2_3.setStyleSheet("color : #bfbfbf;")    
     

        if self.First_name_f3.text() != "" and self.Last_name_F3.text() != "" and self.Email_F3.text() != ""  :
          if  self.Feild_name_f3.text() != "" and self.Phone_F3.text() != ""  :
            if self.Website_F3.text() != "" and self.pic_lineEdit_1.text() != "" : 
 
                self.First_name_f3.setStyleSheet("color : #bfbfbf;")
                self.Last_name_F3.setStyleSheet("color : #bfbfbf;") 
                self.Feild_name_f3.setStyleSheet("color : #bfbfbf;") 
                self.Phone_F3.setStyleSheet("color : #bfbfbf;") 
                self.Email_F3.setStyleSheet("color : #bfbfbf;") 
                self.Website_F3.setStyleSheet("color : #bfbfbf;")
                self.pic_lineEdit_1.setStyleSheet("color : #bfbfbf;")
                self.stackedWidget_3.setCurrentWidget(self.page_13) 
    def add_repo(self):
        
        if self.Repo_line_edit_F1.text() not in self.repo_list:
            self.repo_list.append(self.Repo_line_edit_F1.text())
        self.Repo_line_edit_F1.setText("")


    def selectFile(self):
        self.pic_lineEdit.setText(str(QFileDialog.getOpenFileName()[0]))

    def selectFile1(self):
        self.pic_lineEdit_1.setText(str(QFileDialog.getOpenFileName()[0]))



      
    def F_1_personal_values(self):
            address = [self.country_str.text() , self.City_str.text() , self.Street_str.text() , self.Num_str.text()]   
            github = []
            
            github.append(self.Github_F1.text())
            github.extend(self.repo_list)
            self.personal_list = [
            self.First_name_f1.text() + " " + self.Last_name_F1.text() , 
            self.Feild_name_F1.text() , 
            address , 
            self.Phone_F1.text() , 
            self.Email_F1.text() , 
            github ,  
            ]
            print(self.personal_list)
            github = []
            return self.personal_list


    def F_2_personal_values(self):

            self.personal_list_f2 = [
            self.pic_lineEdit.text(),
            self.First_name_f2.text() + " " + self.Last_name_F2.text() , 
            self.Feild_name_f2.text() , 
            self.Month_F2.currentText() + " " +self.Day_F2.text()+ " " +"," +" "+  self.Year_F2.text() ,
            self.Address_F2.text() ,
            self.Phone_F2.text() , 
            self.Email_F2.text() , 
            ]

    def F_3_personal_values(self):
    
            self.personal_list_f3 = [
            self.pic_lineEdit_1.text(),
            self.First_name_f3.text() + " " + self.Last_name_F3.text() , 
            self.Feild_name_f3.text() , 
            self.Summary_F3.toPlainText().split(" "),
            self.country_str_2.text() + "," +self.City_str_2.text()+ ","+ self.Street_str_2.text() +"," +  self.Num_str_2.text() ,
            self.Phone_F3.text(),
            self.Email_F3.text() ,
            self.Website_F3.text() , 

            ]
            


    def add_F_1_language_values(self):
    
            if self.lang_line_edit_f1.text() not in self.lang_list :
                self.lang_list.append(self.lang_line_edit_f1.text())
                self.lang_level_list.append(int(self.lang_slider_f1.value()))
                self.lang_line_edit_f1.setText("")
                self.lang_slider_f1.setValue(0)

    def add_F_1_skill_values(self):
        
            if self.skill_line_edit_f1.text() not in self.skill_list :
                self.skill_list.append(self.skill_line_edit_f1.text())
                self.skill_level_list.append(int(self.skill_slider_f1.value()))
                self.skill_line_edit_f1.setText("")
                self.skill_slider_f1.setValue(0)

    def add_F_2_language_values(self):
        
            if self.lang_line_edit_f2.text() not in self.lang_list_f2 :
                self.lang_list_f2.append(self.lang_line_edit_f2.text())
                self.lang_level_list_f2.append(int(self.lang_slider_f2.value()))
                self.lang_line_edit_f2.setText("")
                self.lang_slider_f2.setValue(0)

    def add_F_2_skill_values(self):
        
            if self.skill_line_edit_f2.text() not in self.skill_list_f2 :
                self.skill_list_f2.append(self.skill_line_edit_f2.text())
                self.skill_level_list_f2.append(int(self.skill_slider_f2.value()))
                self.skill_line_edit_f2.setText("")
                self.skill_slider_f2.setValue(0)


    def add_F_3_language_values(self):

            if self.lang_line_edit_f3.text() not in self.lang_list_f3 :
                self.lang_list_f3.append(self.lang_line_edit_f3.text())
                self.lang_level_list_f3.append(int(self.lang_slider_f3.value()))
                self.lang_line_edit_f3.setText("")
                self.lang_slider_f3.setValue(0)

    def add_F_3_skill_values(self):
        
            if self.skill_line_edit_f3.text() not in self.skill_list_f3 :
                self.skill_list_f3.append(self.skill_line_edit_f3.text())
                self.skill_level_list_f3.append(int(self.skill_slider_f3.value()))
                self.skill_line_edit_f3.setText("")
                self.skill_slider_f3.setValue(0)

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
                self.un_line_edit_f1.setText("")
                self.gpa_line_edit_f1.setText("")
                self.summary_text_edit_f1.setText("")
                self.from_date_edit_f1.setText("")
                self.to_date_edit_f1.setText("")

                
            
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
                self.title_edit_f1.setText("")
                self.un_line_edit_f1_5.setText("")
                self.summary_text_edit_f1_5.setText("")
                self.from_date_edit_f1_5.setText("")
                self.to_date_edit_f1_5.setText("")
    def add_F_3_education_values(self):
        

            if self.title_edit_f1_3.text() not in self.title_list_f3 :
                self.education_list_f3 = []
                self.title_list_f3.append(self.title_edit_f1_3.text())
                education_str = self.from_date_edit_f1_7.text() +  " - "  + self.to_date_edit_f1_7.text()   
                self.education_date_list_f3.append(education_str)  
                self.place_list_f3.append(self.un_line_edit_f1_7.text())
                self.summary_list_f3.append(self.summary_text_edit_f1_7.toPlainText().split(" "))
                self.education_list_f3.append(self.education_date_list_f3)       
                self.education_list_f3.append(self.title_list_f3)
                self.education_list_f3.append(self.place_list_f3)
                self.education_list_f3.append(self.summary_list_f3)
                self.title_edit_f1_3.setText("")
                self.un_line_edit_f1_7.setText("")
                self.summary_text_edit_f1_7.setText("")
                self.from_date_edit_f1_7.setText("")
                self.to_date_edit_f1_7.setText("")
                
            


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
                self.title_line_edit_f1_2.setText("")
                self.work_summary_text_edit_f1.setPlainText("")
                self.from_w_date_edit_f1.setText("")
                self.to_w_date_edit_f1.setText("")



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
            self.company_line_edit_f1_6.setText("")
            self.title_line_edit_f1_6.setText("")
            self.work_summary_text_edit_f1_5.setPlainText("")
            self.to_w_date_edit_f1_5.setText("")
            self.from_w_date_edit_f1.setText("")
    def add_F_3_work_values(self):
        

            self.work_list_f3 = []
            self.title_list_w_f3.append(self.title_line_edit_f1_8.text())
            education_str = self.from_w_date_edit_f1_7.text() +  " - "  + self.to_w_date_edit_f1_7.text()   
            self.education_date_list_w_f3.append(education_str)  
            self.place_list_w_f3.append(self.company_line_edit_f1_8.text())
            self.summary_list_w_f3.append(self.work_summary_text_edit_f1_7.toPlainText().split(" "))
            self.work_list_f3.append(self.education_date_list_w_f3)       
            self.work_list_f3.append(self.title_list_w_f3)
            self.work_list_f3.append(self.place_list_w_f3)
            self.work_list_f3.append(self.summary_list_w_f3)
            self.company_line_edit_f1_8.setText("")
            self.title_line_edit_f1_8.setText("")
            self.work_summary_text_edit_f1_7.setPlainText("")
            self.to_w_date_edit_f1_7.setText("")
            self.from_w_date_edit_f1_7.setText("")


    def add_F_1_award_values(self):

            if self.award_summary_text_edit_f1.toPlainText() not in self.title_award_list :
                    
                self.award_list = []
                award_str = self.award_date_edit_f1.text()
                self.title_award_list.append(self.award_summary_text_edit_f1.toPlainText()) 
                self.award_date_list.append(award_str)    
                self.award_list.append(self.award_date_list)
                self.award_list.append(self.title_award_list)
                self.award_summary_text_edit_f1.setText("")
                self.award_date_edit_f1.setText("")



    def get_value(self) : 
        pass



    def create_f1(self):
        font = [str(self.font_f2_combo.currentText()) , self.fontsize_f1_spinbox.value()]
        skills = [self.skill_list , self.skill_level_list ]
        language =  [self.lang_list  , self.lang_level_list ]
        create_form1(self.personal_list,skills,language,self.Summary_f1,self.work_list,self.education_list,self.award_list,font)
    def create_f2(self):
        font = [str(self.font_f2_combo.currentText()) , self.fontsize_f2_spinBox.value()]
        skills = [self.skill_list_f2 , self.skill_level_list_f2 ]
        language =  [self.lang_list_f2 , self.lang_level_list_f2 ]
        create_form2(self.personal_list_f2,self.education_list_f2,self.work_list_f2,language,skills,font)
    def create_f3(self):
        font = [str(self.font_f2_combo_2.currentText()) , self.fontsize_f2_spinBox_3.value()]
        skills = [self.skill_list_f3 , self.skill_level_list_f3 ]
        language =  [self.lang_list_f3 , self.lang_level_list_f3 ]
        create_form3(self.personal_list_f3 , skills , language , self.work_list_f3 , self.education_list_f3 , font)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    app.setStyle("Fusion")
    w = Practice()
    w.show()
    sys.exit(app.exec_())
    
    








