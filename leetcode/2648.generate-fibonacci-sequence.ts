function* fibGenerator(): Generator<number, any, number> {
  // Store a = x_n and b = x_{n + 1}
  let a = 0;
  let b = 1;

  while (true) {
    // Get x_n and set a, b vals to x_{n + 1} and x_{n + 2}
    const x_n = a;

    [a, b] = [b, a + b];

    yield x_n;
  }
}
