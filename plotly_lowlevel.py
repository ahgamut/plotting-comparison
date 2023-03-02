# importing the necessary packages
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_indices = list(mpg.groupby("class")["hwy"].idxmax())
mpg["index"] = mpg.index
mpg["text"] = mpg.apply(
    lambda x: x["model"] if x["index"] in best_indices else "", axis=1
)

# how do I know the right amount of rows?!
fig = make_subplots(
    rows=2,
    cols=2,
    shared_xaxes=True,
    shared_yaxes=True,
    x_title="displ",
    y_title="hwy",
    subplot_titles=["cyl = {}".format(x) for x, _ in mpg.groupby("cyl")],
)
subplot_indices = [
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
]

cnames = list(mpg["class"].unique())
used_cnames = set()
colors = ["black", "red", "green", "gray", "goldenrod", "magenta", "cyan"]

for i, (cyl, subdf) in enumerate(mpg.groupby("cyl")):
    row, col = subplot_indices[i]
    for (cname, sdf2) in subdf.groupby("class"):
        fig.add_trace(
            go.Scatter(
                x=sdf2["displ"],
                y=sdf2["hwy"],
                mode="markers+text",
                text=sdf2["text"],
                textposition="bottom center",
                name=cname,
                marker_color=colors[cnames.index(cname)],
                showlegend=cname not in used_cnames,
            ),
            row=row,
            col=col,
        )
        used_cnames.add(cname)

fig.update_layout(
    height=800,
    width=800,
    title_text="mpg via plotly: displ vs hwy, facetted via cyl",
    legend=dict(
        title_text="class",
        yanchor="bottom",
        y=-0.15,
        xanchor="center",
        x=0.5,
        orientation="h",
    ),
)

# save the figure
# fig.show()
fig.write_image("./plotly_lowlevel.pdf")
