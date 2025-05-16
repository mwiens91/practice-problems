type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type ArrayType = { id: number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
  const idToObjectsMap = new Map<number, ArrayType>();

  for (const object of arr1) {
    idToObjectsMap.set(object.id, object);
  }

  for (const object of arr2) {
    const existingObject = idToObjectsMap.get(object.id);

    if (existingObject !== undefined) {
      // Merge the objects
      for (const [key, value] of Object.entries(object)) {
        existingObject[key] = value;
      }
    } else {
      // Set this object to the map
      idToObjectsMap.set(object.id, object);
    }
  }

  return [...idToObjectsMap.values()].sort((a, b) => a.id - b.id);
}
