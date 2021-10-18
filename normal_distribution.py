import csv 
import pandas as pd
import plotly.figure_factory as ff

df= pd.read_csv("normal_distribution.csv")
fig= ff.create_distplot([df["Avg Rating"]],["Avg Rating of Brands"])
fig.show()