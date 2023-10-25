class Salutation:
    """Say hello to someone!"""

    salutation: str
    subject: str

    def __init__(self, salutation: str, subject: str) -> None:
        self.salutation = salutation
        self.subject = subject

    def say_hello(self) -> None:
        return f"{self.salutation}, {self.subject}"