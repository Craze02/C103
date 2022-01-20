import pandas as pd
import plotly.express as px

df = pd.read_csv("C103/bar_chart.csv")
fig = px.bar(df, x = 'Country',y = 'InternetUsers')
fig.show()