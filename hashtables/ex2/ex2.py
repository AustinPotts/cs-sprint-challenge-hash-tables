#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length): # Def takes in tickets & length 
    """
    YOUR CODE HERE
    """
    route = [None] * length 

    store = dict() # Create dictionary 
    for ticket in tickets: # iterate over tickets, if ticket then store 
        store[ticket.source] = ticket.destination
    next = store["NONE"]

    for current in range(0, length): # for current in range
        route[current] = next
        next = store[next]

    return route
