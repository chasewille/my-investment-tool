# Investment Calculator
def calculate_future_value(present_value, annual_rate, periods):
    future_value = present_value * (1 + annual_rate) ** periods
    return future_value

# Example Inputs
present_value = float(input("Enter the present value ($): "))
annual_rate = float(input("Enter the annual interest rate (as a decimal): "))
periods = int(input("Enter the number of periods (years): "))

# Calculate Future Values
future_value = calculate_future_value(present_value, annual_rate, periods)

print(f"The future value of your investment is: ${future_value:.2f}")

