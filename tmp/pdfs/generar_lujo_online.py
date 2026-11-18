from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/pdf/identidades_tienda_online_lujo.pdf'
LOGOS=ROOT/'assets/logos_luxury'
W,H=595,842
INK=HexColor('#1E1716'); GOLD=HexColor('#C69A4A'); CREAM=HexColor('#F6F0E8'); WINE=HexColor('#75162A'); TAUPE=HexColor('#796D68'); EMERALD=HexColor('#173D35')

def tx(c,s,x,y,sz,color=INK,font='Helvetica',lead=None):
    c.setFont(font,sz); c.setFillColor(color)
    for line in s.split('\n'):
        c.drawString(x,y,line); y-=lead or sz*1.28
    return y
def rr(c,s,x,y,sz,color=INK,font='Helvetica'):
    c.setFont(font,sz); c.setFillColor(color); c.drawRightString(x,y,s)
def footer(c,n,dark=False):
    col=HexColor('#BFB2A8') if dark else HexColor('#9A8C84')
    c.setStrokeColor(col); c.line(48,38,W-48,38)
    tx(c,'PROYECTO DE MARCA - MODA ONLINE',48,22,7,col,'Helvetica-Bold'); rr(c,f'{n:02d}',W-48,22,8,col,'Helvetica-Bold')
def tag(c,s,x,y,color=GOLD):
    ww=stringWidth(s,'Helvetica-Bold',8)+20; c.setFillColor(color); c.roundRect(x,y,ww,18,9,fill=1,stroke=0); tx(c,s,x+10,y+5,8,white,'Helvetica-Bold')
def logo(c,fn,x,y,w,h):
    c.setFillColor(white); c.roundRect(x,y,w,h,14,fill=1,stroke=0)
    c.drawImage(ImageReader(LOGOS/fn),x+7,y+7,w-14,h-14,preserveAspectRatio=True,anchor='c',mask='auto')
def pair(c,num,heading,sub,left,right,dark=False):
    bg=INK if dark else CREAM; fg=white if dark else INK; mu=HexColor('#D2C4BC') if dark else TAUPE
    c.setFillColor(bg); c.rect(0,0,W,H,fill=1,stroke=0)
    tx(c,heading,48,780,26,fg,'Helvetica-Bold'); tx(c,sub,48,750,11,mu)
    for x,item in [(48,left),(302,right)]:
        name,desc,fn,col=item
        tag(c,name.upper(),x,684,col); tx(c,name,x,644,24,fg,'Helvetica-Bold'); tx(c,desc,x,616,10,mu)
        logo(c,fn,x,300,245,270)
    footer(c,num,dark); c.showPage()

c=canvas.Canvas(str(OUT),pagesize=(W,H)); c.setTitle('Cinco identidades para una tienda online de lujo')
# cover
c.setFillColor(INK); c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(GOLD); c.circle(469,620,100,fill=1,stroke=0); c.setFillColor(WINE); c.circle(427,575,58,fill=1,stroke=0)
tx(c,'CINCO NOMBRES\nCON ALMA DE LUJO',48,650,31,white,'Helvetica-Bold',38)
tx(c,'Un universo de moda online que no se olvida.',48,548,14,HexColor('#D9CCC2'))
tag(c,'IDENTIDAD & CARÁCTER',48,486,WINE)
tx(c,'Una selección emocional, pronunciable\ny diseñada para dejar una primera impresión.',48,162,12,HexColor('#D9CCC2'),'Helvetica',18)
tx(c,'NOV 2026',48,86,8,HexColor('#D9CCC2'),'Helvetica-Bold'); c.showPage()

# naming page
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
tx(c,'Cinco nombres. Cinco emociones.',48,780,26,INK,'Helvetica-Bold')
tx(c,'Todos son compuestos, fáciles de decir y pensados para una marca premium.',48,750,11,TAUPE)
names=[('LUNAVÉ','Luna + allure','Misterio y elegancia.'),('ALMARIA','Alma + aria','Una belleza que se siente.'),('VELORIA','Velvet + aurora','Glamour con sombra y luz.'),('AMARIEL','Amar + halo','Romance con presencia.'),('SOLEVIA','Sol + vía','Luz que acompaña.')]
for i,(n,origin,feel) in enumerate(names):
    y=668-i*111; c.setFillColor(white); c.roundRect(48,y-8,499,82,12,fill=1,stroke=0)
    c.setFillColor(GOLD if i in (0,2) else WINE); c.circle(79,y+32,18,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',11); c.drawCentredString(79,y+28,str(i+1))
    tx(c,n,116,y+43,15,INK,'Helvetica-Bold'); tx(c,origin,116,y+24,10,TAUPE,'Helvetica-Oblique'); tx(c,feel,286,y+24,10,INK)
footer(c,2); c.showPage()

pair(c,3,'Dos identidades que seducen','La noche y el alma: lujo emocional con un símbolo propio.',('Lunavé','Misterio que atrae.','lunave.png',GOLD),('Almaria','Una belleza que abraza.','almaria.png',WINE),True)
pair(c,4,'Dos identidades que mandan','Drama, textura y una presencia imposible de ignorar.',('Veloria','Glamour que mira de frente.','veloria.png',GOLD),('Amariel','Romance con fuerza.','amariel.png',HexColor('#B96B4E')),False)

# single final logo
c.setFillColor(EMERALD); c.rect(0,0,W,H,fill=1,stroke=0)
tx(c,'Una identidad que ilumina',48,780,26,white,'Helvetica-Bold')
tx(c,'SOLEVIA es serena, reconocible y aspiracional.',48,750,11,HexColor('#D7D3BC'))
tag(c,'SOLEVIA',48,688,GOLD); tx(c,'Solevia',48,646,28,white,'Helvetica-Bold'); tx(c,'Luz que acompaña. Lujo que respira.',48,617,11,HexColor('#D7D3BC'))
logo(c,'solevia.png',98,245,399,320)
tx(c,'Pensada para una marca luminosa, refinada\ny memorable desde el primer vistazo.',98,188,13,white,'Helvetica-Bold',19)
footer(c,5,True); c.showPage()

# final recommendation
c.setFillColor(INK); c.rect(0,0,W,H,fill=1,stroke=0)
tx(c,'Mi selección',48,780,26,white,'Helvetica-Bold')
tx(c,'Tres nombres listos para convertirse en una firma de moda.',48,750,11,HexColor('#D9CCC2'))
choices=[('LUNAVÉ','El más poético.','Para moda nocturna, sensual y editorial.',GOLD),('VELORIA','El más magnético.','Para una marca con actitud y alto impacto.',WINE),('SOLEVIA','El más versátil.','Para lujo sereno, luminoso y duradero.',EMERALD)]
for i,(n,head,desc,col) in enumerate(choices):
    y=620-i*150; c.setFillColor(white); c.roundRect(48,y,499,112,14,fill=1,stroke=0)
    c.setFillColor(col); c.circle(84,y+56,23,fill=1,stroke=0); c.setFillColor(white); c.setFont('Helvetica-Bold',10); c.drawCentredString(84,y+52,str(i+1))
    tx(c,n,125,y+70,16,INK,'Helvetica-Bold'); tx(c,head,125,y+48,11,INK,'Helvetica-Bold'); tx(c,desc,125,y+27,9,TAUPE)
tx(c,'Antes de elegir: comprobar la disponibilidad legal\ndel nombre, dominio y redes sociales.',48,105,12,HexColor('#D9CCC2'),'Helvetica',17)
footer(c,6,True); c.save(); print(OUT)
