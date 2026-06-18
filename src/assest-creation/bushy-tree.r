library(ape)
library(ggtree)
library(ggplot2)
library(viridis)

set.seed(42)

# Create a large tree with many tips
n_tips <- 250   # increase to 500+ for even busier
tree <- rtree(n_tips)

# Add random branch lengths variation
tree$edge.length <- abs(rnorm(length(tree$edge.length), mean = 1, sd = 0.5))

p <- ggtree(tree, layout="ellipse",
            aes(color = branch.length), size = 80) +
  scale_color_viridis(option = "inferno", direction = -1) +
  theme_tree() +
  theme(
    legend.position = "none"
  )

svg("test.svg", height = 1400, width = 590)
p
dev.off()



