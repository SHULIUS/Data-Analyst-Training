import tkinter as tk
from tkinter import filedialog
import PyPDF2

class PDFTextReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de PDF (Texto)")
        self.root.geometry("700x600")

        # Área de texto
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Controles
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        self.btn_open = tk.Button(control_frame, text="Abrir PDF", command=self.abrir_pdf)
        self.btn_open.pack(side=tk.LEFT, padx=10)

        self.btn_prev = tk.Button(control_frame, text="Anterior", command=self.pagina_anterior)
        self.btn_prev.pack(side=tk.LEFT, padx=10)

        self.btn_next = tk.Button(control_frame, text="Siguiente", command=self.pagina_siguiente)
        self.btn_next.pack(side=tk.LEFT, padx=10)

        self.label_pagina = tk.Label(control_frame, text="Página: 0")
        self.label_pagina.pack(side=tk.LEFT, padx=10)

        self.reader = None
        self.total_paginas = 0
        self.pagina_actual = 0

    def abrir_pdf(self):
        ruta = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if ruta:
            with open(ruta, 'rb') as f:
                self.reader = PyPDF2.PdfReader(f)
                self.total_paginas = len(self.reader.pages)
                self.pagina_actual = 0
                self.mostrar_pagina()

    def mostrar_pagina(self):
        if self.reader:
            texto = self.reader.pages[self.pagina_actual].extract_text()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, texto if texto else "[Página sin texto]")
            self.label_pagina.config(text=f"Página: {self.pagina_actual + 1} / {self.total_paginas}")

    def pagina_siguiente(self):
        if self.reader and self.pagina_actual < self.total_paginas - 1:
            self.pagina_actual += 1
            self.mostrar_pagina()

    def pagina_anterior(self):
        if self.reader and self.pagina_actual > 0:
            self.pagina_actual -= 1
            self.mostrar_pagina()


# Ejecutar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTextReader(root)
    root.mainloop()
