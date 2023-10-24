import pandas as pd 

class read():

	#define the instance variables
	def __init__(self, path_to_file):
		self.data = self.read_file_to_dataframe(path_to_file)

	def get_dataset(self):
		return self.data

	#read the data file in dataframe
	def read_file_to_dataframe(self, file_to_read):
		dataframe = pd.read_csv(file_to_read,  sep = "\s+", skiprows = 0, header = None, skipinitialspace = True, skipfooter=0, engine = "python")
		return dataframe

	#get the names of the columns of the data file
	def get_columns(self):
		columns = list()
		for i in self.data.columns:
			columns.append(i)
		return columns
	
	#print the whole dataset
	def print_whole_dataset(self):
		print(self.data.to_string())



