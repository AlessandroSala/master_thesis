import matplotlib.pyplot as plt
import numpy as np

def plot_separation_energies():
    """
    Calculates and plots the one-neutron (Sn) and two-neutron (S2n)
    separation energies for Sn (Z=50) isotopes as a function of
    mass number (A).
    
    The S_n plot clearly shows the even-odd staggering.
    The S_2n plot shows the smooth trend and shell effects.
    
    Data is from the AME2020 atomic mass evaluation.
    Reference:
    M. Wang, et al., "The AME 2020 atomic mass evaluation (I). Evaluation of 
    input data and adjustment," Chinese Physics C 45, 030002 (2021).
    """
    
    # Total binding energies (B) in MeV for Sn (Z=50) isotopes.
    # Data extracted from AME2020 (Wang et al., 2021).
    # Key = Mass Number (A), Value = Total Binding Energy (B) in MeV
    binding_energies_mev = {
        # A: B(MeV)
        107: 903.026,
        108: 914.655,
        109: 923.286,
        110: 934.570,
        111: 942.738,
        112: 953.525,
        113: 961.270,
        114: 971.573,
        115: 979.118,
        116: 988.682,
        117: 995.625,
        118: 1004.951,
        119: 1011.434,
        120: 1020.539,
        121: 1026.709,
        122: 1035.523,
        123: 1041.469,
        124: 1049.958,
        125: 1055.691,
        126: 1063.884,
        127: 1069.410,
        128: 1077.373,
        129: 1082.673,
        130: 1090.286,
        131: 1095.490,
        132: 1102.843,
        133: 1105.242,
        134: 1108.873,
        135: 1111.143,
        136: 1114.792,
        137: 1116.824,
    }

    # Get a sorted list of available mass numbers
    all_a = sorted(binding_energies_mev.keys())
    
    # Lists to store S_n (one-neutron separation energy)
    # S_n(A) = B(A) - B(A-1)
    a_plot_sn = []
    sn_plot = []
    
    # Lists to store S_2n (two-neutron separation energy)
    # S_2n(A) = B(A) - B(A-2)
    a_plot_s2n = []
    s2n_plot = []
    
    # Calculate S_n
    for a in all_a[0:]: # Start from the second nucleus
        if (a + 1) in binding_energies_mev:
            sn = binding_energies_mev[a+1] - binding_energies_mev[a ]
            a_plot_sn.append(a-1)
            sn_plot.append(sn)
            
    # Calculate S_2n
    for a in all_a[2:]: # Start from the third nucleus
        if (a - 2) in binding_energies_mev:
            s2n = binding_energies_mev[a] - binding_energies_mev[a - 2]
            a_plot_s2n.append(a)
            s2n_plot.append(s2n)

    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot S_n
    plt.plot(a_plot_sn, sn_plot, 'bo-', 
             markersize=6, label='$S_n$')
             
    # Style the plot
    plt.xlabel('Mass Number (A)', fontsize=14)
    plt.ylabel("$S_n$ [MeV]", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.minorticks_on()
    
    # Highlight the N=82 shell closure (A=132)
    plt.axvline(x=132, color='k', linestyle='--', linewidth=1, label='N=82 Shell Closure')
    plt.legend(fontsize=12) # Call legend again to include axvline
    
    # Add a text box for the data source
    plt.text(0.02, 0.02, 'Data from AME2020 (Wang et al., 2021)',
             transform=plt.gca().transAxes, fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.5))
    plt.ylim(0, 14)
             
    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Check if matplotlib is installed
    try:
        import matplotlib
    except ImportError:
        print("Matplotlib not found.")
        print("Please install it using: pip install matplotlib")
    else:
        plot_separation_energies()
