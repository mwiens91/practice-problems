function checkIfInstanceOf(obj: any, classFunction: any): boolean {
  // Edge case: obj is null or undefined or classFunction is not a
  // function
  if (
    obj === null ||
    obj === undefined ||
    typeof classFunction !== "function"
  ) {
    return false;
  }

  return Object(obj) instanceof classFunction;
}

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
