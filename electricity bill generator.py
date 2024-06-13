import random
# Get customer information
customer_name = input("Customer Name: ")
account_number = random.randint(100000, 10000000)  # Generate random account number

# Get billing period 
# Get electricity usage
kWh_used = float(input("Enter the total kilowatt-hours used: "))
rate_kwh = float(input("Enter the electricity rate (in rupees per kWh): "))

# Calculate base charge
base_charge = kWh_used * rate_kwh

# Calculate taxes
tax_rate = 0.18  # 18% tax 
taxes = base_charge * tax_rate

# Calculate total bill amount
total_bill_amount = base_charge + taxes

# Print the bill
print("Electricity Bill")
print(f"Customer Name: {customer_name}")
print(f"Account Number: {account_number}")

# print(f"Billing Period: {start_date} to {end_date}")
print(f"Base Electricity Charge: ₹{base_charge:.2f}")
print(f"Taxes: ₹{taxes:.2f}")
print(f"Total Bill Amount: ₹{total_bill_amount:.2f}")