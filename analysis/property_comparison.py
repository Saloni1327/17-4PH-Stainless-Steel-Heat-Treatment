import pandas as pd

# Load experimental results
data = pd.read_csv("../data/experimental_results.csv")

# Properties where higher values indicate higher measured performance
higher_is_better = {
    "Yield Strength (MPa)": "Yield Strength",
    "UTS (MPa)": "Ultimate Tensile Strength",
    "Elongation (%)": "Elongation",
    "Rockwell Hardness (HRC)": "Rockwell Hardness",
    "Microhardness (HV)": "Microhardness",
    "Impact Energy (J)": "Impact Energy",
}

print("17-4 PH Stainless Steel — Property Comparison")
print("=" * 55)

for column, label in higher_is_better.items():
    best = data.loc[data[column].idxmax()]
    print(f"{label}: {best['Condition']} ({best[column]})")

# Corrosion rate is a lower-is-better property
best_corrosion = data.loc[data["Corrosion Rate (mm/year)"].idxmin()]

print(
    f"Lowest Corrosion Rate: "
    f"{best_corrosion['Condition']} "
    f"({best_corrosion['Corrosion Rate (mm/year)']} mm/year)"
)
