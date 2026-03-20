import matplotlib.pyplot as plt

# College data (example)
years = [2019, 2020, 2021, 2022, 2023]
marks = [65, 72, 78, 81, 88]

# Plot chart
plt.plot(years, marks, marker='o')

# Labels aur title
plt.xlabel("Year")
plt.ylabel("Marks (%)")
plt.title("College Marks Over Years")

# Grid show karne ke liye
plt.grid()

# Chart display
plt.show()