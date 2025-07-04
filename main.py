import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("460x620")
        self.root.configure(bg="#22252D")

        self.criar_interface()
        self.root.bind("<Key>", self.tecla_pressionada)

    def criar_interface(self):
        self.entrada = tk.Entry(self.root, font=("Consolas", 24), bd=10, insertwidth=2,
                                width=22, borderwidth=4, relief="flat", bg="#1E1E1E", fg="white", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=5, pady=20)

        botoes = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("√", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("x²", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("π", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("e", 4, 4),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("log", 5, 3), ("ln", 5, 4),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("⌫", 6, 3)
        ]

        for (texto, linha, coluna) in botoes:
            cor = "#3C4048" if texto.isdigit() or texto == "." else "#556080"
            if texto in ("=", "C", "⌫"):
                cor = "#5C7AEA" if texto == "=" else "#EA5C5C"
            comando = lambda t=texto: self.acao_botao(t)
            tk.Button(self.root, text=texto, padx=16, pady=16, bd=0, bg=cor, fg="white",
                      font=("Arial", 14), command=comando).grid(row=linha, column=coluna, padx=5, pady=5)

    def acao_botao(self, tecla):
        if tecla == "=":
            self.calcular()
        elif tecla == "C":
            self.entrada.delete(0, tk.END)
        elif tecla == "⌫":
            self.entrada.delete(len(self.entrada.get()) - 1)
        elif tecla in ("sin", "cos", "tan", "log", "ln", "√", "x²", "π", "e"):
            self.funcao_cientifica(tecla)
        else:
            self.entrada.insert(tk.END, tecla)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

    def funcao_cientifica(self, funcao):
        try:
            valor = self.entrada.get()
            num = float(eval(valor)) if valor else 0
            if funcao == "sin":
                res = math.sin(math.radians(num))
            elif funcao == "cos":
                res = math.cos(math.radians(num))
            elif funcao == "tan":
                res = math.tan(math.radians(num))
            elif funcao == "log":
                res = math.log10(num)
            elif funcao == "ln":
                res = math.log(num)
            elif funcao == "√":
                res = math.sqrt(num)
            elif funcao == "π":
                res = math.pi
            elif funcao == "e":
                res = math.e
            elif funcao == "x²":
                res = num ** 2
            else:
                res = "Erro"
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(res))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

    def tecla_pressionada(self, event):
        tecla = event.keysym
        if tecla in "1234567890":
            self.entrada.insert(tk.END, tecla)
        elif tecla in ("plus", "KP_Add"):
            self.entrada.insert(tk.END, "+")
        elif tecla in ("minus", "KP_Subtract"):
            self.entrada.insert(tk.END, "-")
        elif tecla in ("asterisk", "KP_Multiply"):
            self.entrada.insert(tk.END, "*")
        elif tecla in ("slash", "KP_Divide"):
            self.entrada.insert(tk.END, "/")
        elif tecla == "Return":
            self.calcular()
        elif tecla == "BackSpace":
            self.entrada.delete(len(self.entrada.get()) - 1)
        elif tecla == "Escape":
            self.entrada.delete(0, tk.END)
        elif tecla == "period" or tecla == "comma":
            self.entrada.insert(tk.END, ".")
        elif tecla == "parenleft":
            self.entrada.insert(tk.END, "(")
        elif tecla == "parenright":
            self.entrada.insert(tk.END, ")")

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
