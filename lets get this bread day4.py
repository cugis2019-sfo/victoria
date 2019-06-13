import pandas
import plotly
studentlist = [["Steve", 32, "Male"], ["Lia", 28, "Female"], ["Vin", 45, "Male"], ["Katie", 38, "Female"]]
studentlistdf = pandas.DataFrame(studentlist, columns=["Name", "Age", "Gender"], index = ["1", "2", "3", "4"])
print(studentlistdf)

dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

agenamegender = go.Bar(x=studentlistdf["Name"], y=studentlistdf["Age"])


plot([agenamegender])
 
import pandas as pd
df = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
 womenoccupation = go.Bar(x= df["occupation"], y=df["women"], marker = {"color": df["women"], "colorscale" : "Jet"})
plot([womenoccupation])

titles = go.Layout(
                    title = "Percentage of Women Employed by Occupation",
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text="Occupation",
                        )
                    ),
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="Percentage",
                            )
                      )
                    )

fig= go.Figure(data=[womenoccupation], layout = titles)
plot(fig)
