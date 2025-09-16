package DSA_practice.leetcode_solutions.Graphs;


import java.util.*;

class Tuple {
    int distance;
    int node;

    Tuple(int distance, int node) {
        this.distance = distance;
        this.node = node;
    }
}

public class Dijkstra {

    static int[] dijkstra_Algo(int v, ArrayList<ArrayList<ArrayList<Integer>>> adj, int src) {
        PriorityQueue<Tuple> pq = new PriorityQueue<>((x, y) -> x.distance - y.distance);

        int[] dist = new int[v];
        Arrays.fill(dist, (int) 1e9);

        dist[src] = 0;
        pq.add(new Tuple(0, src));

        while (!pq.isEmpty()) {
            Tuple it = pq.poll();
            int dis = it.distance;
            int node = it.node;

            for (int i = 0; i < adj.get(node).size(); i++) {
                int adjNode = adj.get(node).get(i).get(0);
                int edgeWt = adj.get(node).get(i).get(1);

                if (dis + edgeWt < dist[adjNode]) {
                    dist[adjNode] = dis + edgeWt;
                    pq.add(new Tuple(dist[adjNode], adjNode));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        int v = 6;
        ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<>();

        for (int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }

        // Add edges: (node, weight)
        adj.get(0).add(new ArrayList<>(Arrays.asList(1, 2)));
        adj.get(0).add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.get(1).add(new ArrayList<>(Arrays.asList(2, 1)));
        adj.get(1).add(new ArrayList<>(Arrays.asList(3, 7)));
        adj.get(2).add(new ArrayList<>(Arrays.asList(4, 3)));
        adj.get(3).add(new ArrayList<>(Arrays.asList(4, 1)));
        adj.get(4).add(new ArrayList<>(Arrays.asList(5, 5)));

        int src = 0;
        int dest = 5;

        int[] shortestDistances = dijkstra_Algo(v, adj, src);

        if (shortestDistances[dest] == (int) 1e9) {
            System.out.println("No path exists from " + src + " to " + dest);
        } else {
            System.out.println("Shortest distance from " + src + " to " + dest + " = " + shortestDistances[dest]);
        }
    }
}
