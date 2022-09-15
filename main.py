import tkinter as tk

def main():
    print("Python Running...")
    window = tk.Tk()
    voo_value = tk.Label(text="Value of VOO: ABC.XX")
    voo_value.pack()
    window.mainloop()

if __name__ == "__main__":
    main()