#include<iostream>
using namespace std;
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    int get_max_node(TreeNode* root, TreeNode* parent){
        if(root->right == NULL){
            int ret = root->val;
            if(parent->left == root){
                parent->left = root->left;
            }else{
                parent->right = root->left;
            }
            return ret;
        }else{
            return get_max_node(root->right, root);
        }
    }
    void remove(TreeNode* parent, TreeNode* child){
        if(child == parent->left){
            parent->left = NULL;
        }else{
            parent->right = NULL;
        }
    }
    TreeNode* deleteNode(TreeNode* root, int key, TreeNode* parent=NULL) {
        if(root == NULL){
            return root;
        }
        if(root->val == key){
            if(root->left == NULL && root->right == NULL){
                if(parent == NULL){
                    root =NULL;
                }else{
                    remove(parent, root);
                }
            }else if(root->left != NULL){
                root->val = get_max_node(root->left, root);
            }else{
                if(parent == NULL){
                    root = root->right;
                }else{
                    TreeNode* to_remove = root->right;
                    root->left = to_remove->left;
                    root->right= to_remove->right;
                    root->val = to_remove->val;
                }
            }
            
        }else if(root-> val < key){
            deleteNode(root->right, key, root);
        }else{
            deleteNode(root->left, key, root);
        }
        return root;
        
    }
};