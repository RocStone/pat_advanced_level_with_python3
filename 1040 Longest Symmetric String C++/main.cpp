#include <iostream>

using namespace std;

// 坑：C++里的数组使用前一定要初始化，这里的dp数组，默认就并不是false，好坑


int main() {
    string s;
    getline(cin, s);
    int ans = 0;
    bool dp[s.length()][s.length()];
    for(int i=0; i < s.length(); i ++){
        for (int j = 0; j < s.length(); ++j) {
            dp[i][j] = false;
        }
    }
    for (int i = 0; i < s.length(); ++i) {
        dp[i][i] = true;
        ans = 1;
    }
    for (int i = 0; i < s.length() - 1; ++i) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            ans = 2;
        }
    }
    for (int L = 3; L <= s.length(); L++) {
        for (int i = 0; i + L - 1 < s.length(); i++) {
            if (s[i] == s[i + L - 1] and dp[i + 1][i + L - 2]) {
                dp[i][i + L - 1] = true;
                ans = L;
            }
        }
    }
    printf("%d", ans);
    return 0;
}