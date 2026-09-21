# Create a Node class to represent each customer in the waitlist
class Node:
    """
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    """
    def __init__(self, name):
        self.name = name
        self.next = None

# Create a LinkedList class to manage the waitlist
class LinkedList:
    """
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    """
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            current.next = current
            self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        if not current:
            print("The list is currently empty.")
        else:
            while current:
                print(current.name)
                current = current.next

def waitlist_generator():
    waitlist = LinkedList()

    print("\n--- Waitlist Manager ---")
    print("1. Add customer to front")
    print("2. Add customer to end")
    print("3. Remove customer by name")
    print("4. Print waitlist")
    print("5. Exit")

    while True:
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?

This waitlist runs on a singly linked list. Instead of grouping everyone in one continuous memory block
like a standard array, each customer gets their own "node." Each node just points to the next person in 
line. This setup lets the program add or drop people quickly by just changing where the links point, rather 
than shifting a whole array of data around.

- What role does the head play?

The head acts as the front door to the list. Since linked lists don't use numbered indexes, you can't 
just jump straight to the 5th person. Anytime you want to search, add, or remove a customer, you have 
to start at the head and walk through the connections. If you lose track of the head, the rest of the 
list is lost in memory.

- When might a real engineer need a custom list like this?

In the real world, software engineers build custom lists like this when they need to constantly add 
and remove data without slowing down the system. You'll see them used under the hood for things like 
server request queues, operating system task managers, or the undo/redo features in standard apps.

'''