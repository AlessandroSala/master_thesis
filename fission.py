import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Constants and SEMF Parameters ---

# Typical Semi-Empirical Mass Formula (SEMF) Coefficients (in MeV)
A_S = 18.0      # Surface energy coefficient (a_s)
A_C = 0.72      # Coulomb energy coefficient (a_c)

# Fixed Mass Number for this plot (Heavy nucleus to show the effect clearly)
FIXED_A = 200

# --- 2. Define the Function and Plot Parameters ---

def calculate_delta_e(alpha_20_squared, A, R, a_s, a_c):
    """
    Calculates the deformation energy Delta E for a given quadrupole
    deformation (alpha_20^2) and fixed Mass Number (A) and ratio (R = Z^2/A).

    Formula: Delta E = alpha_20^2 * [ A^(2/3) * ( (2/5 * a_s) - (1/5 * a_c * R) ) ]
    """
    # Calculate the coefficient K (the slope)
    # K = A^(2/3) * ( (2/5 * a_s) - (1/5 * a_c * R) )
    K = A**(2/3) * ( (0.4 * a_s) - (0.2 * a_c * R) )
    
    # Delta E = K * alpha_20^2
    return K * alpha_20_squared

# Deformation parameter range for the plot (from spherical to large deformation)
ALPHA_20_SQUARED_values = np.linspace(0, 0.5, 200)

# Stability Ratios (R = Z^2/A) to plot
# Note: Labels now only contain the ratio number as requested.
R_ratios = [
    {'R': 15, 'label': r'15'},
    {'R': 25, 'label': r'25'},
    {'R': 35, 'label': r'35'},
    {'R': 45, 'label': r'45'},
]

# --- 3. Generate and Plot the Data ---

plt.figure(figsize=(10, 6))

for ratio_data in R_ratios:
    R = ratio_data['R']
    label = ratio_data['label']
    
    # Calculate the energy correction for the entire alpha_20^2 range
    delta_e_values = calculate_delta_e(ALPHA_20_SQUARED_values, FIXED_A, R, A_S, A_C)
    
    # Plot the results
    # Formatting the label to show Z^2/A = [ratio]
    plt.plot(ALPHA_20_SQUARED_values, delta_e_values, label=r'$Z^2/A = ' + label + r'$', linewidth=2)

# --- 4. Customizing the Plot Aesthetics ---

plt.title(
    r'Deformation Energy ($\Delta E$) vs. Quadrupole Deformation ($\alpha_{20}^2$)' + f' for Fixed $A = {FIXED_A}$',
    fontsize=16,
    fontweight='bold'
)
plt.xlabel(r'Quadrupole Deformation Parameter Squared ($\alpha_{20}^2$)', fontsize=14)
plt.ylabel(r'Deformation Energy ($\Delta E$) [MeV]', fontsize=14)

# Highlight the zero-energy line
plt.axhline(0, color='gray', linestyle='--', linewidth=1)

plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(title=r'Stability Ratio ($Z^2/A$)', fontsize=12)
plt.ylim(-10, 10) 
plt.xlim(0, 0.5) 
plt.tick_params(labelsize=12)
plt.tight_layout()
plt.show()

# --- Interpretation of the Plot ---
# * Positive slope (K > 0) means energy increases with deformation (stable sphere).
# * Negative slope (K < 0) means energy decreases with deformation (unstable sphere, favors deformation).
# * For the fixed mass number A=200, the critical ratio R_crit where the slope is zero lies between 35 and 45.
