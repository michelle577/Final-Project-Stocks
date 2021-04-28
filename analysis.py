import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#Load data
data = pd.read_csv("C:/Users/Michele/Desktop/project/berkshire 13-f.csv")

#make a pivot table
pivot = data.pivot_table(index=["date","NAME OF ISSUER"],
                 #columns="TITLE OF CLASS",
                 values = ["SHRS OR PRN AMT","VALUE (x$1000)"],
                 aggfunc="sum").sort_values(["NAME OF ISSUER","date"])

groupbyObject = pivot.groupby(["NAME OF ISSUER"]).pct_change().reset_index()
print("e")
fig = px.scatter(pivot.reset_index(),x="date",y="SHRS OR PRN AMT",color="NAME OF ISSUER",size="VALUE (x$1000)",log_y=True)
#fig = px.line(groupbyObject,x="date",y=["SHRS OR PRN AMT","VALUE (x$1000)"],color="NAME OF ISSUER",orientation="NAME OF ISSUER")
fig.show()

