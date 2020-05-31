import pandas as pd

class FileLoader:
	def __init__(self):
		pass

	def load(self, path):
		dataset = pd.read_csv(path)
		return(dataset)

	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		elif n == 0:
			print(df)
		else:
			print(df.tail(-n))

loader = FileLoader()
data = loader.load("./athlete_events.csv")
data = data.loc[data['Year'] == 2004]
data = data.sort_values('Age')
print(data.Age)