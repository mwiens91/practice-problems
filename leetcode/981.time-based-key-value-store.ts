// @leet start
class TimeMap {
  private readonly map = new Map<string, [number, string][]>();

  set(key: string, value: string, timestamp: number): void {
    if (!this.map.has(key)) {
      this.map.set(key, []);
    }

    this.map.get(key)!.push([timestamp, value]);
  }

  get(key: string, timestamp: number): string {
    const vals = this.map.get(key);

    if (!vals || vals[0][0] > timestamp) {
      return "";
    }

    let lo = 0;
    let hi = vals.length - 1;

    while (lo <= hi) {
      const mid = Math.floor((lo + hi) / 2);

      if (vals[mid][0] <= timestamp) {
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }

    return vals[hi][1];
  }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
// @leet end
