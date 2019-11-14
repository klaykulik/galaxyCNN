import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

def importData():

    path = './data/data_clean/'
    all_data = []
    all_files = glob.glob(path + '*.txt')

    for i, filename in enumerate(all_files):
        df = pd.read_csv(filename);
        all_data.append(df)

    complete = pd.concat(all_data)
    return complete

if __name__ == '__main__':

    gal = importData()
    # print(gal.head())
    # print(len(gal))



    X = gal.Velocity * np.sin(gal.RA) * np.cos(gal.DEC)
    Y = gal.Velocity * np.sin(gal.RA) * np.sin(gal.DEC)
    Z = gal.Velocity * np.cos(gal.DEC) 

    from mpl_toolkits.mplot3d import Axes3D




    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(X, Y, Z)
    plt.show()
