import tkinter as tk
from plot import plot_page 
from getOilPrice import insert_tables 

window = tk.Tk()

textbox = tk.Text(window)
textbox.pack()

def checkPrice(price):
    if price < 0:
        print("Price must be positive")

def button_click():
    plot_page(v92)
    

button = tk.Button(window, text="Plot", command=button_click)
button.pack()

if __name__ == '__main__':
    v92 = insert_tables()
    checkPrice(v92)
    window.mainloop()