from fpdf import FPDF

def create_form3(personal_info,skill,languages,work_experience,education,font):
    pdf = FPDF()
    pdf.add_page()
    '''HEADER'''
    pdf.set_xy(10,0)
    pdf.set_font("Times", size=25, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255,128,0)
    pdf.cell(80, 10, fill=True, ln=1)

    pdf.set_xy(29,19)
    pdf.set_font("Times", size=25, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 128, 0)
    pdf.cell(42, 42, fill=True, ln=1)

    pdf.set_xy(30,20)
    pdf.image(personal_info[0], w=40, h=40)

    '''NAME AND FIELD'''
    pdf.set_xy(120, 30)
    pdf.set_font("Times", size=25, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 10, personal_info[1], fill=True, ln=1)
    pdf.set_xy(120, 40)
    pdf.set_text_color(255, 128, 0)
    pdf.set_font("courier", size=15, style="B")
    pdf.cell(0, 10, personal_info[2], fill=True, ln=1, align="L")

    '''ABOUT ME'''
    pdf.set_xy(10,70)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "ABOUT ME", fill=True, ln=1,align="C")

    pdf.set_line_width(1)
    pdf.set_draw_color(132,132,132)
    pdf.line(15, 80,43,80)

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(43, 80, 57, 80)

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(57, 80, 85, 80)

    x = 15
    y = pdf.get_y()+5
    pdf.set_font(font[0], size=font[1])
    pdf.set_text_color(128, 128, 128)
    for j in range(len(personal_info[3])):
        if j == 0:
            pass
        else:
            if x + pdf.get_string_width(personal_info[3][j]) > 80:
                x = 15
                y = y + font[1] / 2
            else:
                x = x + pdf.get_string_width(personal_info[3][j - 1]) + 2

        pdf.set_xy(x, y)
        pdf.cell(pdf.get_string_width(personal_info[3][j]) + 1, 5, personal_info[3][j], 0, 1, "C")


    '''CONTACT'''
    pdf.set_xy(10, pdf.get_y()+5)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "CONTACT", fill=True, ln=1, align="C")

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(15, pdf.get_y(), 43, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(43, pdf.get_y(), 57, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(57, pdf.get_y(), 85, pdf.get_y())

    pdf.set_xy(15,pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "Address", fill=True, ln=1)
    pdf.set_text_color(132,132,132)
    pdf.set_xy(15, pdf.get_y())
    pdf.cell(20, 5, personal_info[4], fill=True, ln=1)

    pdf.set_xy(15, pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "Phone", fill=True, ln=1)
    pdf.set_text_color(132, 132, 132)
    pdf.set_xy(15, pdf.get_y())
    pdf.cell(20, 5, personal_info[5], fill=True, ln=1)

    pdf.set_xy(15, pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "E-Mail", fill=True, ln=1)
    pdf.set_text_color(132, 132, 132)
    pdf.set_xy(15, pdf.get_y())
    pdf.cell(20, 5, personal_info[6], fill=True, ln=1)

    pdf.set_xy(15, pdf.get_y() + 3)
    pdf.set_font("times", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 5, "WebSite", fill=True, ln=1)
    pdf.set_text_color(132, 132, 132)
    pdf.set_xy(15, pdf.get_y())
    pdf.cell(20, 5, personal_info[7], fill=True, ln=1)

    '''LANGUAGES'''
    pdf.set_xy(10, pdf.get_y() + 5)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "LANGUAGES", fill=True, ln=1, align="C")

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(15, pdf.get_y(), 43, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(43, pdf.get_y(), 57, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(57, pdf.get_y(), 85, pdf.get_y())

    for i in range(len(languages[0])):
        pdf.set_xy(15, pdf.get_y() + 5)
        pdf.set_font("times", size=15)
        pdf.set_text_color(0, 0, 0)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(20, 5, languages[0][i], fill=True, ln=1)

        pdf.set_line_width(1)
        pdf.set_draw_color(0,0,128)
        pdf.line(15, pdf.get_y() + 2, languages[1][i] * 7 + 15, pdf.get_y() + 2)

        pdf.set_line_width(1)
        pdf.set_draw_color(132, 132, 132)
        pdf.line(languages[1][i] * 7 + 15, pdf.get_y() + 2, 85, pdf.get_y() + 2)

    '''SKILLS'''
    pdf.set_xy(10, pdf.get_y() + 5)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "SKILLS", fill=True, ln=1, align="C")

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(15, pdf.get_y(), 43, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(43, pdf.get_y(), 57, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(57, pdf.get_y(), 85, pdf.get_y())

    for i in range(len(skill[0])):
        pdf.set_xy(15, pdf.get_y() + 5)
        pdf.set_font("times", size=15)
        pdf.set_text_color(0, 0, 0)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(20, 5,skill[0][i], fill=True, ln=1)

        pdf.set_line_width(1)
        pdf.set_draw_color(0,0,128)
        pdf.line(15, pdf.get_y()+2, skill[1][i]*7 + 15, pdf.get_y()+2)

        pdf.set_line_width(1)
        pdf.set_draw_color(132, 132, 132)
        pdf.line(skill[1][i]*7 + 15, pdf.get_y()+2, 85, pdf.get_y()+2)

    '''WORK EXPERIENCE'''
    pdf.set_xy(100, 70)
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "WORK EXPERIENCE", fill=True, ln=1, align="L")

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(100, 80, 114, 80)

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(114, 80, 200, 80)

    for i in range(len(work_experience[1])):
        pdf.set_xy(100,pdf.get_y()+3)
        pdf.set_font(font[0], size=font[1]+2,style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, work_experience[1][i], fill=False, ln=1)
        pdf.set_xy(155, pdf.get_y() - 7)
        pdf.set_font(font[0], size=font[1])
        pdf.cell(25, 5, work_experience[2][i], fill=True, ln=1)
        pdf.set_xy(100, pdf.get_y() + 3)
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.cell(20, 6, work_experience[0][i], fill=False, ln=1)
        x = 155
        y = pdf.get_y() - 6
        pdf.set_font(font[0], size=font[1])
        for j in range(len(work_experience[3][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(work_experience[3][i][j]) > 200:
                    x = 155
                    y = y + font[1] / 2
                else:
                    x = x + pdf.get_string_width(work_experience[3][i][j - 1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(work_experience[3][i][j]) + 1, 5, work_experience[3][i][j], 0, 1, "C")

    '''EDUCATION'''
    pdf.set_xy(100, pdf.get_y())
    pdf.set_font("arial", size=15, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(80, 10, "EDUCATION", fill=True, ln=1, align="L")

    pdf.set_line_width(1)
    pdf.set_draw_color(255, 128, 0)
    pdf.line(100, pdf.get_y(), 114, pdf.get_y())

    pdf.set_line_width(1)
    pdf.set_draw_color(132, 132, 132)
    pdf.line(114, pdf.get_y(), 200, pdf.get_y())

    for i in range(len(education[1])):
        pdf.set_xy(100,pdf.get_y()+3)
        pdf.set_font(font[0], size=font[1]+2,style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(20, 10, education[2][i], fill=False, ln=1)
        pdf.set_xy(155, pdf.get_y() - 7)
        pdf.set_font(font[0], size=font[1])
        pdf.cell(25, 5, education[1][i], fill=True, ln=1,align="L")
        pdf.set_xy(100, pdf.get_y() + 3)
        pdf.set_text_color(128, 128, 128)
        pdf.set_font(font[0], size=font[1])
        pdf.cell(20, 6, education[0][i], fill=False, ln=1)
        x = 155
        y = pdf.get_y() - 6
        pdf.set_font(font[0], size=font[1])
        for j in range(len(education[3][i])):
            if j == 0:
                pass
            else:
                if x + pdf.get_string_width(education[3][i][j]) > 200:
                    x = 155
                    y = y + font[1] / 2
                else:
                    x = x + pdf.get_string_width(education[3][i][j - 1]) + 2

            pdf.set_xy(x, y)
            pdf.cell(pdf.get_string_width(education[3][i][j]) + 1, 5, education[3][i][j], 0, 1, "C")

    pdf.set_display_mode("fullpage")
    pdf.output(f"{personal_info[1]}_form3.pdf")

image = "trump.png"
name = "Sara Heidari"
field = "Electrical Engineering"
about_me = "sajad khavari hastam az mashhad ke dar daneshgah amikabir dars mikhanam eeeee kheili jaleb bud mage na"
about_me = about_me.split(" ")
address = "Iran,Mashhad,faramarz abbasi,23"
phone = "09159179628"
e_mail = "mr.khavari.n@gmail.com"
website = "sajadkhavari.ir"
personal_info = [image,name,field,about_me,address,phone,e_mail,website]

languages=[["English","France"],[8,6]]

skill = [["Python","Matlab","C++"],[5,8,3]]

works_dates=["2003-2007","2012-2019"]
works_title=["Embedded system","IoT Gateway"]
works_company=["Communication Company","Irancell"]
w1 = "Embedded system in Communication Company iran and persepolis barcelona esteghlal iran sajad"
w2 = "Iot Gateway in Irancell hamrahe aval iran intenational nackend linel messi iran "
works_sum = [w1.split(" "),w2.split(" ")]
work_experience=[works_dates,works_title,works_company,works_sum]

education_dates=["2001-2008","2009-2018"]
education_title=["Master","PHD Computer Science"]
education_center=["Amirkabir University","Sharif University"]
e1 = "amirkabir university iran has no number very good afternoon is none and its empty"
e2 = "sharif university azady square iran best persepolis esteghlal"
education_sum=[e1.split(" "),e2.split(" ")]
education=[education_dates,education_title,education_center,education_sum]

font = ["arial",12]

create_form3(personal_info,skill,languages,work_experience,education,font)