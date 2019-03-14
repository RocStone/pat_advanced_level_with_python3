#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 坑：注意python可以直接用int转化结果，c++可不行，我需要一位一位的处理数字，不输出开头的0
//     另外，当整个数字就是0时，需要专门输出一个0，否则不输出任何东西会导致一个测试点错误


bool cmp(string a, string b){
    return (a + b) < (b + a);
}

int main() {
    int n = 0;
    cin >> n;
    vector<string> numbers;
    for(int i =0; i < n ; i++){
        string s;
        cin >> s;
        numbers.push_back(s);
    }
    sort(numbers.begin(), numbers.end(), cmp);
    bool handing_zero = true;
    for(string &s : numbers){
        for(char &c: s){
            if( handing_zero and c == '0'){
                continue;
            } else{
                handing_zero = false;
                printf("%c", c);
            }
        }
    }
    if (handing_zero){
        printf("0");
    }
    return 0;
}
