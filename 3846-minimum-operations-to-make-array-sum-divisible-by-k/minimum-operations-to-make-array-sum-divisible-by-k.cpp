class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int total = 0;
        for (int x: nums){
            total += x;
        }
        int count = 0;
        while (total % k != 0){
            count += 1;
            total -= 1;
        }
        return count;
    }
};