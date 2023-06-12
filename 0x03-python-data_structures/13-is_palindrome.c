#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 *@head: pointer to pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL;
	int len = 0, mid;
	int *Arr = NULL;

	if (*head == NULL)
		return (1);


	tmp = *head;

	if (tmp->next == NULL)
		return (1);

	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}

	Arr =  (int *)malloc(sizeof(int) * len);
	tmp = *head;
	len = 0;

	while (tmp != NULL)
	{
		Arr[len++] = tmp->n;
		tmp = tmp->next;
	}

	for (mid = 0; mid < len / 2; mid++)
	{
		if (Arr[mid] != Arr[len - mid - 1])
		{
			free(Arr);
			return (0);
		}
	}
	free(Arr);
	return (1);
}
