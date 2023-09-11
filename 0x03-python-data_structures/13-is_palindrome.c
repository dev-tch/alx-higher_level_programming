#include "lists.h"

/*find the middle of list*/
/**
* get_node_at_middle - search middle node
* @h: list
* Return: pointer to middle node
*/
listint_t *get_node_at_middle(listint_t *h)
{
	/*declare two pointers at head*/
	listint_t *jmpone = h,  *jmptwo = h;

	while (jmpone != NULL && jmptwo != NULL)
	{
		jmpone = jmpone->next;
		jmptwo = jmptwo->next;
	}
	return (jmpone);
}

/**/
/**
* reversed_list - reverse the second half of list
* @h: second half list
* Return: pointer to the list
*/
listint_t *reversed_list(listint_t *h)
{
	listint_t *before = NULL;
	listint_t *now = h;
	listint_t *after = NULL;

	while (now != NULL)
	{
		after = now->next;
		now->next = before;
		before = now;
		now = after;
	}
	return (before);
}

/**
* is_palindrome -  list can be same if we  read from first or last
* @head: list
* Return: (0 or 1)
*/
int is_palindrome(listint_t **head)
{
	listint_t *mid = NULL;
	listint_t *halftwo =  NULL;
	listint_t *halfone = *head;
	int is_pal = 1;

	if (*head == NULL || (*head)->next == NULL)
	return (1);

	mid = get_node_at_middle(*head);
	if (mid == NULL)
		return (1);
	halftwo =  reversed_list(mid->next);
	while (halftwo != NULL)
	{
		if (halfone->n != halftwo->n)
		{
			is_pal = 0;
			break;
		}
		halfone = halfone->next;
		halftwo = halftwo->next;
	}

	mid->next = reversed_list(halfone);
	return (is_pal);
}
