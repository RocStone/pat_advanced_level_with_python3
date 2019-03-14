#include <iostream>
#include <algorithm>
#include "vector"
#include "stack"

using namespace std;
vector<int> s;
vector<vector<int>> parents(500 + 1);
int bikes[500 +1];
int Capacity, N, Problem_index, M;
long long min_out_bikes = INT64_MAX;
long long remain = 0;
vector<int> min_route;
class Edge {
public:
    int u;
    int v;
    int length;

    Edge(int u, int v, int length);
};

Edge::Edge(int u, int v, int length) {
    this->u = u;
    this->v = v;
    this->length = length;
}

void dfs(int index) {
    if (index == 0) {
        int out_bike = 0, current_remain = 0;
        for (int i = s.size() - 1; i >= 0; i --) {
            int v = s[i];
            // 车辆不足，
            if (bikes[v] < Capacity / 2){
                current_remain -= Capacity / 2 - bikes[v];
                if (current_remain < 0){
                    out_bike -= current_remain;
                    current_remain = 0;
                }
            // 车辆过多
            } else if (bikes[v] > Capacity / 2){
                current_remain += bikes[v] - Capacity / 2;
            }
        }
        if (out_bike < min_out_bikes or (out_bike == min_out_bikes and current_remain < remain)){
            min_out_bikes = out_bike;
            remain = current_remain;
            min_route.clear();
            min_route.assign(s.begin(), s.end());
            reverse(min_route.begin(), min_route.end());
        }
    }
    s.push_back(index);
    for (vector<int>::iterator it = parents[index].begin(); it != parents[index].end(); it++) {
        dfs(*it);
    }
    s.pop_back();
}


int main() {
    cin >> Capacity >> N >> Problem_index >> M;
    for (int i = 1; i <= N; ++i) {
        cin >> bikes[i];
    }
    vector<vector<Edge>> edges(N + 1);

    for (int i = 0; i < M; ++i) {
        int u, v, length;
        cin >> u >> v >> length;
        Edge edge = Edge(u, v, length);
        edges[u].push_back(edge);
        edge = Edge(v, u, length);
        edges[v].push_back(edge);
    }

    bool visited[N + 1];
    long long dist[N + 1];
    for (int i = 0; i < N + 1; ++i) {
        dist[i] = INT_FAST64_MAX;
    }
    dist[0] = 0;
    while (true) {
        // 找最近的点
        long long d = INT_FAST64_MAX;
        int index = -1;
        for (int i = 0; i < N + 1; ++i) {
            if (not visited[i] and dist[i] < d) {
                d = dist[i];
                index = i;
            }
        }
        // 访问这个点
        if (d == INT_FAST64_MAX or index == Problem_index) {
            break;
        }
        visited[index] = true;
        // 更新与之相连的边
        long long len = edges[index].size();
        for (long long i = 0; i < len; ++i) {
            if (not visited[edges[index][i].v]) {
                if (dist[edges[index][i].v] > edges[index][i].length + dist[index]) {
                    dist[edges[index][i].v] = edges[index][i].length + dist[index];
                    parents[edges[index][i].v].clear();
                    parents[edges[index][i].v].push_back(index);
                } else if (dist[edges[index][i].v] == edges[index][i].length + dist[index]) {
                    parents[edges[index][i].v].push_back(index);
                }
            }
        }
    }
    vector<int> route;
    dfs(Problem_index);
    cout << min_out_bikes;
    cout << " 0";
    for(vector<int>::iterator it = min_route.begin(); it != min_route.end(); it ++){
        cout << "->" << *it;
    }
    cout << " " << remain << endl;
    return 0;
}
