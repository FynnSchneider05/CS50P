from fpdf import FPDF



def main():
    name = input("Whats your Name? ")
    pdf = FPDF()
    pdf.add_page()

    pdf = print_title(pdf)
    pdf = print_tshirt(pdf, name)




def print_title(pdf):
    #title
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(195, 10, "CS50 Shirtificate", align="C")
    pdf.ln(30)

    return pdf


def print_tshirt(pdf, name):
    #shirt
    pdf.image("shirtificate.png",25,40, 160)

    #name
    try:
        font_size = set_font_size(name)

    except:
        main()

    else:
        pdf.set_font("Helvetica", "B", font_size)
        pdf.set_text_color(255)
        pdf.cell(195, 130, f"{name} took CS50", align="C")

        pdf.output("shirtificate.pdf")



def set_font_size(name):
    if len(name) <= 7:
        font_size = 30

    elif len(name) > 7 and len(name) <= 12:
        font_size = 25

    elif len(name) > 12 and len(name) <=19:
        font_size = 20

    elif len(name >19 and len(name) <= 25):
        font_size = 15

    else:
        raise TypeError("Name Too long")

    return font_size

if __name__ == "__main__":
    main()
