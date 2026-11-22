// Last updated: 11/22/2026, 7:04:59 PM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        if (s.size()!=t.size()) return false;
5        unordered_map <char,int> mp;
6        for (char c : s ) mp[c]++ ;
7        for (char c : t ) {
8            mp[c]--;
9            if (mp[c]<0) return false;
10        }
11        return true;
12    };
13};