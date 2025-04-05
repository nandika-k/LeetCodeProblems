class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // sort values
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 1; i++) {
            // check if curr == next
            if (nums[i] == nums[i+1]) return true;
        }
        return false;
    }
};
