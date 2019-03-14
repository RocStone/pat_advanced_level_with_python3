#include <iostream>
#include "vector"
#include "map"

// 独立想出来，做了一小时，很爽
using namespace std;

int main() {

    int N;
    cin >> N;
    int f_color_length;
    cin >> f_color_length;
    int f_color[f_color_length];
    for (int i = 0; i < f_color_length; ++i) {
        scanf("%d", &f_color[i]);
    }
    int strip_length;
    cin >> strip_length;
    int strip[strip_length];
    for (int j = 0; j < strip_length; ++j) {
        scanf("%d", &strip[j]);
    }
    map<int, int> order;
    for (int k = 0; k < f_color_length; ++k) {
        order[f_color[k]] = k;
    }

    map<int, int> last_length;
    for (int &each : f_color) {
        last_length[each] = 0;
    }

    for (int &color: strip) {
        if (order.find(color) != order.end()) {
            int pre_max_length = 0;
            int o = order[color];
            for (int i = 0; i < o + 1; ++i) {
                if (last_length[f_color[i]] > pre_max_length) {
                    pre_max_length = last_length[f_color[i]];
                }
            }
            last_length[color] = pre_max_length + 1;
            for (int j = o + 1; j < f_color_length; ++j) {
                if (last_length[color] > last_length[f_color[j]]) {
                    last_length[f_color[j]] = last_length[color];
                }
            }
        }
    }

    int max_length = 0;
    for (auto &it : last_length) {
        if (it.second > max_length){
            max_length = it.second;
        }
    }
    cout << max_length;
    return 0;
}