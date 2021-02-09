import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # data load
    cars = pd.read_csv('cars-sample.csv')
    c_map = pd.DataFrame({'Manufacturer':cars['Manufacturer'].unique(),'color':['#6e750e','#c20078','#e50000','#15b01a','#75bbfd']})
    cars = cars.merge(c_map, on='Manufacturer', how='left')

    fig, ax = plt.subplots()
    x = cars['Weight']
    y = cars['MPG']
    ax.scatter(x, y, c = cars['color'], s = cars['Weight'], alpha = 0.5,)# label = cars['Manufacturer'].unique() )
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__=='__main__':
    print('ran from main')
    main()
