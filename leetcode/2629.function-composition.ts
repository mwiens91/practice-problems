type F = (x: number) => number;

const compose = (functions: F[]) => (x: number) =>
  functions.reduceRight((accum, f) => f(accum), x);
