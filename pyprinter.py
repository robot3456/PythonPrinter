import win32print

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
list_printers=[]

for printer in printers : 
	print(printer[2])
	lis

filename = "img1.png"
filename = "img2.jpg"

# full printer name prompted when executing this script
printer_name = ""

file_handle = open(filename, 'rb')

printer_handle = win32print.OpenPrinter(printer_name)


job_info = win32print.StartDocPrinter(printer_handle, 1, (filename, None, "RAW") )

#---------------------------------------------------------------------
win32print.StartPagePrinter(printer_handle)
win32print.WritePrinter(printer_handle, file_handle.read())

win32print.EndPagePrinter(printer_handle)
win32print.EndDocPrinter(printer_handle)

win32print.ClosePrinter(printer_handle)
file_handle.close()

#---------------------------------------------------------------------





