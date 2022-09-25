import tkinter as tk
import requests

LOCAL_HOST = "http://127.0.0.1"
PORT = "3000"

def main():
    print("Python Running...")

    voo_value = "Undefined"

    try:
        response = requests.get(local_host + ":" + port)
        voo_value = str(response.json())
    except BaseException as error:
        print("Error occurred with receiving a response")

    window = tk.Tk()
    voo_value_label = tk.Label(text="Value of VOO: " + str(voo_value))
    voo_value_label.pack(padx = 10, pady = 10)
    window.mainloop()

if __name__ == "__main__":
    main()