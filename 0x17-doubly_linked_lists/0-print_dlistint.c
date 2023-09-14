#include "lists.h"
/**
* print_dlistint - print nodes of doubly linked list
* @h: list
* Return:(nb of nodes)
*/
size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *temp = h;
size_t nb_elem = 0;
while (temp != NULL)
{
printf("%d\n", temp->n);
temp = temp->next;
nb_elem++;
}
return (nb_elem);
}

