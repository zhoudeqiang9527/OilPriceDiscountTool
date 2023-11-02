import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
matplotlib.rcParams['axes.unicode_minus'] = False     # 用来正常显示负号

def plot_page(price):
    

    startOil = 26
    oil_quantity  = [] #油的升数
    manjian = []
    danjian = []
    manjian_300=[]
    for i in range(startOil,50):
        oil_quantity.append(i)
        totalPrice = i*price
        if(totalPrice > 220):
            manjian.append(totalPrice - 15)
        else:
            manjian.append(totalPrice)
        
        total_300 = i*price
        if(total_300 > 300):
            manjian_300.append(total_300 - 30)
        else:
            manjian_300.append(total_300)

        danjian.append(i*(price-0.6))
        
    # 绘制曲线
    plt.plot(oil_quantity, manjian, label='满220减15')
    plt.plot(oil_quantity, manjian_300, label='满300减30')
    plt.plot(oil_quantity, danjian, label='每升减6毛')

    # 添加轴标签
    plt.xlabel('油量(升)')
    plt.ylabel('实付金额')

    # 添加标题
    plt.title('Price vs. Oil Quantity')

    # 添加图例
    plt.legend()

    # 显示图形
    plt.show()
    
    
    

