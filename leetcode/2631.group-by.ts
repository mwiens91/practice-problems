type GroupingFn<T> = (item: T) => string;

interface Array<T> {
  groupBy(fn: GroupingFn<T>): Record<string, T[]>;
}

Array.prototype.groupBy = function <T>(this: T[], fn: GroupingFn<T>) {
  const groupedObj: Record<string, T[]> = {};

  for (const elem of this) {
    const key = fn(elem);

    if (!Object.prototype.hasOwnProperty.call(groupedObj, key)) {
      groupedObj[key] = [];
    }

    groupedObj[key].push(elem);
  }

  return groupedObj;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
