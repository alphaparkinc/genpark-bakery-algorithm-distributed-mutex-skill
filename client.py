class BakeryMutexArbitrator:
    """Lamport's Bakery algorithm state arbitrator."""
    def __init__(self, num_nodes: int = 4):
        self.num_nodes = num_nodes
        self.tickets = [0] * num_nodes

    def request_ticket(self, node_id: int) -> int:
        self.tickets[node_id] = max(self.tickets) + 1
        return self.tickets[node_id]

    def release_ticket(self, node_id: int):
        self.tickets[node_id] = 0

    def can_enter(self, node_id: int) -> bool:
        my_ticket = self.tickets[node_id]
        if my_ticket == 0:
            return False
        for other_id in range(self.num_nodes):
            other_ticket = self.tickets[other_id]
            if other_ticket != 0:
                if (other_ticket, other_id) < (my_ticket, node_id):
                    return False
        return True
