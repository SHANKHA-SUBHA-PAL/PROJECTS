from numpy import average
import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("Projects\MOBILE-RATING.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average"],show_hist=False)

fig.show()