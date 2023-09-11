#include "lists.h"

/**
* reverse_list - recursive function to reverse list and save it in new one
* @h: list of integers
* @new: reversed list
* Return: void
*/

void reverse_list(listint_t *h, listint_t **new)
{
	if (h == NULL)
	{
		return;
	}
	reverse_list(h->next, new);
	add_nodeint_end(new, h->n);
}
/**
* is_palindrome - check if list is palindrome
* @head: list
* Return: (1: palindrome) (0: not palindrome)
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp  = *head;
	listint_t *tmp2 = *head;
	listint_t *new  = NULL;
	int  is_pal = 1;
	/**/
	if (tmp == NULL)
	{
		return (1);
	}
	reverse_list(tmp, &new);

	while (tmp2 != NULL && new != NULL)
	{
		if (tmp2->n != new->n)
		{
			is_pal = 0;
			break;
		}
		new  = new->next;
		tmp2 = tmp2->next;
	}
	return (is_pal);
}
