class Solution {
public:
    cn.example.string convertToTitle(int n) {
        cn.example.string res;
        while(n>0){
            int k=(n-1)%26;
            n=(n-1)/26;
            res.push_back('A'+k);
        }
        reverse(res.begin(),res.end());
        return res;
    }
};