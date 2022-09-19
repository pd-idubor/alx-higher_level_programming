#include "lists.h"

/**
 * check_cycle - Cchecks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tmp = list;

	while (tmp != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;
		if (head == tmp)
			return (1);
	}
	return (0);
}
