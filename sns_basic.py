# importing the necessary packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_indices = list(mpg.groupby("class")["hwy"].idxmax())
mpg["index"] = mpg.index
mpg["text"] = mpg.apply(
    lambda x: x["model"] if x["index"] in best_indices else "", axis=1
)

# drawing the plot
fig = plt.figure(figsize=(7, 7))
p = (
    so.Plot(mpg, x="displ", y="hwy", color="class", text="text")
    .on(fig)
    .facet(col="cyl", wrap=2)
    .share(x=True, y=True)
    .add(so.Dots(pointsize=5))
    .add(so.Line(), so.PolyFit(), color=None)
    .add(so.Text(fontsize=10), color=None)
    .label(
        x="",
        y="",
        title="cyl = {}".format,
    )
)
p.plot()


fig.text(0.5, 0.04, "displ", ha="center", fontsize=14)
fig.text(0.04, 0.5, "hwy", va="center", rotation="vertical", fontsize=14)
fig.suptitle("mpg via seaborn: displ vs hwy, facetted via cyl")

# save the figure
fig.savefig("./sns_basic.pdf")
