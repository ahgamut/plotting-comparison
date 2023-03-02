# importing the necessary packages
import pandas as pd
import plotext as plt

# loading the data
mpg = pd.read_csv("./mpg.csv", header=0)
best_in_class = mpg.loc[mpg.groupby("class")["hwy"].idxmax()]

for cname, subdf in mpg.groupby("class"):
    plt.scatter(subdf["displ"], subdf["hwy"], label=cname)

plt.title("mpg via altair: displ vs hwy")
plt.show()
# any helper functions

# loading the data

# variables

# transformations

# aesthetics

# scales and guides

# saving the data

# running the script
def main():
    pass

if __name__ == "__main__":
    main()
