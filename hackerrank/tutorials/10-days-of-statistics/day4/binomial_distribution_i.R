#!/usr/bin/env Rscript

BinomialDistribution <- function(x, n, p) {
  return(choose(n, x) * p^x * (1 - p)^(n - x))
}

# Parse "input" variables (actually hardcoded)
ratio.boy.to.girl <- 1.09
num.children.exact <- 6
num.boys.at.least <- 3

# Compute probability of a boy
probability.boy <- ratio.boy.to.girl / (1 + ratio.boy.to.girl)

# Compute the result
result <- 0

for (boys in num.boys.at.least:num.children.exact) {
  result <- result + BinomialDistribution(boys, num.children.exact, probability.boy)
}

# Print the result
cat(format(round(result, 3), nsmall=3), sep="\n")
