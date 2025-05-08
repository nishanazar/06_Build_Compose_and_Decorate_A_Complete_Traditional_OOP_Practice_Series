class Employee:
    def __init__(self, name:str, salary:int, ssn: int):
        self.name = name
        self._salary = salary
        self.__ssn = ssn



emp = Employee("Ali", 50000, 555)

print("Public Variable (name):", emp.name)
print("Protected Variable (_salary):", emp._salary)

print(emp.__ssn)
# Try accessing the private variable directly
# print("Private Variable (__ssn):", emp.__ssn)  # This will cause an error