// https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        int size = nums.size();
        vector<int> v;
        for(i=0;i<size;i++){
            for(j=i+1;j<size;j++){
                if(nums[i]+nums[j]==target){
                    v.push_back(i);
                    v.push_back(j);
                    return v;
                }
            }
        }
    }
};