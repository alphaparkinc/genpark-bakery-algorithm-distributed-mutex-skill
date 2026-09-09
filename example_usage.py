from client import BakeryMutexArbitrator

def main():
    print("=== Lamport's Bakery Mutex Arbitrator ===")
    arbitrator = BakeryMutexArbitrator(num_nodes=3)

    # Node 1 gets ticket first
    t1 = arbitrator.request_ticket(1)
    # Node 0 gets ticket second
    t0 = arbitrator.request_ticket(0)

    print("Ticket 1:", t1, "| Ticket 0:", t0)
    assert arbitrator.can_enter(1) is True # Node 1 has lower ticket (served first)
    assert arbitrator.can_enter(0) is False

    arbitrator.release_ticket(1)
    assert arbitrator.can_enter(0) is True

    print("Bakery Mutex Arbitrator verified successfully!")

if __name__ == "__main__":
    main()
