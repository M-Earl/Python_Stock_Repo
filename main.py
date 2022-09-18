import tkinter as tk
import requests

url = "https://api.weather.gov/points/39.7456,-97.0892"

def main():
    print("Python Running...")

    response = requests.get(url)
    print(response.json())

    window = tk.Tk()
    voo_value = "ABC.XX"
    voo_value_label = tk.Label(text="Value of VOO: " + voo_value)
    voo_value_label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()