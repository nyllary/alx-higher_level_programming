#include "lists.h"
/**
 * add_dnodeint - adds a new node at the brginning
 * @head: prev pointer of the current node
 * @n: vvalue of the initial 1st node
 * Return: the value of the node and
 * the content of the head pointer
*/

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = *head;

	if (*head != NULL)
		(*head)->prev = new_node;

	*head = new_node;
	return (new_node);
}
