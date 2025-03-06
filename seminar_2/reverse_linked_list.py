def reverse_linked_list(my_list):
    prev = None
    current = my_list.head

    while current is not None:
        next_noda = current.next
        current.next = prev
        prev = current
        current = next_noda
    my_list.head = prev
    return my_list