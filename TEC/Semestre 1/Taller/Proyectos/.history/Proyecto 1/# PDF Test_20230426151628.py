# PDF Test

from reportlab.pdfgen import canvas # Libreria para generar el PDF

def marcas_por_evento_datos():

    # Crear un lienzo
    pdf = canvas.Canvas("C:/Users/led_2/Desktop/mi_pdf.pdf")

    # Agregar texto
    pdf.drawString(100, 750, "Hola, mundo.")

    # Guardar el PDF
    pdf.save()

hola = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]

for i in hola:
    for j in i:
        i

print (hola)