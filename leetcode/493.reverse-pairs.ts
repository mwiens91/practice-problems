// @leet start
function reversePairs(nums: number[]): number {
  return sortAndCount(nums, 0, nums.length - 1);
}

function sortAndCount(nums: number[], left: number, right: number): number {
  if (left >= right) {
    return 0;
  }

  const mid = Math.floor((left + right) / 2);
  const leftCount = sortAndCount(nums, left, mid);
  const rightCount = sortAndCount(nums, mid + 1, right);

  return leftCount + rightCount + mergeAndCount(nums, left, mid, right);
}

function mergeAndCount(
  nums: number[],
  left: number,
  mid: number,
  right: number,
): number {
  const res = count(nums, left, mid, right);
  merge(nums, left, mid, right);

  return res;
}

function count(
  nums: number[],
  left: number,
  mid: number,
  right: number,
): number {
  let res = 0;
  let rightPtr = mid + 1;

  for (let leftPtr = left; leftPtr <= mid; leftPtr++) {
    while (rightPtr <= right && nums[leftPtr] > 2 * nums[rightPtr]) {
      rightPtr++;
    }

    res += rightPtr - mid - 1;
  }

  return res;
}

function merge(nums: number[], left: number, mid: number, right: number) {
  const temp: number[] = [];
  let leftPtr = left;
  let rightPtr = mid + 1;

  while (leftPtr <= mid && rightPtr <= right) {
    nums[leftPtr] <= nums[rightPtr]
      ? temp.push(nums[leftPtr++])
      : temp.push(nums[rightPtr++]);
  }

  leftPtr <= mid
    ? temp.push(...nums.slice(leftPtr, mid + 1))
    : temp.push(...nums.slice(rightPtr, right + 1));

  for (let i = 0; i <= right - left; i++) {
    nums[left + i] = temp[i];
  }
}
// @leet end
