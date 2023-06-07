#include "lists.h"
/**
 * insert_node - Function inserts a node in a sorted linked list
 * @head: the head of the linked lists
 * @number: data in the newnode
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	current = *head;
	while (current->next != NULL && number >= current->next->n)
		current = current->next;
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
