#include "lists.h"

/**
 * dlistint_len - prints the number of elements in a list
 * @h: the first node
 *
 * Return: the number of elements
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}
	return (count);
}
