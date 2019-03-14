#include <iostream>
#include "vector"

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int d[N];
    int ds[N + 1];
    ds[0] = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d", &d[i]);
        ds[i + 1] = d[i] + ds[i];
    }

    vector<string> wrong_ans, right_ans;
    int wrong_diff = INTMAX_MAX;
    bool find_ans = false;

    int i = 0, j = 0;
    while (i < N + 1 and j < N + 1 and i <= j) {
        if (ds[j] - ds[i] < M) {
            j += 1;
        } else if (ds[j] - ds[i] == M) {
            right_ans.push_back(to_string(i + 1) + "-" + to_string(j));
            find_ans = true;
            j++;
            i++;
        } else {
            if (not find_ans) {
                if (wrong_diff > ds[j] - ds[i]) {
                    wrong_ans.clear();
                    wrong_ans.push_back(to_string(i + 1) + "-" + to_string(j));
                    wrong_diff = ds[j] - ds[i];
                } else if (wrong_diff == ds[j] - ds[i]) {
                    wrong_ans.push_back(to_string(i + 1) + "-" + to_string(j));
                }
            }
            i++;
        }
    }
    if (find_ans){
        for(string &s: right_ans){
            cout << s << endl;
        }
    } else{
        for(string &s: wrong_ans){
            cout << s << endl;
        }
    }

    return 0;
}