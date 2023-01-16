import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")

        self.total = tk.StringVar()

        self.entry = tk.Entry(self, textvariable=self.total)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)

        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)

        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)

        self.create_button(".", 4, 1)
        self.create_button("0", 4, 2)
        self.create_button("C", 4, 3)

        self.create_button("+", 5, 1)
        self.create_button("-", 5, 2)
        self.create_button("*", 5, 3)
        self.create_button("/", 6, 1)
        self.create_button("%", 6, 2)
        self.create_button("=", 6, 3, command=self.calculate)

    def create_button(self, text, row, column, command=None):
        button = tk.Button(self, text=text, command=command)
        button.grid(row=row, column=column, padx=10, pady=10)

    def calculate(self):
        current = self.entry.get()
        try:
            self.total.set(ast.literal_eval(current))
        except (ValueError, SyntaxError):
            self.total.set(("Error"))

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()