import pandas as pd 
import plotly.express as px

df = pd.read_csv("C103/line_chart.csv")
fig = px.line(df,x = "Year", y = "Percapital", color = "Country", title = 'Per Capita Income')
fig.show()