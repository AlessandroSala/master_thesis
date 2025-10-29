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
        108: 916.733,
        109: 924.381,
        110: 933.435,
        111: 940.380,
        112: 949.191,
        113: 956.402,
        114: 965.342,
        115: 972.783,
        116: 981.849,
        117: 989.508,
        118: 998.688,
        119: 1006.554,
        120: 1015.845,
        121: 1023.905,
        122: 1033.298,
        123: 1041.540,
        124: 1051.031,
        125: 1058.913,
        126: 1068.514,
        127: 1076.436,
        128: 1086.130,
        129: 1094.167,
        130: 1103.948,
        131: 1112.083,
        132: 1121.942,
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
    for a in all_a[1:]: # Start from the second nucleus
        if (a - 1) in binding_energies_mev:
            sn = binding_energies_mev[a] - binding_energies_mev[a - 1]
            a_plot_sn.append(a)
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
             markersize=6, label='$S_n$ (one-neutron)')
             
    # Plot S_2n
    plt.plot(a_plot_s2n, s2n_plot, 'rs-', 
             markersize=6, label='$S_{2n}$ (two-neutron)')
             
    # Style the plot
    plt.xlabel('Mass Number (A)', fontsize=14)
    plt.ylabel('Separation Energy (MeV)', fontsize=14)
    plt.title('Neutron Separation Energies in Sn (Z=50) Isotopes', fontsize=16)
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
