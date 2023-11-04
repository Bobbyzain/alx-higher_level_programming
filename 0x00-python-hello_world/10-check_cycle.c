#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - to check if a linked list is circular
 * @list: the linked list parameter
 * Return: Always int
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *head2;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;
	head2 = list->next;
	while (head && head2 && head2->next)
	{
		if (head == head2)
		{
			return (1);
		}
		head = head->next;
		head2 = head2->next->next;
	}
	return (0);
}
