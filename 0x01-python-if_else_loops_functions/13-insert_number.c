#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: start node
 * @number: to be inserted
 * Return: address of the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (tmp == NULL || tmp->n >= number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n > number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
