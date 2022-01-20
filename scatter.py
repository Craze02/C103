import pandas as pd
import plotly.express as px

df = pd.read_csv("C103/bar_chart.csv")
fig = px.scatter(df,x = "Population", y = "Per capita",size = "Percentage", color = "Country", size_max = 60 )
fig.show()