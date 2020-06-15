class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}. {self.age}"

    def __repr__(self) -> str:
        return f"Object of the class {self.__class__.__name__}. name: {self.name}, last_name: {self.last_name}, age: {self.age}"
