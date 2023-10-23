import pandas as pd
import matplotlib.pyplot as plt

def get_columns(dataframe):
    columns = list()
    for i in dataframe.columns:
        columns.append(i)
    return columns

def read_file_to_dataframe(file_to_read):
    dataframe = pd.read_csv(file_to_read,  sep = "\s+", skiprows = 0, header = None, skipinitialspace = True, skipfooter=0, engine = "python")
    return dataframe

def plot(file):
    dataframe = read_file_to_dataframe(file)
    cols = get_columns(dataframe)
    plt.hist(dataframe[cols[10]], bins = 50,  edgecolor='black', label = "Energy" )
    #print(dataframe.to_string())
    #plt.hist(dataframe[11], bins = 50,  edgecolor='black', label = "X" ) #we did 10 and it is energy, 13 Z of crystal
    #plt.hist(dataframe[12], bins = 50,  edgecolor='black', label = "y" )
    #plt.scatter(dataframe[11], dataframe[12], label = "x vs y deixnei pou epese ka8e gegonos ston x kai ston y axona")
    #plt.scatter(dataframe[11], dataframe[12], label = "3D")
    plt.legend(loc = "best")
    plt.show()



plot("3saSingles_paxys_crystallos.dat")



