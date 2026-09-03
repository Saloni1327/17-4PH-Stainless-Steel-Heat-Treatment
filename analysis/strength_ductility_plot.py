import pandas as pd
import matplotlib.pyplot as plt

# Load experimental results
data = pd.read_csv("../data/experimental_results.csv")

# Create strength–ductility plot
plt.figure(figsize=(8, 6))

plt.scatter(
    data["UTS (MPa)"],
    data["Elongation (%)"]
)

for _, row in data.iterrows():
    plt.annotate(
        row["Condition"],
        (row["UTS (MPa)"], row["Elongation (%)"]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Ultimate Tensile Strength (MPa)")
plt.ylabel("Elongation (%)")
plt.title("17-4 PH Stainless Steel: Strength–Ductility Relationship")

plt.tight_layout()
plt.savefig("../figures/strength_ductility_relationship.png", dpi=300)
plt.show()
