class TimeLimitedCache {
  private props: Record<number, [number, ReturnType<typeof setTimeout>]>;

  constructor() {
    this.props = {};
  }

  set(key: number, value: number, duration: number): boolean {
    const hadKey = this.props.hasOwnProperty(key);

    // If the key already exists cancel the scheduled deletion and
    // delete it now
    if (hadKey) {
      clearTimeout(this.props[key][1]);

      delete this.props[key];
    }

    this.props[key] = [
      value,
      setTimeout(() => delete this.props[key], duration),
    ];

    // Return whether the key already existed
    return hadKey;
  }

  get(key: number): number {
    if (this.props.hasOwnProperty(key)) {
      return this.props[key][0];
    }

    return -1;
  }

  count(): number {
    return Object.keys(this.props).length;
  }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
