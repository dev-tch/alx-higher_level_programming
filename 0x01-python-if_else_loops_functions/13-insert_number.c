#include "lists.h"
/**
* insert_node - function to insert node in linked list
* @head: list
* @number: content of node
* Return: the new added node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *tmp = *head, *new_node = NULL, *old_node = NULL;
new_node =  malloc(sizeof(listint_t));
/*malloc failed*/
if (new_node == NULL)
{
	return (NULL);
}
else
{
	new_node->n = number;
	new_node->next = NULL;
}
if (*head == NULL)
{
	*head = new_node;
	return (new_node);
/*insert the node at  first position*/
}
while (tmp != NULL)
{
	if (number <= tmp->n)
	{
		/*insertion */
		old_node->next = new_node;
		new_node->next = tmp;
		return (new_node);
	}
	old_node = tmp;
	tmp = tmp->next;
}

old_node->next = new_node;
return (new_node);
}

