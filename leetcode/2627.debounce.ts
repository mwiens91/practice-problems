type F = (...args: number[]) => void;

function debounce(fn: F, t: number): F {
  let ref: undefined | ReturnType<typeof setTimeout> = undefined;

  return function (...args) {
    // Clear previous call
    clearTimeout(ref);

    // Schedule this call
    ref = setTimeout(fn, t, ...args);
  };
}

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
