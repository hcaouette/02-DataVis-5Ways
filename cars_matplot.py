import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # data load
    cars = pd.read_csv('cars-sample.csv')
    # manufacturer and color association
    color_map = {'ford':0,'toyota':1,'bmw':2,'honda':3,'mercedes':4}
    color = np.array(['#6e750e','#c20078','#e50000','#15b01a','#75bbfd'])
    cars['color_map']=cars.Manufacturer.map(color_map,na_action='ignore')
    # print(cars.head())
    col_map = cars.color_map.to_numpy()
    # print(col_map)

    #matplot part
    fig, ax = plt.subplots()
    lab = cars['Manufacturer'].unique() #'ford' 'toyota' 'bmw' 'honda' 'mercedes'
    x = cars['Weight']
    y = cars['MPG']
    ax.scatter(x, y, c = color[col_map], s = cars['Weight'], alpha = 0.5,)# label = lab )
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__=='__main__':
    print('ran from main')
    main()
