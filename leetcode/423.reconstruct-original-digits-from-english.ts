// @leet start
function originalDigits(s: string): string {
  const A_CODE_POINT = "a".codePointAt(0);
  const E_OFFSET = 4;
  const G_OFFSET = 6;
  const F_OFFSET = 5;
  const I_OFFSET = 8;
  const H_OFFSET = 7;
  const O_OFFSET = 14;
  const N_OFFSET = 13;
  const S_OFFSET = 18;
  const R_OFFSET = 17;
  const U_OFFSET = 20;
  const T_OFFSET = 19;
  const W_OFFSET = 22;
  const V_OFFSET = 21;
  const X_OFFSET = 23;
  const Z_OFFSET = 25;

  // Get char counts
  const charCounts = Array(26).fill(0);

  for (const ch of s) {
    charCounts[ch.codePointAt(0) - A_CODE_POINT]++;
  }

  // Get num counts
  const numCounts = Array(10).fill(0);

  let target = Z_OFFSET;

  while (charCounts[target]) {
    numCounts[0]++;

    charCounts[Z_OFFSET]--;
    charCounts[E_OFFSET]--;
    charCounts[R_OFFSET]--;
    charCounts[O_OFFSET]--;
  }

  target = X_OFFSET;

  while (charCounts[target]) {
    numCounts[6]++;

    charCounts[S_OFFSET]--;
    charCounts[I_OFFSET]--;
    charCounts[X_OFFSET]--;
  }

  target = W_OFFSET;

  while (charCounts[target]) {
    numCounts[2]++;

    charCounts[T_OFFSET]--;
    charCounts[W_OFFSET]--;
    charCounts[O_OFFSET]--;
  }

  target = G_OFFSET;

  while (charCounts[target]) {
    numCounts[8]++;

    charCounts[E_OFFSET]--;
    charCounts[I_OFFSET]--;
    charCounts[G_OFFSET]--;
    charCounts[H_OFFSET]--;
    charCounts[T_OFFSET]--;
  }

  target = H_OFFSET;

  while (charCounts[target]) {
    numCounts[3]++;

    charCounts[T_OFFSET]--;
    charCounts[H_OFFSET]--;
    charCounts[R_OFFSET]--;
    charCounts[E_OFFSET] -= 2;
  }

  target = S_OFFSET;

  while (charCounts[target]) {
    numCounts[7]++;

    charCounts[S_OFFSET]--;
    charCounts[E_OFFSET] -= 2;
    charCounts[V_OFFSET]--;
    charCounts[N_OFFSET]--;
  }

  target = V_OFFSET;

  while (charCounts[target]) {
    numCounts[5]++;

    charCounts[F_OFFSET]--;
    charCounts[I_OFFSET]--;
    charCounts[V_OFFSET]--;
    charCounts[E_OFFSET]--;
  }

  target = F_OFFSET;

  while (charCounts[target]) {
    numCounts[4]++;

    charCounts[F_OFFSET]--;
    charCounts[O_OFFSET]--;
    charCounts[U_OFFSET]--;
    charCounts[R_OFFSET]--;
  }

  target = O_OFFSET;

  while (charCounts[target]) {
    numCounts[1]++;

    charCounts[O_OFFSET]--;
    charCounts[N_OFFSET]--;
    charCounts[E_OFFSET]--;
  }

  target = N_OFFSET;

  while (charCounts[target]) {
    numCounts[9]++;

    charCounts[N_OFFSET] -= 2;
    charCounts[I_OFFSET]--;
    charCounts[E_OFFSET]--;
  }

  const res: string[] = [];

  for (const [i, count] of numCounts.entries()) {
    res.push(String(i).repeat(count));
  }

  return res.join("");
}
// @leet end
