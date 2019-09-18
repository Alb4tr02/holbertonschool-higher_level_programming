#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to the list's head
 * Return: 1 if the list is palindorme or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, aux = 0;
	int num[200];
	listint_t *cpy = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	cpy = *head;
	for (; cpy && len < 200; len++, cpy = cpy->next)
		num[len] = cpy->n;
	len--;
	aux = len;
	for (i = 0; i <= len / 2; i++, aux--)
		if (num[i] != num[aux])
			return (0);
	return (1);
}
