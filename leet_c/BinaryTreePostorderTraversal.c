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

void postorder(struct TreeNode* root, int* arr, int* s) {
  if (root != NULL) {
    postorder(root->left, arr, s);
    postorder(root->right, arr, s);
    arr[(*s)++] = root->val;
  }
}

int* postorderTraversal(struct TreeNode* root, int* returnSize){
  int cnt = counter(root);
  int* arr = malloc(sizeof(int) * cnt);

  *returnSize = 0;
  postorder(root, arr, returnSize);

  return arr;
}
