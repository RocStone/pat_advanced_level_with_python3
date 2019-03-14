#include <iostream>
#include <algorithm>
#include "map"
#include "vector"
using namespace std;

//start time: 2019-02-22 15-43-34 周五
//end time: 2019-02-22 15-54-11 周五
// 坑：不能用cin，要用scanf，题目已经告诉我们人名长度为4个字符，所以string可以用scanf来提取

int main() {

    int N, K;
    cin >> N >> K;
    map<string, vector<int>> courses;
    for (int i=0; i <K; i ++){
        int no, numbers;
        scanf("%d %d", &no, &numbers);
        string name;
        name.resize(4);
        for (int j = 0; j < numbers; ++j) {
            scanf("%s", &name[0]);
            courses[name].push_back(no);
        }
    }
    string name;
    for (int i = 0; i < N; ++i) {
        cin >> name;
        printf("%s %lld", name.c_str(), courses[name].size());
        sort(courses[name].begin(), courses[name].end());
        for(int &t: courses[name]){
            printf(" %d", t);
        }
        printf("\n");
    }
    return 0;
}