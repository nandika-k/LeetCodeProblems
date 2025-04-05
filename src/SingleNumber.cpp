class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int singleNum = 0;
        for (int num: nums) {
          // use XOR to find unique num
            singleNum ^= num;
        }
        
        return singleNum;
    }
};
