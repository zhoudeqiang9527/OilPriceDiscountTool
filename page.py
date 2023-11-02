import tkinter as tk
from plot import plot_page 
from getOilPrice import insert_tables 

window = tk.Tk()

textbox = tk.Text(window)
textbox.pack()

def button_click():
    fig, ax = plot_page(textbox.get("1.0", "end-1c"))
    ax.set_title('Plot from Textbox')
    fig.canvas.draw()

button = tk.Button(window, text="Plot", command=button_click)
button.pack()

if __name__ == '__main__':
    insert_tables()
    window.mainloop()