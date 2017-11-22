#!/usr/bin/env R

png(filename = "Rplot%03d.png")
d <- read.csv("http://www.cyclismo.org/tutorial/R/_static/simple.csv",header=TRUE)
plot(velocity~mass,d)
dev.off()
