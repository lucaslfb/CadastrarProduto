import ctypes
import sqlite3
import tkinter.messagebox
from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

ctypes.windll.shcore.SetProcessDpiAwareness(True)


def create_db():
    conection = sqlite3.connect('produtos.db')
    c = conection.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos'")
    table_exists = c.fetchone()

    if not table_exists:
        c.execute(''' CREATE TABLE produtos (
            nome_produto TEXT,
            quantidade INTEGER,
            data TEXT,
            preco REAL,
            id_produto INTEGER
            );
        ''')

    conection.commit()
    conection.close()


def register_project():
    conection = sqlite3.connect('produtos.db')
    c = conection.cursor()

    c.execute("INSERT INTO produtos VALUES(:nome_produto, :quantidade, :data, :preco, :id_produto)",
              {
                  'nome_produto': entry_1.get(),
                  'quantidade': entry_2.get(),
                  'data': entry_3.get(),
                  'preco': entry_4.get(),
                  'id_produto': entry_5.get()
              }
              )

    conection.commit()
    conection.close()


def make_center_window(width, height):
    window = Tk()

    width_w = window.winfo_screenwidth()
    height_h = window.winfo_screenheight()

    x = (width_w - width) // 2
    y = (height_h - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")
    return window


def verify_field():
    entry = [entry_1, entry_2, entry_3, entry_4, entry_5]

    if not all(e.get() for e in entry):
        tkinter.messagebox.showerror('Error', 'Não deixe nenhum campo em branco!')
    else:
        create_db()
        register_project()
        tkinter.messagebox.showinfo('Sucessful', 'Produto registrado com sucesso!')
        for e in entry:
            e.delete(0, END)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lucas\IdeaProjects\GuiProject\build\assets\frame0")

window = make_center_window(756, 551)
window.configure(bg="#FFFFFF")
window.title('Cadastrar produto')

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=551,
    width=756,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    378.0,
    275.0,
    image=image_image_1
)

canvas.create_text(
    76.0,
    18.0,
    anchor="nw",
    text="Cadastro de produto",
    fill="#FFFFFF",
    font=("Kanit Light", 30 * -1)
)

canvas.create_text(
    33.0,
    70.0,
    anchor="nw",
    text="Produto",
    fill="#FFFFFF",
    font=("Kanit Light", 25 * -1)
)

canvas.create_text(
    32.0,
    149.0,
    anchor="nw",
    text="Quantidade",
    fill="#FFFFFF",
    font=("Kanit Light", 25 * -1)
)

canvas.create_text(
    33.0,
    223.0,
    anchor="nw",
    text="Data",
    fill="#FFFFFF",
    font=("Kanit Light", 25 * -1)
)

canvas.create_text(
    33.0,
    298.0,
    anchor="nw",
    text="Preço",
    fill="#FFFFFF",
    font=("Kanit Light", 25 * -1)
)

canvas.create_text(
    33.0,
    373.0,
    anchor="nw",
    text="Id do produto",
    fill="#FFFFFF",
    font=("Kanit Light", 25 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    207.5,
    120.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Kanit Light", 25 * -1)
)
entry_1.place(
    x=41.0,
    y=101.0,
    width=333.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    207.5,
    199.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Kanit Light", 25 * -1)
)
entry_2.place(
    x=41.0,
    y=180.0,
    width=333.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    207.5,
    274.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Kanit Light", 25 * -1)
)
entry_3.place(
    x=41.0,
    y=255.0,
    width=334.0,
    height=41.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    207.5,
    349.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Kanit Light", 25 * -1)
)
entry_4.place(
    x=41.0,
    y=330.0,
    width=333.0,
    height=41.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    207.5,
    424.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Kanit Light", 25 * -1)
)
entry_5.place(
    x=41.0,
    y=405.0,
    width=333.0,
    height=41.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=2,
    highlightthickness=0,
    command=verify_field,
    relief="flat",
)
button_1.place(
    x=115.0,
    y=471.0,
    width=186.0,
    height=43.0
)

window.resizable(False, False)
window.mainloop()
