#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * struct ListNode - a node of a singly linked list
 * @val: integer value in the node
 * @next: pointer to the next node
 */
typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;

/**
 * is_palindrome - a function that checks if a singly
 * linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */
int is_palindrome(ListNode **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	ListNode *slow = *head;
	ListNode *fast = *head;
	ListNode *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		ListNode *next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (prev->val != slow->val)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return 1;
}

/**
 * createNode - a fubction that creates a new node of a singly linked list
 * @val: integer value to put in the new node
 * Return: pointer to the new node
 */
ListNode *createNode(int val)
{
	ListNode *newNode = (ListNode *)malloc(sizeof(ListNode));
	newNode->val = val;
	newNode->next = NULL;
	return (newNode);
}

/**
 * main - entry point
 * Return: 0 on success
 */
int main()
{
	ListNode *head = createNode(1);
	head->next = createNode(2);
	head->next->next = createNode(3);
	head->next->next->next = createNode(2);
	head->next->next->next->next = createNode(1);

	int result = is_palindrome(&head);
	if (result)
	{
		printf("The linked list is a palindrome.\n");
	}
	else
	{
		printf("The linked list is not a palindrome.\n");
	}

	ListNode *current = head;
	while (current != NULL)
	{
		ListNode *temp = current;
		current = current->next;
		free(temp);
	}

	return (0);
}
