from PIL import Image, ImageWin
import win32print
import win32ui

# Nom de l'imprimante
printer_name = "EPSON437291 (ET-3850 Series)"

# Charger l'image
image_path = "img1.png"
image = Image.open(image_path)

# Obtenir le handle de l'imprimante
hprinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hprinter, 2)
printer_dc = win32ui.CreateDC()
printer_dc.CreatePrinterDC(printer_name)

# Déterminer la taille du papier
width = printer_dc.GetDeviceCaps(8)  # HORZRES
height = printer_dc.GetDeviceCaps(10)  # VERTRES

# Redimensionner l'image pour s'adapter à la page
image = image.resize((width, height))

# Démarrer l'impression
printer_dc.StartDoc(image_path)
printer_dc.StartPage()

# Convertir l'image en format imprimable et l'envoyer à l'imprimante
dib = ImageWin.Dib(image)
dib.draw(printer_dc.GetHandleOutput(), (0, 0, width, height))

# Terminer l'impression
printer_dc.EndPage()
printer_dc.EndDoc()
printer_dc.DeleteDC()
win32print.ClosePrinter(hprinter)

print("Impression terminée avec succès !")
