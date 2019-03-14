#include <utility>
#include "set"
#include <iostream>
#include "map"
#include "string"
using namespace std;
// start time: 2019-02-21 19-39-56 周四
// end time: 2019-02-21 20-09-44 周四
// 坑：1. string不能作为类的参数，我懒得研究为什么。  2. 获取string首字母的办法是string.at(0)
//     3. scanf读取string的办法是先用resize确定string大小

class MyNode {
public:
    string addr;
    string next_addr;

    MyNode() = default;
};

int n;
string start1, start2;
map<string, MyNode> hash_map;
set<string> route;


int main() {
    cin >> start1 >> start2 >> n;
    string addr, next_addr, letter;
    addr.resize(5);
    next_addr.resize(5);
    letter.resize(1);
    for (int i = 0; i < n; ++i) {
        scanf("%s %s %s", &addr[0], &letter[0], &next_addr[0]);
        MyNode node;
        node.next_addr = next_addr;
        node.addr = addr;
        hash_map[addr] = node;
    }
    string cur_addr = start1;
    while (cur_addr.at(0) != '-') {
        route.insert(cur_addr);
        cur_addr = hash_map[cur_addr].next_addr;
    }
    cur_addr = start2;
    while (cur_addr.at(0) != '-') {
        if (route.find(cur_addr) != route.end()) {
            cout << cur_addr;
            exit(0);
        }
        cur_addr = hash_map[cur_addr].next_addr;
    }
    cout << -1;
    return 0;
}