// Last updated: 11/23/2026, 8:15:43 AM
1class Solution {
2public:
3    int majorityElement(vector<int>& nums) {
4        unordered_map<int,int> mp;
5        int n=nums.size();
6        for (int x : nums){
7            mp[x]++;
8            if (mp[x]>(n/2)){
9                return x;
10            }
11        }
12        return 0;
13    }
14};