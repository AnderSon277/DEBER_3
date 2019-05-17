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
gol=0

def moveball(event):
	global x,y,gol,msg
	msg = Message(tk,width=250, text = "GOOOOOOOOL")
	if (event.keysym == 'Up' and gol==0):
		canvas.move(2,0,-10)
		y=y-10
	elif (event.keysym == 'Down' and gol==0):
		canvas.move(2,0,10)
		y=y+10
	elif (event.keysym == 'Left' and gol==0):
		canvas.move(2,-10,0)
		x=x-10
	elif (event.keysym == 'Right'and gol==0):
		canvas.move(2,10,0)
		x=x+10
	else:
		canvas.move(2,0,0)
	if  ((x>630) and (235>y>=145)) :
		gol=1
		msg.config(bg='blue', font=('times', 20, 'italic'))
		msg.pack()
		canvas.bind_all('<KeyPress-Return>',inicio)
		
	elif (x<70 and (235>y>=145)) :
		gol=2
		msg.config(bg='red', font=('times', 20, 'italic'))
		msg.pack()
		canvas.bind_all('<KeyPress-Return>',inicio)
		

def inicio(event):
	global x,y,gol,msg
	x,y=350,195
	if(gol==1):
		canvas.move(2,-290,0)
	elif(gol==2):
		canvas.move(2,290,0)
	gol=0
	msg.config(text="")
	
		
canvas.bind_all('<KeyPress-Up>',moveball)
canvas.bind_all('<KeyPress-Down>',moveball)
canvas.bind_all('<KeyPress-Left>',moveball)
canvas.bind_all('<KeyPress-Right>',moveball)


tk.mainloop()