// Problem: Two Sum
// Platform: neetcode
// Difficulty: Easy
// Language: c++
// Synced: 2026-05-23T08:29:33.313Z
Code  |  C++Visualize codeShare Solutionclass Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> memo;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (memo.find(complement) != memo.end()) {
                vector<int> result;
                result.push_back(memo[complement]);
                result.push_back(i);
                return result;
            }
            else {
                memo[nums[i]] = i;
            }
        }
        return {-1, -1};
    }
};