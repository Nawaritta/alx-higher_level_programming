#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 *@head: pointer to pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL;
	size_t len = 0, mid;
	int *Arr = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	tmp = *head;
	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	mid = len / 2;
	Arr =  (int *)malloc(sizeof(int) * mid);

	tmp = *head;
	while (mid > 0)
	{
		Arr[mid - 1] = tmp->n;
		tmp = tmp->next;
		mid--;
	}

	if (len % 2 != 0)
		tmp = tmp->next;

	while (mid < len / 2)
	{
		if (tmp->n != Arr[mid])
		{
			free(Arr);
			return (0);
		}
		mid++;
		tmp = tmp->next;
	}
	free(Arr);
	return (1);
}
