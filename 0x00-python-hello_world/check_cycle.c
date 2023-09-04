#include "lists.h"
/**
* check_cycle - check if list in cycle
* @list: list contains nodes of integers
* Return: 0- there is no cycle 1- there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr_one_move = list, *ptr_two_move = list;

	if (list == NULL)
		return (0);
	do {
		if (ptr_two_move == NULL || ptr_two_move->next == NULL)
			return (0);
		ptr_one_move = ptr_one_move->next;
		ptr_two_move = ptr_two_move->next->next;
	} while (ptr_one_move != ptr_two_move);

return (0);
}

