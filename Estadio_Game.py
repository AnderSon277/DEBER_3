from tkinter import *  
tk = Tk()
canvas = Canvas(tk,width=800,height=500)
canvas.pack()
my_image= PhotoImage(file="Campo-Futbol.gif")
my_image2= PhotoImage(file="ball2.gif")
canvas.create_image(80,40,anchor=NW, image=my_image)
canvas.create_image(350,195,anchor=NW, image=my_image2)
canvas.pack(expand=YES, fill=BOTH)
tk.title("EL JUEGO DE ANDER")
x,y=350,195

def moveball(event):
	global x,y
	if event.keysym == 'Up':
		canvas.move(2,0,-10)
		y=y-10
	elif event.keysym == 'Down':
		canvas.move(2,0,10)
		y=y+10
	elif event.keysym == 'Left':
		canvas.move(2,-10,0)
		x=x-10
	elif event.keysym == 'Right':
		canvas.move(2,10,0)
		x=x+10
	else:
		canvas.move(2,0,0)
	if  (x==630 and y==195) :
		msg = Message(tk,width=250, text = "GOOOOOOOOL")
		msg.config(bg='blue', font=('times', 20, 'italic'))
		msg.pack()
	elif (x==70 and y==195) :
		msg = Message(tk,width=250, text = "GOOOOOOOOL")
		msg.config(bg='red', font=('times', 20, 'italic'))
		msg.pack()
	else:
		msg.config(state="heidenn")

		
canvas.bind_all('<KeyPress-Up>',moveball)
canvas.bind_all('<KeyPress-Down>',moveball)
canvas.bind_all('<KeyPress-Left>',moveball)
canvas.bind_all('<KeyPress-Right>',moveball)

tk.mainloop()