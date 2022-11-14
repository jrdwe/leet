#include <stdio.h>
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

void preorder(struct TreeNode* root, int* arr, int* s) {
  if (root != NULL) {
    arr[(*s)++] = root->val;
    preorder(root->left, arr, s);
    preorder(root->right, arr, s);
  }
}

int* preorderTraversal(struct TreeNode* root, int* returnSize){
  int cnt = counter(root);
  int* arr = malloc(sizeof(int) * cnt);

  *returnSize = 0;
  preorder(root, arr, returnSize);

  return arr;
}
