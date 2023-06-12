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

	if (tmp->next == NULL)
		return (1);

	Arr =  (int *)malloc(sizeof(int));

	while (tmp != NULL)
	{
		Arr[len++] = tmp->n;
		tmp = tmp->next;
		Arr = (int *) realloc(Arr, sizeof(int) * (len + 1));
	}

	mid = len;
	while (mid > len / 2)
	{
		if (Arr[len - mid] != Arr[mid - 1])
		{
			free(Arr);
			return (0);
		}
		mid--;
	}
	free(Arr);
	return (1);
}
