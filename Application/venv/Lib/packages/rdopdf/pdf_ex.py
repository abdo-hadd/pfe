import os
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String
from reportlab.platypus import SimpleDocTemplate, Paragraph 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def add_legend(draw_obj, chart, data):
    legend = Legend()
    legend.alignment = 'right'
    legend.x = 10
    legend.y = 70
    legend.colorNamePairs = Auto(obj=chart)
    draw_obj.add(legend)
def pie_chart_with_legend(DATA,LABELS):
    data = DATA
    drawing = Drawing(width=400, height=200)
    my_title = String(170, 40, ' Pie Chart Domain', fontSize=14)
    pie = Pie()
    pie.sideLabels = True
    pie.x = 150
    pie.y = 65
    pie.data = data
    pie.labels = LABELS
    pie.slices.strokeWidth = 0.5
    drawing.add(my_title)
    drawing.add(pie)
    add_legend(drawing, pie, data)
    return drawing

def get_pdf_from_CV(fileName,Nom,Prenom,Age,Numero,Email,Gendre,Adresse,Domain,skills,DATA,LABELS):

	pdf = canvas.Canvas(fileName)
	pdf.setTitle('Document title!')


	pdfmetrics.registerFont(TTFont('abc', os.path.join(os.path.dirname(__file__),'SakBunderan.ttf')))

	# 1 aykhsni n7te immage  
	pdf.drawInlineImage(os.path.join(os.path.dirname(__file__),'lis.png'), 10, 700)

	pdf.drawInlineImage(os.path.join(os.path.dirname(__file__),'limn.png'), 410, 710)

	pdf.setFont('abc', 15)
	pdf.drawCentredString(305, 770, 'Université Cadi Ayyad')
	pdf.drawCentredString(300, 755, 'Faculté des Sciences Semlalia')
	pdf.drawCentredString(302, 740, 'Département d informatique')
	pdf.drawCentredString(310, 725, 'Marrakech')


	pdf.setFillColorRGB(204, 0, 0)
	pdf.setFont("Courier-Bold", 24)
	pdf.drawCentredString(310,630, 'Rapport CV/RESUME')
	pdf.line(180, 625, 440, 625)
	pdf.line(180, 622, 440, 622)

	pdf.setFillColorRGB(0, 0, 0)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 580)
	text.textLine('Nom')
	pdf.drawText(text)
	pdf.drawCentredString(110, 580, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 580)
	text.textLine(Nom)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 560)
	text.textLine('Prénom')
	pdf.drawText(text)
	pdf.drawCentredString(110, 560, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 560)
	text.textLine(Prenom)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 540)
	text.textLine('Age')
	pdf.drawText(text)
	pdf.drawCentredString(110, 540, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 540)
	text.textLine(Age)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 520)
	text.textLine('Numéro')
	pdf.drawText(text)
	pdf.drawCentredString(110, 520, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 520)
	text.textLine(Numero)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 500)
	text.textLine('Email')
	pdf.drawText(text)
	pdf.drawCentredString(110, 500, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 500)
	text.textLine(Email)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 480)
	text.textLine('Gendre')
	pdf.drawText(text)
	pdf.drawCentredString(110, 480, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 480)
	text.textLine(Gendre)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 460)
	text.textLine('Adresse')
	pdf.drawText(text)
	pdf.drawCentredString(110, 460, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 460)
	text.textLine(Adresse)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 440)
	text.textLine('Domain')
	pdf.drawText(text)
	pdf.drawCentredString(110, 440, ':')
	pdf.setFont("Courier", 17)
	text = pdf.beginText(140, 440)
	text.textLine(Domain)
	pdf.drawText(text)

	pdf.setFont("Courier-Bold", 17)
	text = pdf.beginText(25, 420)
	text.textLine('Skills')
	pdf.drawText(text)
	pdf.drawCentredString(110, 420, ':')
	pdf.setFont("Courier", 13)
	#text.setFillColor(colors.red)
	text = pdf.beginText(140, 420)


	skills = str(skills)
	skills = skills.split(',')
	ling=""
	totale_ling =[]
	i=0
	for a in skills:
		a = str(a)
		a = a[:-1]
		ling += a
		i += 1
		if i % 5 == 0:
			totale_ling.append(ling)
			ling = ""

	for line in totale_ling:
	    text.textLine(line)
	pdf.drawText(text)

	# ngade char pie

	d = Drawing(400,200)
	chart = pie_chart_with_legend(DATA,LABELS)    
	d.add(chart)
	d.save(formats=['png'], outDir=os.path.join(os.path.dirname(__file__),'./Lib/site-packages/rdopdf'), fnRoot='test')

	pdf.drawInlineImage(os.path.join(os.path.dirname(__file__),'test.png'), 120, 1)

	pdf.save()
