from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/propuesta_identidad_moda_KA.pdf'
LOGOS = ROOT / 'assets/logos'

W, H = 595, 842  # A4
INK = HexColor('#211917')
CLAY = HexColor('#B8674A')
WINE = HexColor('#6E1828')
SAND = HexColor('#F4EEE8')
MIST = HexColor('#E4D8CF')
MUTED = HexColor('#766B66')

def text(c, s, x, y, size, color=INK, font='Helvetica', leading=None):
    c.setFont(font, size); c.setFillColor(color)
    for line in s.split('\n'):
        c.drawString(x, y, line)
        y -= leading or size * 1.28
    return y

def right(c, s, x, y, size, color=INK, font='Helvetica'):
    c.setFont(font, size); c.setFillColor(color); c.drawRightString(x, y, s)

def pill(c, label, x, y, fill, fg=white):
    c.setFillColor(fill); c.roundRect(x, y, stringWidth(label, 'Helvetica-Bold', 8) + 20, 18, 9, fill=1, stroke=0)
    text(c, label, x+10, y+5, 8, fg, 'Helvetica-Bold')

def logo(c, filename, x, y, w, h):
    # White base guarantees a legible presentation regardless of transparency.
    c.setFillColor(white); c.roundRect(x, y, w, h, 10, fill=1, stroke=0)
    c.drawImage(ImageReader(LOGOS / filename), x+8, y+8, w-16, h-16, preserveAspectRatio=True, anchor='c', mask='auto')

def footer(c, num):
    c.setStrokeColor(MIST); c.line(48, 38, W-48, 38)
    text(c, 'ESTUDIO DE NOMBRE Y MARCA', 48, 22, 7, MUTED, 'Helvetica-Bold')
    right(c, f'{num:02d}', W-48, 22, 8, MUTED, 'Helvetica-Bold')

c = canvas.Canvas(str(OUT), pagesize=(W,H)); c.setTitle('Propuesta de identidad - Moda KA')

# 1 - cover
c.setFillColor(SAND); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(WINE); c.rect(0,0,17,H,fill=1,stroke=0)
text(c, 'IDENTIDAD PARA UNA\nTIENDA DE MODA', 55, 635, 31, INK, 'Helvetica-Bold', 38)
text(c, 'Cinco nombres. Cinco caminos.\nUna marca que se sienta cerca.', 57, 535, 15, MUTED, 'Helvetica', 22)
pill(c, 'INICIALES K - A', 57, 466, WINE)
c.setFillColor(CLAY); c.circle(473, 616, 85, fill=1, stroke=0)
c.setFillColor(WINE); c.circle(441, 585, 52, fill=1, stroke=0)
text(c, 'K A', 394, 570, 34, white, 'Helvetica-Bold')
text(c, 'Propuesta creativa', 57, 90, 11, MUTED, 'Helvetica')
text(c, '16 NOV 2026', 57, 68, 8, MUTED, 'Helvetica-Bold')
c.showPage()

# 2 - key choices
c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
text(c, 'Las dos voces principales', 48, 780, 26, INK, 'Helvetica-Bold')
text(c, 'Cercanas, memorables y con un gesto de moda propio.', 48, 750, 11, MUTED)
cards=[('KAI','Minimalista. Íntima. Fácil de recordar.','kai.png', CLAY),('KALA','Elegante. Femenina. Con carácter.','kala.png', WINE)]
for i,(name,desc,img,col) in enumerate(cards):
    x=48+i*253
    c.setFillColor(SAND); c.roundRect(x, 280, 231, 410, 16, fill=1,stroke=0)
    pill(c,'PRINCIPAL',x+18,650,col)
    text(c,name,x+18,604,28,INK,'Helvetica-Bold')
    text(c,desc,x+18,578,10,MUTED,'Helvetica')
    logo(c,img,x+18,356,195,185)
    text(c,'Un nombre que acompaña,\nsin imponerse.',x+18,324,11,INK,'Helvetica-Bold',15)
footer(c,2); c.showPage()

# 3 - full range
c.setFillColor(SAND); c.rect(0,0,W,H,fill=1,stroke=0)
text(c,'Las otras tres rutas',48,780,26,INK,'Helvetica-Bold')
text(c,'Distintas personalidades para una misma promesa: vestir con alma.',48,750,11,MUTED)
alts=[('ALKA','Original y serena.','alka.png'),('KAIA','Luminosa y actual.','kaia.png'),('AKÉ','Artística y cercana.','ake.png')]
for i,(n,d,img) in enumerate(alts):
    x=48+i*168
    c.setFillColor(white); c.roundRect(x,312,151,355,14,fill=1,stroke=0)
    text(c,n,x+16,632,20,INK,'Helvetica-Bold')
    text(c,d,x+16,609,9,MUTED)
    logo(c,img,x+12,430,127,138)
    text(c,'Una identidad\nque deja huella.',x+16,390,10,INK,'Helvetica-Bold',14)
footer(c,3); c.showPage()

# 4 - hypotheses
c.setFillColor(white); c.rect(0,0,W,H,fill=1,stroke=0)
text(c,'Qué podría sentir quien entra',48,780,26,INK,'Helvetica-Bold')
text(c,'Hipótesis de conexión emocional - una por cada nombre.',48,750,11,MUTED)
items=[
('KAI','“Aquí puedo ser yo.”','Moda para vestir lo que sientes.'),
('KALA','“Esto tiene carácter.”','Belleza cotidiana con presencia.'),
('ALKA','“No se parece a lo de siempre.”','Piezas distintas, con alma.'),
('KAIA','“Me eleva sin esfuerzo.”','Una moda joven, cuidada y luminosa.'),
('AKÉ','“Parece que me conociera.”','Una boutique que elige contigo.'),
]
for i,(n,quote,desc) in enumerate(items):
    y=675-i*112
    c.setFillColor(SAND); c.roundRect(48,y-14,499,84,12,fill=1,stroke=0)
    c.setFillColor(WINE if i==1 else CLAY); c.circle(78,y+28,17,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',10); c.drawCentredString(78,y+24,n[:2])
    text(c,n,112,y+43,13,INK,'Helvetica-Bold')
    text(c,quote,112,y+24,11,INK,'Helvetica-Oblique')
    text(c,desc,112,y+7,9,MUTED)
footer(c,4); c.showPage()

# 5 - recommendation
c.setFillColor(INK); c.rect(0,0,W,H,fill=1,stroke=0)
text(c,'Mi recomendación',48,780,26,white,'Helvetica-Bold')
text(c,'Empezar por KAI. Guardar KALA como alternativa más sofisticada.',48,747,11,MIST)
for x,n,sub,col in [(48,'KAI','Cercanía tranquila',CLAY),(302,'KALA','Elegancia con fuerza',WINE)]:
    c.setFillColor(white); c.roundRect(x,396,205,230,16,fill=1,stroke=0)
    c.setFillColor(col); c.circle(x+103,550,44,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',19); c.drawCentredString(x+103,543,n)
    text(c,sub,x+23,470,13,INK,'Helvetica-Bold')
    text(c,'Una identidad cálida,\nclara y recordable.',x+23,438,10,MUTED,'Helvetica',15)
text(c,'Siguiente paso: comprobar disponibilidad del nombre\ny crear la identidad final elegida.',48,185,15,white,'Helvetica-Bold',22)
footer(c,5); c.save()
print(OUT)
