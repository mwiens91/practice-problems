type P = Promise<number>;

const addTwoPromises = async (promise1: P, promise2: P): P =>
  Promise.all([promise1, promise2]).then(([val1, val2]) => val1 + val2);

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
