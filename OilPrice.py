import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("My GUI")
window.geometry("400x200")

# 创建两个Frame框
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
# 在Frame中添加第二行组件  
button2 = tk.Button(frame2, text="Button 2") 
button2.pack(side='right',padx=5)

label2 = tk.Label(frame2, text="Label 2")
label2.pack(side='left') 

textbox3 = tk.Text(frame2, height=1, width=20)
textbox3.pack(side='left')

textbox2 = tk.Text(frame2, height=1, width=20)
textbox2.pack(side='left',padx=20)

def button_click():
   textbox2.insert(tk.END, "abc")

   
# 在Frame中添加第一行组件
button1 = tk.Button(frame1, text="Button 1", command=button_click)
button1.pack(side='right',padx=5)

label1 = tk.Label(frame1, text="Label 1")
label1.pack(side='left')

textbox1 = tk.Text(frame1, height=1, width=20) 
textbox1.pack(side='left')



fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperatures = [30, 32, 34, 36, 38, 37, 36, 35, 32, 31, 30, 29] 

ax.plot(months, temperatures)
ax.set_title("Monthly Temperatures")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")

canvas = FigureCanvasTkAgg(fig, master=window)  
canvas.draw()
canvas.get_tk_widget().pack()








# 将两个Frame平行显示
frame1.pack()
frame2.pack()



window.mainloop()