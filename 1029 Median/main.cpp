#include "iostream"
#include "queue"
#include "climits"

// 这道题卡时间、卡空间，所以最后只能用队列来做，第一行全部读取到队列里
// 第二行读一个处理一个，读进来就比大小，删除比他小的数字，一直删到中位数就完事

using namespace std;
int n, m;
queue<int> queue1;

void init() {
    int tmp;
    cin >> n;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tmp);
        queue1.push(tmp);
    }
    queue1.push(INT_MAX);
    cin >> m;
}


int main() {
    init();
    int k = (m + n) / 2;
    if ((m + n) % 2 == 1) {
        k = (m + n + 1) / 2;
    }
    int tmp;
    while (true){
        break;
    }
    for (int i = 0; i < m; i++) {
        scanf("%d", &tmp);
        while(k > 1){
            if(tmp >= queue1.front()){
                queue1.pop();
                k--;
            } else{
                break;
            }
        }
        if( k == 1){
            if (tmp < queue1.front()){
                cout << tmp;
            } else{
                cout << queue1.front();
            }
            exit(0);
        }
        k -- ;
    }
    while (k > 1){
        queue1.pop();
        k--;
    }
    cout << queue1.front();
    return 0;
}










//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int n, m;
//int line1[200001]={0};
//int line2[200001]={0};
//
//void init() {
//    cin >> n;
//    for (int i = 0; i < n; i++) {
//        scanf("%d", &line1[i]);
//    }
//    cin >> m;
//    for (int i = 0; i < m; i++) {
//        scanf("%d", &line2[i]);
//    }
//}
//
//
//int findKth(int left1, int left2, int k){
//    if (left1 >= n) return line2[left2 + k - 1];
//    if (left2 >= m) return line1[left1 + k - 1];
//    if (k == 1) return min(line1[left1], line2[left2]);
//    long long mid1 = left1 + k / 2 - 1 < n ? line1[left1 + k / 2 - 1] : INT64_MAX;
//    long long mid2 = left2 + k / 2 - 1 < m ? line2[left2 + k / 2 - 1] : INT64_MAX;
//    if (mid1 < mid2){
//        return findKth(left1 + k / 2, left2, k - k / 2);
//    } else{
//        return findKth(left1, left2 + k / 2, k - k / 2);
//    }
//}
//
//int main() {
//    init();
//    if ((m + n) % 2 == 0){
//        cout << findKth(0, 0, (m + n) / 2);
//    } else{
//        cout << findKth(0, 0, (m + n + 1) / 2);
//    }
//    return 0;
//}