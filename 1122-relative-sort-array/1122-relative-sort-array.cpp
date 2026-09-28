class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> freq;

        // Count frequency
        for (int x : arr1) {
            freq[x]++;
        }

        vector<int> ans;

        // Follow arr2 order
        for (int x : arr2) {
            while (freq[x] > 0) {
                ans.push_back(x);
                freq[x]--;
            }
        }

        // Remaining elements in ascending order
        for (auto p : freq) {
            while (p.second > 0) {
                ans.push_back(p.first);
                p.second--;
            }
        }

        return ans;
    }
};