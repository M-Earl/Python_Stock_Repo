import tkinter as tk
import requests

local_host = "http://127.0.0.1"
port = "3000"

def main():
    print("Python Running...")

    response = requests.get(local_host + ":" + port)
    print(response.json())

    window = tk.Tk()
    voo_value_label = tk.Label(text="Value of VOO: " + str(response.json()))
    voo_value_label.pack(padx = 10, pady = 10)
    window.mainloop()

if __name__ == "__main__":
    main()