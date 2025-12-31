// @leet start
import java.util.Arrays;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] mat = new int[m][n];

        for (int[] row : mat) {
            Arrays.fill(row, -1);
        }

        int minRow = 0;
        int maxRow = m - 1;
        int minCol = 0;
        int maxCol = n - 1;

        while (head != null) {
            for (int j = minCol; j <= maxCol && head != null; j++, head = head.next) {
                mat[minRow][j] = head.val;
            }

            for (int i = minRow + 1; i <= maxRow && head != null; i++, head = head.next) {
                mat[i][maxCol] = head.val;
            }

            for (int j = maxCol - 1; j >= minCol && head != null; j--, head = head.next) {
                mat[maxRow][j] = head.val;
            }

            for (int i = maxRow - 1; i > minRow && head != null; i--, head = head.next) {
                mat[i][minCol] = head.val;
            }

            minRow++;
            maxRow--;
            minCol++;
            maxCol--;
        }

        return mat;
    }
}
// @leet end
