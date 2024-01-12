#include "lists.h"
/**
 * print_dlistint - prints the number in a linked list
 * @h: the first node
 *
 * Return: the number of nodes in a linked-list
*/
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
