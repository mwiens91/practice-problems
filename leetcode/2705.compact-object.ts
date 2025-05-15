type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

const isObject = (
  value: JSONValue,
): value is Record<string, JSONValue> | JSONValue[] =>
  typeof value === "object" && value !== null;

function compactObject(obj: Obj): Obj {
  if (Array.isArray(obj)) {
    const newObj: JSONValue[] = [];

    for (const element of obj) {
      if (isObject(element)) {
        newObj.push(compactObject(element));
      } else if (element) {
        newObj.push(element);
      }
    }

    return newObj;
  }

  // obj is a record
  const newObj: Record<string, JSONValue> = {};

  for (const [key, value] of Object.entries(obj)) {
    if (isObject(value)) {
      newObj[key] = compactObject(value);
    } else if (value) {
      newObj[key] = value;
    }
  }

  return newObj;
}
