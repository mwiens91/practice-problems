type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  private callbackMap: Record<string, Callback[]>;

  constructor() {
    this.callbackMap = {};
  }

  subscribe(eventName: string, callback: Callback): Subscription {
    if (!this.callbackMap.hasOwnProperty(eventName)) {
      this.callbackMap[eventName] = [];
    }

    this.callbackMap[eventName].push(callback);

    return {
      unsubscribe: () => {
        this.callbackMap[eventName] = this.callbackMap[eventName].filter(
          (fn) => fn !== callback,
        );
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    if (this.callbackMap.hasOwnProperty(eventName)) {
      return this.callbackMap[eventName].map((fn) => fn(...args));
    }

    return [];
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
