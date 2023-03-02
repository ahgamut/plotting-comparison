# importing the necessary packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from plotnine import (
    aes,
    facet_wrap,
    ggplot,
    geom_point,
    geom_label,
    geom_smooth,
    labeller,
    theme,
    guides,
    guide_legend,
    labs,
)

plt.style.use("ggplot")

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_in_class = mpg.loc[mpg.groupby("class")["hwy"].idxmax()]

plot = (
    ggplot(mpg, mapping=aes(x="displ", y="hwy", color="class"))
    + geom_point(size=3)
    + facet_wrap("~ cyl", labeller=labeller(cols=lambda x: f"cyl = {x}"))
    + geom_label(
        aes(label="model"), size=10, alpha=0.5,
        color="black", data=best_in_class
    )
    + geom_smooth(se=False, color="blue")
    + theme(legend_position="bottom", figure_size=(9, 9))
    + guides(colour=guide_legend(nrow=1, override_aes=dict(size=4)))
    + labs(title="mpg via plotnine: displ vs hwy, facetted via cyl")
)

# saving the figure
fig = plot.draw(show=False)
plt.savefig("./plotnine_basic.pdf")
