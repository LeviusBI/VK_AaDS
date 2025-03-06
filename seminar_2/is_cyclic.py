def hasCycle(lst):
    if lst.head is None or lst.head.next is None:
        return False
    slow = lst.head
    fast = lst.head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True