import matplotlib.pyplot as plt

def plot_page(data):
    x = [1,2,3]
  
    y = [6,7,8]
    
    if len(y) != len(x):
        y = [y[0]] * len(x)
        
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig, ax
    
    

