#!/usr/bin/env Rscript

PoissonDistribution <- function(k, lambda) {
  return(lambda^k * exp(1)^(-lambda) / factorial(k))
}

# Parse "input" variables (actually hardcoded)
poisson.mean <- 2.5
poisson.actual <- 5

# Compute probability
result <- PoissonDistribution(poisson.actual, poisson.mean)

# Print the result
cat(format(round(result, 3), nsmall=3), sep="\n")
