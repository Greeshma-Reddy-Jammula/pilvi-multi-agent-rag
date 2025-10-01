class SagaStep:
    def __init__(self, action, rollback):
        self.action = action
        self.rollback = rollback

class Saga:
    def __init__(self):
        self.steps = []
        self.completed = []

    def add_step(self, action, rollback):
        self.steps.append(SagaStep(action, rollback))

    def execute(self):
        try:
            for step in self.steps:
                step.action()
                self.completed.append(step)
            print("Saga completed successfully!")
        except Exception as e:
            print(f"Error: {e}. Rolling back...")
            for step in reversed(self.completed):
                step.rollback()
            print("Rollback complete")

# Example
if __name__ == "__main__":
    saga = Saga()
    saga.add_step(lambda: print("Book flight"), lambda: print("Cancel flight"))
    saga.add_step(lambda: print("Book hotel"), lambda: print("Cancel hotel"))
    saga.add_step(lambda: (_ for _ in ()).throw(Exception("Payment failed")),
                  lambda: print("Refund payment"))
    saga.execute()
