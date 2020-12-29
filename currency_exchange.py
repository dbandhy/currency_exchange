import tkinter

def convert(out_data, money_data):
	""" Convert dolars to soles"""
	m = money_data.get()
	out_data.set(m * 3.39)

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

out_data = tkinter.StringVar()
money_data = tkinter.DoubleVar()

tkinter.Label(frame, text='Ingrese cantidad en dólares:').pack()

text = tkinter.Entry(frame, textvar=money_data)
text.pack()

label = tkinter.Label(frame, textvar=out_data)
label.pack()

button = tkinter.Button(frame, text='Convertir', command=lambda:
convert(out_data, money_data))
button.pack()

button2 = tkinter.Button(frame, text='Salir', command=lambda:
window.destroy())
button2.pack()

window.mainloop()
