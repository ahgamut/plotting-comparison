# importing the necessary packages
library(ggplot2)
library(ggrepel)
library(dplyr)

# loading the data
mpg <- read.csv("./mpg.csv", header=T,
                colClasses=c("factor", "factor", "numeric", "integer",
                             "factor", "factor", "factor",
                             "integer", "integer", "factor", "factor")
                )
best_in_class <- mpg %>% group_by(class) %>%
    filter(row_number(desc(hwy)) == 1)

cyl.labs <- sapply(levels(mpg$cyl), FUN=function(x) sprintf("cyl = %s", x))
names(cyl.labs) <- levels(mpg$cyl)
print(cyl.labs)

# making the plot
plot <- ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(colour = class)) +
  facet_wrap(~ cyl, labeller = labeller(cyl = cyl.labs)) +
  geom_point(size = 3, shape = 1, data = best_in_class) +
  ggrepel::geom_label_repel(aes(label = model), data = best_in_class) +
  geom_smooth(se = FALSE) + theme(legend.position = "bottom") +
  guides(colour = guide_legend(nrow = 1, override.aes = list(size = 4))) +
  labs(
    title = "mpg via ggplot2: displ vs hwy, facetted via cyl",
  )

# saving the data
ggsave("base_ggplot2.pdf", plot=plot)
