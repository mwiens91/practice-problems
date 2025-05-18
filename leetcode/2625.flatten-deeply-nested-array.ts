type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (
  arr: MultiDimensionalArray,
  n: number,
): MultiDimensionalArray {
  const arrayStack = [arr];
  const indexStack = [0];

  const flattened: MultiDimensionalArray = [];

  while (arrayStack.length > 0) {
    const topArray = arrayStack[arrayStack.length - 1];
    const topIndex = indexStack[indexStack.length - 1];

    // Pop from stacks if the top stack index is out of bounds
    if (topIndex >= topArray.length) {
      arrayStack.pop();
      indexStack.pop();

      continue;
    }

    // If current element is a number push it to the flattened
    // array. Otherwise the current element is an array: if the current
    // depth is greater than or equal to n, we push it to the flattened
    // array; otherwise we push it to the stack.
    const depth = arrayStack.length - 1;

    if (typeof topArray[topIndex] === "number" || depth >= n) {
      flattened.push(topArray[topIndex]);

      indexStack[indexStack.length - 1] += 1;
    } else {
      // Increment the index of the parent array
      indexStack[indexStack.length - 1] += 1;

      // Push child array to the stack
      arrayStack.push(topArray[topIndex]);
      indexStack.push(0);
    }
  }

  return flattened;
};
