import java.util.*;
class Solution {
    public int mem(int i,int j,int[][] grid,int[][] dp){
        if(i==0&&j==0) return grid[0][0];
        if(i<0 || j<0) return (int)1e9;

        if(dp[i][j]!=-1) return dp[i][j];
        int up=grid[i][j]+mem(i-1,j,grid,dp);
        int left=grid[i][j]+mem(i,j-1,grid,dp);
        dp[i][j]=Math.min(up,left);
        return dp[i][j];
    }
    public int minPathSum(int[][] grid) {
        int i=grid.length;
        int j=grid[0].length;
        int[][] dp=new int[i][j];
        for(int[] a: dp){
            Arrays.fill(a,-1);
        }
        return mem(i-1,j-1,grid,dp);
    }
}