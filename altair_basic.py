# importing the necessary packages
import pandas as pd
import altair as alt

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_in_class = mpg.loc[mpg.groupby("class")["hwy"].idxmax()]

fig = (
    alt.Chart(mpg)
    .properties(title="mpg via altair: displ vs hwy, facetted via cyl")
    .encode(x="displ", y="hwy", color="class")
    .mark_point()
    .facet("cyl:N", columns=2)
    .configure_title(fontSize=20, font="Courier", anchor="start", color="gray")
)


alt.Chart.save(fig, "altair_basic.json")
