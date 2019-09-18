#include "lists.h"
#include <stdlib.h>
/**
 * len_list - returns the list's length
 * @head: pointer to the list's head
 * Return: list's length
 */
int len_list(listint_t **head)
{
	int len = 0;
	listint_t *cpy = *head;

	for (; cpy; len++, cpy = cpy->next)
		;
	return (len);
}
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to the list's head
 * Return: 1 if the list is palindorme or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, aux = 0;
	int *num = NULL;
	listint_t *cpy = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	cpy = *head;
	len = len_list(head) - 1;
	aux = len;
	if (len == 0)
		return (1);
	num = (int *)malloc(sizeof(int) * len);
	for (; i <= len; i++, cpy = cpy->next)
		num[i] = cpy->n;
	for (i = 0; i <= len / 2; i++, aux--)
	{
		if (num[i] != num[aux])
		{
			free(num);
			return (0);
		}
	}
	free(num);
	return (1);
}
