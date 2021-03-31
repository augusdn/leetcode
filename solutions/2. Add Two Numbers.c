/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
​
​
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *node1 = l1, *node2 = l2, *cur;
    struct ListNode *head = NULL;
    
    int val, flag = 0;
    while(node1 != NULL || node2 != NULL || flag != 0){
        val = 0;
        if(node1 != NULL){
            val += node1->val;
            node1 = node1->next;
        }
        if(node2 != NULL){
            val += node2->val;
            node2 = node2->next;
        }
        val += flag;
        
        flag = val/10;
        val %= 10;
        
        struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        newNode->val = val;
        newNode->next = NULL;
        
        if(head == NULL)
            head = newNode;
        else
            cur->next = newNode;
        
        cur = newNode;
    }
    return head;
}
