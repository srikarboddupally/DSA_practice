class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int up = matrix[i][j] + matrix[i-1][j];
                int left = matrix[i][j] + (j > 0 ? matrix[i-1][j-1] : (int)1e9);
                int right = matrix[i][j] + (j < n-1 ? matrix[i-1][j+1] : (int)1e9);

                matrix[i][j] = Math.min(up, Math.min(left, right));
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            ans = Math.min(ans, matrix[n-1][j]);
        }
        return ans;
    }
}
