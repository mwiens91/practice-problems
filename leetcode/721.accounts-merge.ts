// @leet start
function accountsMerge(accounts: string[][]): string[][] {
  // DSU implementation. Note:
  //
  // 1. the find method creates a new set if an email doesn't have a set
  // 2. the union method takes in any emails, it doesn't need to have
  //    the roots passed in
  // 3. the implementation uses union-by-size and path compression
  const rank = new Map<string, number>();
  const parent = new Map<string, string>();

  const find = (e: string): string => {
    if (!parent.has(e)) {
      parent.set(e, e);
      rank.set(e, 1);

      return e;
    }

    if (parent.get(e) !== e) {
      parent.set(e, find(parent.get(e)!));
    }

    return parent.get(e)!;
  };

  const union = (e1: string, e2: string) => {
    const e1Root = find(e1);
    const e2Root = find(e2);

    if (e1Root === e2Root) {
      return;
    }

    const [smallerRoot, largerRoot] =
      rank.get(e1Root)! < rank.get(e2Root)!
        ? [e1Root, e2Root]
        : [e2Root, e1Root];
    parent.set(smallerRoot, largerRoot);
    rank.set(largerRoot, rank.get(smallerRoot)! + rank.get(largerRoot)!);
  };

  // Find parents of each email
  const emailNameMap = new Map<string, string>();

  for (const account of accounts) {
    for (let i = 1; i < account.length; i++) {
      union(account[1], account[i]);
      emailNameMap.set(account[i], account[0]);
    }
  }

  // For each root parent, gather all emails
  const rootEmailsMap = new Map<string, string[]>();

  for (const email of parent.keys()) {
    const root = find(email);

    if (!rootEmailsMap.has(root)) {
      rootEmailsMap.set(root, []);
    }

    rootEmailsMap.get(root)!.push(email);
  }

  return Array.from(rootEmailsMap.values()).map((emails) => [
    emailNameMap.get(emails[0])!,
    ...emails.sort(),
  ]);
}
// @leet end
