# PDF Test

from reportlab.pdfgen import canvas # Libreria para generar el PDF

def marcas_por_evento_datos():

    # Crear un lienzo
    pdf = canvas.Canvas("C:/Users/led_2/Desktop/mi_pdf.pdf")

    # Agregar texto
    pdf.drawString(500, 750, "Hola, mundo.")
    pdf.drawString(100, 750, "Este es mi primer PDF.")

    # Guardar el PDF
    pdf.save()

marcas_por_evento_datos()