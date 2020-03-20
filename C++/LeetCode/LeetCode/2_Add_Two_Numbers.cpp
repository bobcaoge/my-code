#include <iostream>
using namespace std;
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		int carry = 0;
		ListNode* ret = new ListNode(0);
		ListNode* cur = ret;
		int val_of_l1;
		int val_of_l2;
		int sum;
		int val;
		while (l1 != NULL || l2 != NULL) {
			val_of_l1 = l1 != NULL ? l1->val : 0;
			val_of_l2 = l2 != NULL ? l2->val : 0;
			sum = val_of_l1 + val_of_l2 + carry;
			carry = sum / 10;
			val = sum % 10;
			cur->next = new ListNode(val);
			cur = cur->next;
			if (l1 != NULL) {
				l1 = l1->next;
			}
			if (l2 != NULL) {
				l2 = l2->next;
			}
		}
		if (carry != 0) {
			cur->next = new ListNode(carry);
		}
		return ret->next;
	}
};