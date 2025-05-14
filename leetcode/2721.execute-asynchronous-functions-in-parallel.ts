type Fn<T> = () => Promise<T>;

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    // Handle edge case of empty input array
    const results: T[] = [];
    const requiredCount = functions.length;

    if (requiredCount === 0) {
      resolve(results);
    }

    // Normal case: resolve when we have final result or return first
    // error
    let resolvedCount = 0;

    functions.forEach((fn, i) => {
      Promise.resolve(fn())
        .then((result) => {
          // Store the result
          results[i] = result;
          resolvedCount += 1;

          // Resolve if this is the final result
          if (resolvedCount === requiredCount) {
            resolve(results);
          }
        })
        .catch((error) => reject(error));
    });
  });
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
