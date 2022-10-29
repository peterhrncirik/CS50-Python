from fpdf import FPDF

# Get name
name = input('Name: ')

# Initiliaze
pdf = FPDF()
pdf.add_page()

# Set title style and print title
pdf.set_font('helvetica', 'B', 40)
pdf.cell(195, 18, 'CS50 Shirtificate', align='C')

# Set t-shirt text style
pdf.set_text_color(255,255,255)
pdf.set_font('helvetica', 'B', 20)

# add line break
pdf.ln(20)

# get image
pdf.image('./shirtificate.png', 5, 50, 200, 180)

# print name on the image
pdf.cell(195, 160, f'{name} took CS50', align='C')

# print pdf
pdf.output('shirtificate.pdf')
