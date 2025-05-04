import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

class PDFReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de PDF")
        self.root.geometry("600x600")

        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.frame_controls = tk.Frame(root)
        self.frame_controls.pack(pady=5)

        self.btn_prev = tk.Button(self.frame_controls, text="Anterior", command=self.prev_page)
        self.btn_prev.pack(side=tk.LEFT, padx=10)

        self.btn_next = tk.Button(self.frame_controls, text="Siguiente", command=self.next_page)
        self.btn_next.pack(side=tk.LEFT, padx=10)

        self.btn_open = tk.Button(self.frame_controls, text="Abrir PDF", command=self.open_pdf)
        self.btn_open.pack(side=tk.LEFT, padx=10)

        self.label_page = tk.Label(self.frame_controls, text="Página: 0")
        self.label_page.pack(side=tk.LEFT, padx=10)

        self.doc = None
        self.page_num = 0

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.doc = fitz.open(file_path)
            self.page_num = 0
            self.show_page()

    def show_page(self):
        if self.doc and 0 <= self.page_num < len(self.doc):
            page = self.doc[self.page_num]
            text = page.get_text()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
            self.label_page.config(text=f"Página: {self.page_num + 1}")

    def next_page(self):
        if self.doc and self.page_num < len(self.doc) - 1:
            self.page_num += 1
            self.show_page()

    def prev_page(self):
        if self.doc and self.page_num > 0:
            self.page_num -= 1
            self.show_page()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReader(root)
    root.mainloop()
