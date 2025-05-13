type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  const chunkArr: Obj[][] = [];

  let currentChunk: Obj[] = [];

  for (const elem of arr) {
    currentChunk.push(elem);

    if (currentChunk.length >= size) {
      // Push the chunk to the chunked array and reset the chunk
      chunkArr.push(currentChunk);
      currentChunk = [];
    }
  }

  // Push the last chunk if it's non-empty
  if (currentChunk.length > 0) {
    chunkArr.push(currentChunk);
  }

  return chunkArr;
}
