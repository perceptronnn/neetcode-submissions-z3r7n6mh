/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string str = "";
        //TreeNode* p = root;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()) {
            auto top = q.front();
            q.pop();
            if(top) {
                str += to_string(top->val);
                q.push(top->left);
                q.push(top->right); 
            }
            else
                str += 'N';            
            str += ' ';                       
        }

        cout << str;
        return str;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        TreeNode* root = NULL;
        string str = "";
        queue<TreeNode*> q;
        ss >> str;
        if(str == "N") {
            return root;
        }
        root = new TreeNode(stoi(str));
        q.push(root);

        while(!q.empty()) {
            auto top = q.front();
            q.pop();
            ss >> str;
            top->left = NULL;
            if(str != "N") {
                top->left =  new TreeNode(stoi(str));
                q.push(top->left);
            }
            ss >> str;
            top->right = NULL;
            if(str != "N") {
                top->right = new TreeNode(stoi(str));
                q.push(top->right);
            }
        }
        return root;
    }
};
