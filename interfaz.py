import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename , asksaveasfilename
import json
from analizador import analizar
datos_Json= None
class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=120,
            height=25,
            font=("Courier New", 13),
        )

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40, bg="#dee2e6")
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        
    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(
                2,
                y,
                anchor="nw",
                text=linenum,
                fill="#868e96",
                font=("Courier New", 13, "bold"),
            )
            i = self.textwidget.index("%s+1line" % i)


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1")
        self.geometry("1000x700")
        self.scroll = ScrollText(self)
        self.scroll.pack()
        self.after(200, self.scroll.redraw())

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.filemenu)
        self.filemenu.add_command(label="Abrir Archivo", command=self.open_file)
        self.filemenu.add_command(label="Guardar Archivo", command=self.save_file)
        self.filemenu.add_command(label="Salir", command=self.destroy)
        
        self.filemenu.add_separator()
        self.menu.add_command(label="Analizar", command=self.analizar_texto)
        self.menu.add_command(label="Ver reporte")
        self.menu.add_command(label="Ver errores", command=self.devolver_errores)
    def open_file(self):
        global datos_Json
        filepath = askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        self.scroll.delete(1.0,tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.scroll.insert(tk.END, text)
        self.title(f"Proyecto 1 - {filepath}")
    def save_file(self):
        global datos_Json
        if datos_Json == None:
            tk.messagebox.showerror(title="Error", message="No se hay archivo seleccionado aun")
            return
        filepath = asksaveasfilename(
            defaultextension="json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
            initialfile="resultados.json",
        )
        if not filepath:
            tk.messagebox.showerror(title="Error", message="No se ha guardado el archivo")
            return
        with open(filepath, "w") as output_file:
            text = self.scroll.get(1.0, tk.END)
            output_file.write(text)
        self.title(f"Proyecto 1 - {filepath}")
    def analizar_texto(self):
        print("Analizando...")
        text = self.scroll.get(1.0, tk.END) 
        arbol = analizar(text)
    def devolver_errores(self):
        file = open("errores.JSON","w+")
        file.write(json.dumps(analizar.devolver_errores()))
        file.close()


app = Ventana()
app.mainloop()

