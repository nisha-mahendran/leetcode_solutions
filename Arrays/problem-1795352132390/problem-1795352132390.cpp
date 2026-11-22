// Last updated: 11/22/2026, 6:25:32 PM
1class Solution {
2public:
3    bool containsDuplicate(vector<int>& nums) {
4        unordered_map<int,int> mp;
5        for (int i=0;i<nums.size();i++){
6            if (mp.find(nums[i])!=mp.end()){
7                return true;
8            }
9            mp[nums[i]]=i;
10        }
11        return false;
12    }
13};