# Data Analysis

This folder contains Python-based analysis of the experimental results from the 17-4 PH stainless steel heat-treatment study.

## Current Analysis

### Property Comparison

`property_comparison.py` reads the experimental dataset and identifies the heat-treatment condition associated with the highest measured value for each mechanical property, as well as the lowest measured corrosion rate.

### Input Data

The analysis uses:

`../data/experimental_results.csv`

### Properties Analyzed

- Yield strength
- Ultimate tensile strength
- Elongation
- Rockwell hardness
- Microhardness
- Impact energy
- Corrosion rate

## Planned Analysis

Future additions may include:

- Automated property-comparison plots
- Strength–ductility trade-off analysis
- Correlation analysis
- Processing–property visualization
- Statistical analysis of replicate measurements
