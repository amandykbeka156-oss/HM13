class TicketMachine:
    def __init__(self):
        self.state = Idle(self)

    def set_state(self, state):
        self.state = state

    def select_ticket(self):
        self.state.select_ticket()

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def dispense_ticket(self):
        self.state.dispense_ticket()

    def cancel(self):
        self.state.cancel()


class State:
    def __init__(self, machine):
        self.machine = machine

    def select_ticket(self):
        print("Action not allowed in current state.")

    def insert_money(self, amount):
        print("Action not allowed in current state.")

    def dispense_ticket(self):
        print("Action not allowed in current state.")

    def cancel(self):
        print("Action not allowed in current state.")

class Idle(State):
    def select_ticket(self):
        print("Ticket selected. Waiting for money...")
        self.machine.set_state(WaitingForMoney(self.machine))


class WaitingForMoney(State):
    def insert_money(self, amount):
        print(f"Money received: {amount}")
        self.machine.set_state(MoneyReceived(self.machine))

    def cancel(self):
        print("Transaction canceled.")
        self.machine.set_state(TransactionCanceled(self.machine))


class MoneyReceived(State):
    def dispense_ticket(self):
        print("Ticket dispensed. Enjoy your event!")
        self.machine.set_state(TicketDispensed(self.machine))

    def cancel(self):
        print("Transaction canceled. Money refunded.")
        self.machine.set_state(TransactionCanceled(self.machine))


class TicketDispensed(State):
    def __init__(self, machine):
        super().__init__(machine)
        self.reset()

    def reset(self):
        print("Returning to Idle state.")
        self.machine.set_state(Idle(self.machine))


class TransactionCanceled(State):
    def __init__(self, machine):
        super().__init__(machine)
        self.reset()

    def reset(self):
        print("Returning to Idle state.")
        self.machine.set_state(Idle(self.machine))


if __name__ == "__main__":
    machine = TicketMachine()
    machine.select_ticket()
    machine.insert_money(50)
    machine.dispense_ticket()
    machine.select_ticket()
    machine.cancel()
