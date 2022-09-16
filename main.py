import tkinter as tk

def main():
    print("Python Running...")
    window = tk.Tk()
    voo_value = "ABC.XX"
    voo_value_label = tk.Label(text="Value of VOO: " + voo_value)
    voo_value_label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()