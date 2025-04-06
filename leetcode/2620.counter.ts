const createCounter = (n: number) => {
  let count = n;

  return () => {
    const returnVal = count
    count += 1
    return returnVal;
  };
};
