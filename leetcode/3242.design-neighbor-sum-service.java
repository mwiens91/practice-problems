// @leet start
import java.util.HashMap;
import java.util.Map;

class NeighborSum {
    private final int[][] grid;
    private final int n;
    private final Map<Integer, int[]> valToIdxs;

    public NeighborSum(int[][] grid) {
        this.grid = grid;
        n = grid.length;

        valToIdxs = new HashMap<>();

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                valToIdxs.put(grid[y][x], new int[]{x, y});
            }
        }
    }

    public int adjacentSum(int value) {
        int[] idxs = valToIdxs.get(value);
        int x = idxs[0];
        int y = idxs[1];

        return (
            (x > 0 ? grid[y][x - 1] : 0)
            + (x < n - 1 ? grid[y][x + 1] : 0)
            + (y > 0 ? grid[y - 1][x] : 0)
            + (y < n - 1 ? grid[y + 1][x] : 0)
        );
    }

    public int diagonalSum(int value) {
        int[] idxs = valToIdxs.get(value);
        int x = idxs[0];
        int y = idxs[1];

        return (
            ((x > 0) && (y > 0) ? grid[y - 1][x - 1] : 0)
            + ((x < n - 1) && (y > 0) ? grid[y - 1][x + 1] : 0)
            + ((x > 0) && (y < n - 1) ? grid[y + 1][x - 1] : 0)
            + ((x < n - 1) && (y < n - 1) ? grid[y + 1][x + 1] : 0)
        );
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */
// @leet end
