import json
import ast

def read_data(filename):
	with open("data2/2-5-5-100000.json", "r") as f:
	  contents = f.read(filename)
	  data = ast.literal_eval(contents)
	  return(data)