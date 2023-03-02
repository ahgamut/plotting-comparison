# importing the necessary packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_in_class = mpg.loc[mpg.groupby("class")["hwy"].idxmax()]

# drawing the plot
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(7, 7))
axes = axes.ravel()

# for group = color
cmap = plt.cm.jet
cmaplist = [cmap(i) for i in range(cmap.N)]
uniq_class = mpg["class"].unique()
cmaplist = cmaplist[0 : len(cmaplist) : len(cmaplist) // len(uniq_class)]
cmap = mpl.colors.LinearSegmentedColormap.from_list(
    "Custom cmap", cmaplist, len(cmaplist)
)
colors = {x: mpl.colors.to_hex(cmap(i)) for i, x in enumerate(uniq_class)}
used_cnames = set()

# for the labels
boxprops = dict(boxstyle="round", facecolor="white", alpha=0.5)

for i, cyl in enumerate(sorted(mpg["cyl"].unique())):
    df = mpg[mpg["cyl"] == cyl]
    best = best_in_class[best_in_class["cyl"] == cyl]
    for cname, color in colors.items():
        subdf = df[df["class"] == cname]
        if cname in used_cnames:
            axes[i].scatter(subdf["displ"], subdf["hwy"], c=color)
        else:
            axes[i].scatter(subdf["displ"], subdf["hwy"], label=cname, c=color)
            used_cnames.add(cname)

    for j, row in best.iterrows():
        axes[i].text(
            row["displ"],
            row["hwy"],
            row["model"],
            verticalalignment="top",
            bbox=boxprops,
        )
    axes[i].set_title(f"cyl = {cyl}")

fig.suptitle("mpg via matplotlib: displ vs hwy, facetted via cyl")
fig.text(0.5, 0.04, "displ", ha="center", fontsize=14)
fig.text(0.04, 0.5, "hwy", va="center", rotation="vertical", fontsize=14)
plt.figlegend(loc="lower center", ncol=1 + len(uniq_class) // 2)

# saving the plot
plt.savefig("./mpl_lowlevel.pdf")
