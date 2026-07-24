// Last updated: 24/07/2026, 11:25:19
class Solution {
public:
    int sum =0;
    int minOperations(vector<int>& nums, int k) {
       for(int num : nums){
        sum+=num;}
        return sum%k;
    }
};