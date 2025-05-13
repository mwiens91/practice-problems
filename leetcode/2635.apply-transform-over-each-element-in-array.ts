const map = (arr: number[], fn: (n: number, i: number) => number): number[] => {
  const tranformedArray = arr.slice();

  for (let i = 0; i < arr.length; i++) {
    tranformedArray[i] = fn(arr[i], i);
  }

  return tranformedArray;
};
