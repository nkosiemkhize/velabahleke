import matplotlib.pyplot as plt

years = list(range(1996, 2020))
results = [
    99, 96, 97, 100, 95, 96, 95, 90, 93, 94,
    97, 93, 98, 93, 93, 99, 97.3, 96.6, 96.7,
    96.5, 98.6, 98.92, 100, 98.6
]

plt.figure(figsize=(12, 6))
plt.plot(years, results, marker='o', color='#0027C2', label='Pass Rate')
plt.title("Velabahleke Matric Results (1996–2019)")
plt.xlabel("Year")
plt.ylabel("Pass Percentage (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()