#include <iostream>
#include <vector>
#include <stack>
using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
	int get_length_of_ListNode(ListNode* head) {
		int length = 0;
		while (head != NULL) {
			length++;
			head = head->next;
		}
		return length;
	}
	vector<int> nextLargerNodes(ListNode* head) {
		vector<int> ret(get_length_of_ListNode(head));
		stack<vector<int>> s;
		int index = 0;
		while (head != NULL) {
			if (s.empty()) {
				vector<int> info(2);
				info[0] = head->val;
				info[1] = index;
				s.push(info);
			}
			else {
				while (!s.empty()&&head->val > s.top()[0]) {
					ret[s.top()[1]] = head->val;
					s.pop();
				}
				vector<int> info(2);
				info[0] = head->val;
				info[1] = index;
				s.push(info);
			}
			index++;
			head = head->next;
		}
		return ret;
	}
};