import pandas as pd
import matplotlib.pyplot as plt

# Create sample data (25 employees)
data = {
    "Employee_ID": list(range(1, 26)),
    "Age": [22, 25, 28, 24, 30, 27, 26, 29, 23, 31,
            35, 32, 28, 26, 24, 27, 29, 33, 34, 36,
            28, 25, 26, 30, 31],
    "Salary": [15000, 18000, 20000, 17000, 22000, 21000, 19000, 23000, 16000, 24000,
               26000, 25000, 20000, 19500, 17500, 20500, 22500, 25500, 26500, 27000,
               21000, 18500, 19500, 22000, 23500],
    "Role": ["Waiter", "Chef", "Manager", "Waiter", "Chef", "Waiter", "Cleaner", "Chef", "Waiter", "Manager",
             "Chef", "Manager", "Waiter", "Cleaner", "Waiter", "Chef", "Waiter", "Manager", "Chef", "Manager",
             "Chef", "Waiter", "Cleaner", "Chef", "Manager"]
}

df = pd.DataFrame(data)

# Plot chart
plt.plot(df["Employee_ID"], df["Salary"], marker='o')
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.title("Restaurant Employees Salary Chart")
plt.grid()

plt.show()