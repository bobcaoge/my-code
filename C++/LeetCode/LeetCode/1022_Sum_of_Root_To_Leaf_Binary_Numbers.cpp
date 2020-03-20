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
	 int traverse(TreeNode* root, int sum) {
		 if (root == NULL) {
			 return 0;
		 }
		 if (root->left == NULL && root->right == NULL) {
			 return (sum << 1) + root->val;
		 }
		 else {
			 return traverse(root->left, (sum << 1) + root->val) + traverse(root->right, (sum << 1) + root->val);
		 }
	 }
	 int sumRootToLeaf(TreeNode* root) {
		 return traverse(root, 0);
	 }
 };