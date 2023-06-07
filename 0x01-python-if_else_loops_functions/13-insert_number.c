#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: double pointer to the head
 * @number: the number to insert
 *
 * Return: pointer to the newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *tmp = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (head == NULL || *head == NULL)
		return (new_node);

	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	if (number == (*head)->n)
	{
		free(new_node);
		return (*head);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n < number)
			tmp = tmp->next;
		else
			break;
	}
	if (tmp->next != NULL)
		new_node->next = tmp->next;

	tmp->next = new_node;

	return (new_node);
}
