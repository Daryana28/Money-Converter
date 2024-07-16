import tkinter as tk
def usd_to_idr():
    angka = textbock.get()
    dollar = float(angka) * 16165.0
    text.set("Rp." + str(dollar))
    label2.config(font=("helvetica", 15, "bold"),fg="green")
 
Window  = tk.Tk()
Window.title("Money Converter")
Window.geometry("800x300")
label1 = tk.Label(Window, text="USD", font=('helvetica', 12, 'bold'))
label1.pack()

textbock = tk.Entry(Window, font=('helvetica', 15, 'bold'), width=5, justify=tk.CENTER) 
textbock.pack()

button = tk.Button(Window, text="TO",command=usd_to_idr, font=('helvetica', 12, 'bold'))
button.pack()

text = tk.StringVar()
text.set("IDR")

label2 = tk.Label(Window, font=('helvetica', 12, 'bold'), textvariable=text)
label2.pack()

Window.mainloop()