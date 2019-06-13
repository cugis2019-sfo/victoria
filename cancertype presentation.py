import pandas
import plotly
import pandas as pd
df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")
from plotly.offline import plot
import plotly.graph_objs as go
cancercases = go.Bar(x= df["CancerType"], y=df["Number"], marker = {"color": df["Number"], "colorscale" : "Jet"})
plot([cancercases])

titles = go.Layout(
                    title = "Number of Women Cancer Case By Type",
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text="CancerType",
                        )
                    ),
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="Number",
                            )
                      )
                    )

fig= go.Figure(data=[cancercases], layout = titles)
plot(fig)
