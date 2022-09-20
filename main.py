import tkinter as tk
import requests

local_host = "http://127.0.0.1"
port = "3000"

def main():
    print("Python Running...")

    response = requests.get(local_host + ":" + port)
    print(response.json())

    window = tk.Tk()
    voo_value = "ABC.XX"
    voo_value_label = tk.Label(text="Value of VOO: " + voo_value)
    voo_value_label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()