class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_bill_amount(self) -> float:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float) -> None:
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            raise ValueError("Bill amount cannot be negative.")

    def calculate_bill(self) -> float:
        return self.get_bill_amount()

class SeniorPatient(Patient):
    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        return original_bill * 0.80

class PhilHealthPatient(Patient):
    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        return original_bill * 0.85

if __name__ == "__main__":
    print("Hospital Billing System")
    print("=======================")
    patient1 = Patient(input("Patient Name: "), float(input("Cost: ")))
    print(f"Patient: {patient1.get_name()} | Final Bill: ₱{patient1.calculate_bill():,.2f}")

    patient2 = SeniorPatient(input("Senior Patient Name: "), float(input("Cost: ")))
    print(f"Senior Patient: {patient2.get_name()} | Final Bill: ₱{patient2.calculate_bill():,.2f}")

    patient3 = PhilHealthPatient(input("PhilHealth Patient Name: "), float(input("Cost: ")))
    print(f"PhilHealth Patient: {patient3.get_name()} | Final Bill: ₱{patient3.calculate_bill():,.2f}")