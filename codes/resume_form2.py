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
    pdf.output(f"{name}_form2.pdf")

image = "trump.png"
name = "Sajad Khavari"
field = "Electrical Engineering"
birth = "may 9 , 1999"
address = "Iran,Mashhad,faramarz abbasi,23"
phone = "09159179628"
e_mail = "mt.khavari.n@gmail.com"
personal_info=[image,name,field,birth,address,phone,e_mail]

education_dates=["2001-2008","2009-2018"]
education_title=["Master Electrical Engineering","PHD Computer Science"]
education_center=["Amirkabir University","Sharif University"]
e1 = "amirkabir university iran has no number very good afternoon is none and its empty"
e2 = "sharif university azady square iran best persepolis esteghlal"
education_sum=[e1.split(" "),e2.split(" ")]
education=[education_dates,education_title,education_center,education_sum]

works_dates=["2003-2007","2012-2019"]
works_title=["Embedded system","IoT Gateway"]
works_company=["Communication Company","Irancell"]
w1 = "Embedded system in Communication Company iran and persepolis barcelona esteghlal iran sajad"
w2 = "Iot Gateway in Irancell hamrahe aval iran intenational nackend linel messi iran "
works_sum = [w1.split(" "),w2.split(" ")]
work_experience=[works_dates,works_title,works_company,works_sum]

languages = [["English","France","Persian","German","Spanish"],[4,5,3,2,1]]
software = [["Python","MATLAB","React Native"],[5,2,4]]

font = ["arial",12]
create_form2(personal_info,education,work_experience,languages,software,font)