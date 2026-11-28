// Last updated: 11/28/2026, 9:25:01 AM
1class Solution {
2public:
3    int majorityElement(vector<int>& nums) {
4        int n=nums.size();
5        unordered_map<int,int> mp;
6        for(int num : nums){
7            mp[num]++;
8        }
9        for(auto [num,count]:mp){
10            if(count>(n/2)){
11                return num;
12            }
13        }
14        return 0;
15    }
16};