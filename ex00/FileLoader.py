import pandas as pd

class FileLoader:
	def __init__(self):
		pass

	def load(self, path):
		dataset = pd.read_csv(path)
		return(dataset)

	def display(self, df, n):
		if n >= 0:
			print(df.head(n))
		else:
			print(df.tail(-n))

loader = FileLoader()
data = loader.load("./athlete_events.csv")
loader.display(data, 2)