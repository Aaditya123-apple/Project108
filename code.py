import pandas as pd
import plotly.express as px
import csv
import plotly.figure_factory as ff

df=pd.read_csv('student.csv')

fig=ff.create_distplot([df['Avg Rating'].to_list()],['Avg Rating'])
fig.show()
