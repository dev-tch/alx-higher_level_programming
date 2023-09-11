#include "lists.h"
/**
* is_palindrome - check if list is palindrome
* @head: list
* Return: (1 or 0)
*/
int is_palindrome(listint_t **head)
{
	listint_t *jmpone = *head;
	listint_t *jmptwo = *head;
	listint_t *old = NULL;
	listint_t *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (jmptwo != NULL && jmptwo->next != NULL)
	{
		jmptwo = jmptwo->next->next;
		tmp = jmpone->next;
		jmpone->next = old;
		old = jmpone;
		jmpone = tmp;
	}

	if (jmptwo != NULL)
	{
		jmpone = jmpone->next;
	}

	while (old != NULL && jmpone != NULL)
	{

		if (old->n != jmpone->n)
		{
			return (0);
		}
	old = old->next;
	jmpone = jmpone->next;
	}
	return (1);
}
