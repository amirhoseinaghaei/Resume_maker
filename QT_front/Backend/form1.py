import sys 
import random
import os 
from time import sleep
from fpdf import FPDF



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
