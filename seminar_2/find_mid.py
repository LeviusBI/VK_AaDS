def mid_list(my_list):
    slow = my_list.head
    fast = my_list.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow