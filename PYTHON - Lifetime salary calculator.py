class CareerStage:
    def __init__(self, yearly_income, years):
        self.yearly_income = yearly_income
        self.years = years

    def calculate_stage_income(self):
        return self.yearly_income * self.years


class Career:
    def __init__(self):
        self.stages = []

    def add_stage(self, yearly_income, years):
        new_stage = CareerStage(yearly_income, years)
        self.stages.append(new_stage)

    def calculate_lifetime_salary(self):
        total_income = 0
        for stage in self.stages:
            total_income += stage.calculate_stage_income()
        return total_income


def main():
    career = Career()

    print("Lifetime Salary Calculator")

    while True:
        try:
            yearly_income = float(input("Enter yearly income for this stage (HUF): "))
            years = int(input("Enter number of years at this income: "))
            career.add_stage(yearly_income, years)

            add_another = input("Do you want to add another stage? (yes/no): ").lower()
            if add_another != 'yes':
                break
        except ValueError:
            print("Invalid input, please try again.")

    total_income = career.calculate_lifetime_salary()
    print(f"Your total lifetime salary is: {total_income:.2f} HUF")


if __name__ == "__main__":
    main()
