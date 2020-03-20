#include <iostream>
using namespace std;

 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 class Solution {
 public:
	 int rangeSumBST(TreeNode* root, int L, int R) {
		 if (root != NULL) {
			 int sum = rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
			 return root->val <= R && root->val >= L ? sum + root->val : sum;
		 }
		 return 0;

	 }
 };