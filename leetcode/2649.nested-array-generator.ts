type MultidimensionalArray = (MultidimensionalArray | number)[];

function* inorderTraversal(
  arr: MultidimensionalArray,
): Generator<number, void, unknown> {
  // Put non-number[] multidimensional arrays on a stack and the index
  // we're currently at with them
  const arrStack: MultidimensionalArray[] = [arr];
  const idxStack = [0];

  while (arrStack.length > 0) {
    const topArr = arrStack[arrStack.length - 1];
    const topIdx = idxStack[idxStack.length - 1];

    // Pop arrays we've consumed
    if (topArr.length <= topIdx) {
      arrStack.pop();
      idxStack.pop();

      continue;
    }

    // Get the current element and increment the index. If the current
    // element is an array, push it. If it's a number, yield it.
    const currentElement = topArr[topIdx];

    idxStack[idxStack.length - 1] += 1;

    if (Array.isArray(currentElement)) {
      arrStack.push(currentElement);
      idxStack.push(0);
    } else {
      yield currentElement;
    }
  }
}

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
