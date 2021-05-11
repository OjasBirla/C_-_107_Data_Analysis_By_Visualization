import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("Data.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
graph = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
graph.show()