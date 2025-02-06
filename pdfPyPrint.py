import os
import win32print
import win32api
import subprocess

def print_pdf(printer_name, pdf_path):
    """Imprime un fichier PDF en utilisant un programme PDF comme Adobe Acrobat Reader."""
    
    # Vérifie si le fichier PDF existe
    if not os.path.exists(pdf_path):
        print(f"Le fichier PDF {pdf_path} n'existe pas.")
        return
    
    # Vérifie si l'imprimante existe
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
    printer_names = [printer[2] for printer in printers]
    
    if printer_name not in printer_names:
        print(f"L'imprimante {printer_name} n'est pas disponible.")
        return

    # Vérifiez que l'application PDF est disponible (Adobe Acrobat Reader ou autre)
    try:
        # Si vous utilisez Adobe Acrobat Reader, l'exécutable peut être trouvé ici
        acrobat_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
        
        if not os.path.exists(acrobat_path):
            raise FileNotFoundError(f"Adobe Acrobat Reader n'a pas été trouvé à l'emplacement {acrobat_path}. Assurez-vous qu'il est installé.")
        
        # Commande pour imprimer via Acrobat Reader
        print_command = f'"{acrobat_path}" /t "{pdf_path}" "{printer_name}"'
        
        # Utilisation de subprocess pour exécuter la commande
        subprocess.run(print_command, shell=True, check=True)
        
        print(f"Le fichier PDF {pdf_path} est envoyé à l'imprimante {printer_name}.")
        
    except Exception as e:
        print(f"Erreur lors de l'impression du PDF : {e}")

def main():
    # Nom de l'imprimante à utiliser (à adapter en fonction de votre imprimante)
    # full printer name prompted when executing this script
    printer_name = ""

    
    # Chemin du fichier PDF à imprimer
    pdf_path = "document.pdf"  # Le fichier PDF doit exister à cet emplacement

    # Imprime le PDF
    print_pdf(printer_name, pdf_path)

if __name__ == "__main__":
    main()
