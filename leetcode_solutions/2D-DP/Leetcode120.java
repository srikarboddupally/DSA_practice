import java.util.*;

class Triangle {
    public static int mem(int i,int j,List<List<Integer>> a,int n,Integer[][] dp){
        if(i==n-1){
            return a.get(i).get(j);
        }
        if(dp[i][j]!=null) return dp[i][j];

        int d=a.get(i).get(j)+mem(i+1,j,a,n,dp);
        int dg=a.get(i).get(j)+mem(i+1,j+1,a,n,dp);

        return dp[i][j]=Math.min(d,dg);
    }
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        Integer[][] dp=new Integer[n][n];
        return mem(0,0,triangle,n,dp);
    }
}
