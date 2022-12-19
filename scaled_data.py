import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
import glob
import matplotlib.pyplot as plt
"""
Read csvs, determine min max for each feature
than normalize all csv with those values"""

csv_root = '/Data/maneuvers/Informer2020/data/ETT/'
processed_csv_dest = '/Data/maneuvers/Informer2020/data/normed_ETT/'
if not os.path.exists(processed_csv_dest):
    os.mkdir(processed_csv_dest)

#csv_file_list = glob.glob(os.path.join(csv_root, '*.csv'))


# Read each CSV file into DataFrame
# This creates a list of dataframes
#df_list = (pd.read_csv(file) for file in csv_file_list)

# Concatenate all DataFrames each record is 22400
#big_df = pd.concat(df_list, ignore_index=True)
list_df = glob.glob(os.path.join(csv_root, '*.csv'))
def scale_dfs(list_df):
    for file in list_df:
        df = pd.read_csv(file)
        dates = df.iloc[:,0]
        scaler = MinMaxScaler(feature_range=(0, 1))# ‘feature wise normalization
        names = df.columns
        d = scaler.fit_transform(df.iloc[:,1:])
        #scaled_df = pd.concat([big_df.iloc[:,0],pd.DataFrame(d, columns=names[1:])], axis=1, ignore_index=False)
        d = pd.DataFrame(d, columns=names[1:])
        # insert column using insert(position,column_name,
        # first_column) function
        d.insert(0, 'date', dates)
        d.to_csv(processed_csv_dest+file.split('/')[-1], index=False)
    return names

def plot_df(df):

    size = 22400
    df.plot(x = names[0], y = names[1])
    plt.show()
scale_dfs(list_df)
#plot_df(pd.DataFrame(d))