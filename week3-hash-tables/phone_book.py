class PhoneBook:
    """A simple phonebook manager with direct addressing scheme.
    Sample Input:
    12
    add 911 police
    add 76213 Mom
    add 17239 Bob
    find 76213
    find 910
    find 911
    del 910
    del 911
    find 911
    find 76213
    add 76213 daddy
    find 76213
   Sample output:
    Mom
    not found
    police
    not found
    Mom
    daddy
    Explanation:
    76213 is Mom’s number, 910 is not a number in the phone book,
    911 is the number of police, but then it was deleted from
    the phone book, so the second search for 911 returned “not found”.
    Also, note that when the daddy was added with the same phone number
    76213 as Mom’s phone number, the contact’s name was rewritten,
    and now search for 76213 returns “daddy” instead of “Mom”.
    """
    def __init__(self):
        self.book = [None] * 10000000

    def add(self, number, name):
        """Adds a person with name and phone number to the phone book.
        If there exists a user with such number already, then manager overwrites
        the corresponding name.
        """
        self.book[number] = name

    def delete(self, number):
        """deletes the info it is present in the
        phonebook updated so far"""
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        """Replies with the person's name, or with string “not found”
        (without quotes) if there is no such person in the book.
        """
        if self.book[number] is None:#if no such person is found in the book
            return "not found"
        return self.book[number]#return the corresponding result

def process_queries(queries):
    """utility function to read the query and then call
    the corresponding method to be processed"""
    for query in queries:
        q = query.split()
        command = q[0]
        number = int(q[1])
        if command == "add":#invoke the add method
            phonebook.add(number, q[2])
        elif command == "find":#invoke the find method
            print(phonebook.find(number))
        elif command == "del":#invoke the delete method
            phonebook.delete(number)

if __name__ == "__main__":
    phonebook = PhoneBook()
    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)
