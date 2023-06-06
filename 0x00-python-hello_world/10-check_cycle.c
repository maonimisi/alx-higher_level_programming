#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL || list->next == NULL)
		return (0);
	head = list;
	tail = head->next;
	while (head != NULL && tail->next != NULL
		&& tail->next->next != NULL)
	{
		if (head == tail)
			return (1);
		head = head->next;
		tail = tail->next->next;
	}
	return (0);
}
