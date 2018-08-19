#!/usr/bin/env Rscript

BinomialDistribution <- function(x, n, p) {
  return(choose(n, x) * p^x * (1 - p)^(n - x))
}

# Parse "input" variables (actually hardcoded)
probability.piston.reject <- 0.12
total.pistons <- 10

# Compute the results
probability.no.more.than.2.rejects <- 0
probability.at.least.2.rejects <- 0

for (rejects in 0:2) {
  probability.no.more.than.2.rejects <- (probability.no.more.than.2.rejects
                                         + BinomialDistribution(
                                            rejects,
                                            total.pistons,
                                            probability.piston.reject))
}

for (rejects in 2:total.pistons) {
  probability.at.least.2.rejects <- (probability.at.least.2.rejects
                                     + BinomialDistribution(
                                        rejects,
                                        total.pistons,
                                        probability.piston.reject))
}

# Print the results
cat(format(round(probability.no.more.than.2.rejects, 3), nsmall=3), sep="\n")
cat(format(round(probability.at.least.2.rejects, 3), nsmall=3), sep="\n")
