import pandas as pd
import glob

def importData():

    path = './data/data_clean/'
    all_data = []
    all_files = glob.glob(path + '*.txt')

    for i, filename in enumerate(all_files):
        df = pd.read_csv(filename,sep = ' *\| *');
        all_data.append(df)

    complete = pd.concat(all_data)
    return complete

if __name__ == '__main__':

    everything = importData()
    print(everything.head())
    print(len(everything))
