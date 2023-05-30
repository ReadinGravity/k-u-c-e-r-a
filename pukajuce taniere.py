import tkinter as tk
import random

def click(event):
    x, y = event.x, event.y
    for i in z:
        if abs(i[0] - x) < 20:
            pocet[i[1]] = pocet.get(i[1], 0) + 1
            if i[1] == puk:
                canvas.delete('all')
                v = ''.join(j for j in pocet if pocet[j] > 0).upper()
                text = f'puknuty tanierik bolo pismenko: {puk.upper()}\n'
                text += f'na co si klikol:  {v}\n'
                canvas.create_text(250, 100, text=text)
                canvas.update()
            print(pocet)

canvas=tk.Canvas(height=200, width=500)
canvas.pack()
r=20
posun=50
x=25
z=[]
for i in 'abcdefghij':
    canvas.create_oval(x - r,100 - r,x + r,100 + r, fill='#fcc603')
    canvas.create_oval(x - r + 8, 100 - r + 8, x + r - 8, 100 + r - 8, fill='#ffffff', outline='#ffffff')
    canvas.create_text(x, 100, text=i.upper())
    z.append([x, i])
    x += posun

puk = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(puk)

pocet = {}
print(z)

canvas.bind('<Button-1>', click)
tk.mainloop()
