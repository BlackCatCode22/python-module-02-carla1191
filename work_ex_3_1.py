hours = float(input("Enter Hours: "))

rate = float(input("Enter Rate: "))

pay = 0.0

if hours > 40:
    # Regular Pay
    regular_pay = rate * 40
    # Overtime
    overtime_hours = hours - 40
    # Overtime pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Total pay
    pay = regular_pay + overtime_pay
else:
    # Regular pay
    pay = rate * hours

print("Pay:", pay)