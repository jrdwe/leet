#include <stdlib.h>

struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
};

int counter(struct TreeNode* root) {
  if (root == NULL)
    return 0;

  return counter(root->left) + counter(root->right) + 1; 
}

void inorder(struct TreeNode* root, int* arr, int* s) {
  if (root != NULL) {
    inorder(root->left, arr, s);
    arr[(*s)++] = root->val;
    inorder(root->right, arr, s);
  }
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
  int cnt = counter(root);
  int* arr = malloc(sizeof(int) * cnt);

  *returnSize = 0;
  inorder(root, arr, returnSize);

  return arr;
}
