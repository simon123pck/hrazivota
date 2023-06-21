import tkinter as tk
win = tk.Tk()

#width, height
w = 750
h = 600

#cell_list = []

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.grid(columnspan=2, rowspan=1)


fr = open("gol.txt", "r", encoding="utf-8")

def draw_grid(win_size=15):
    count = h // win_size
    for i in range(count):
        canvas.create_line(0, i*win_size, w,i*win_size)
    count = w // win_size
    for i in range(count):
        canvas.create_line(i*win_size, 0, i*win_size, h)

def draw_cells(old_field, win_size=15):
    canvas.delete("all")
    draw_grid()
    # for item in cell_list:
    #     canvas.delete(item)
    cell_list = []
    for y in range(height):
        for x in range(width):
            if old_field[y][x] == 1:
                cell_list.append(canvas.create_oval(x*win_size, y*win_size, (x + 1)*win_size, (y+1)*win_size, fill = "purple"))


def create2Dmatrix(width, height):
    matrix = []
    for y in range(height):
        temp = []
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
    return matrix

def processfile(matrix):
    x, y = 0, 0
    for row in fr:
        x = 0
        for char in row:
            if char == "1":
                matrix[y][x]=1
            x += 1
        y += 1

def return_friends(x,y,matrix):
    count = 0
    #matrix [y][x]
    #navrhnem seriu ifov aby to fungovalo
    if x<width-1 and matrix[y][x+1] == 1:
        count += 1
    if x<width-1 and y<height-1 and matrix[y+1][x+1] == 1:
        count += 1
    if y<height-1 and matrix[y+1][x] == 1:
        count += 1
    if x>0 and y<height-1 and matrix[y+1][x-1] == 1:
        count += 1
    if x>0 and matrix[y][x-1] == 1:
        count += 1
    if x>0 and y>0 and matrix[y-1][x-1] == 1:
        count += 1
    if y>0 and matrix[y-1][x] == 1:
        count += 1
    if x<width-1 and y>0 and matrix[y-1][x+1] == 1:
        count += 1
    return count

def rewrite(oldfield, newfield):
    for x in range(width):
        for y in range(height):
            if old_field[y][x] == 1:
                friends = return_friends(x,y,old_field)
                if friends == 2 or friends == 3:
                    new_field[y][x] = 1
                elif friends < 2:
                    new_field[y][x] = 0
                elif friends > 3:
                    new_field[y][x] = 0
            elif old_field[y][x] == 0:
                friends = return_friends(x, y, old_field)
                if friends == 3:
                    new_field[y][x] = 1

width, height = fr.readline().split(" ")
width = int(width)
height = int(height)

#vytvori 2rozmerny zoz plny 0
old_field = create2Dmatrix(width,height)
#vytvori iny 2rozmerny zoz plny 0
new_field = create2Dmatrix(width,height)
#do 1.zoz nahodime 1 zo suboru
processfile(old_field)
#kreslenie mriezky
draw_grid()


def generations_automat():
    #printnes stary matrix
    #vypocitas novy matrix
    #novy hodime do stareho
    #novy vynulujeme
    global old_field, new_field
    draw_cells(old_field)
    print(old_field)
    rewrite(old_field, new_field)
    old_field = new_field.copy()
    new_field = create2Dmatrix(width, height)
    canvas.after(100,generations_automat)

def generations_click():
        #printnes stary matrix
    #vypocitas novy matrix
    #novy hodime do stareho
    #novy vynulujeme
    global old_field, new_field
    draw_cells(old_field)
    print(old_field)
    rewrite(old_field, new_field)
    old_field = new_field.copy()
    new_field = create2Dmatrix(width, height)


automat_button = tk.Button(win, text="Automaticky", bg="purple", fg="white",font="Arial 18",command=lambda:generations_automat())
automat_button.grid(column=0)
click_button = tk.Button(win, text="Po kliknutí", bg="green", fg="white",font="Arial 18", command=lambda:generations_click())
click_button.grid(row=1,column=1)

win.mainloop()
