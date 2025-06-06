import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # Import norm for normal distribution

# --- App Title and Description ---
st.title("Central Limit Theorem Demonstration")
st.markdown("""
This application provides an interactive demonstration of the **Central Limit Theorem (CLT)**.

The CLT states that the distribution of sample means of a large number of samples taken from a population will be approximately normally distributed, regardless of the shape of the original population's distribution.

**Instructions:**
1.  Use the sidebar to select a population distribution.
2.  Adjust the sample size and the number of samples using the sliders.
3.  Observe how the distribution of sample means (bottom plot) approaches a normal distribution as you increase the sample size and number of samples.
""")

# --- Sidebar for User Input ---
st.sidebar.header("Simulation Parameters")

# Dropdown to select the population distribution
distribution_options = ["Uniform", "Normal", "Exponential"]
selected_distribution = st.sidebar.selectbox(
    "Select a Population Distribution", distribution_options
)

# Sliders to adjust sample size and number of samples
sample_size = st.sidebar.slider(
    "Sample Size (n)", min_value=1, max_value=500, value=30, step=1
)
num_samples = st.sidebar.slider(
    "Number of Samples", min_value=1, max_value=10000, value=500, step=10
)

# --- Data Generation ---

# Generate the population based on user selection
population_size = 100000
if selected_distribution == "Uniform":
    population = np.random.uniform(0, 10, population_size)
    distribution_params = "from 0 to 10"
elif selected_distribution == "Normal":
    population = np.random.normal(5, 2, population_size)
    distribution_params = "with mean 5 and standard deviation 2"
else:  # Exponential
    population = np.random.exponential(2, population_size)
    distribution_params = "with a scale of 2"

# Generate the sample means
sample_means = [
    np.mean(np.random.choice(population, size=sample_size)) for _ in range(num_samples)
]

# --- Visualization ---

# Create two columns for the plots
col1, col2 = st.columns(2)

# Plot the population distribution
with col1:
    st.subheader(f"Population Distribution ({selected_distribution})")
    fig1, ax1 = plt.subplots()
    ax1.hist(population, bins=50, density=True, color="skyblue", edgecolor="black", alpha=0.7)
    ax1.set_title(f"Population: {selected_distribution} {distribution_params}")
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Density")
    st.pyplot(fig1)

# Plot the distribution of sample means
with col2:
    st.subheader("Distribution of Sample Means")
    fig2, ax2 = plt.subplots()
    
    # Plot histogram of sample means
    ax2.hist(sample_means, bins=50, density=True, color="salmon", edgecolor="black", alpha=0.7)
    
    # Calculate parameters for normal distribution
    population_mean = np.mean(population)
    population_std = np.std(population)
    std_error = population_std / np.sqrt(sample_size)
    
    # Generate points for normal curve
    xmin, xmax = ax2.get_xlim()
    x = np.linspace(xmin, xmax, 1000)
    y = norm.pdf(x, population_mean, std_error)
    
    # Plot the density curve
    ax2.plot(x, y, 'k-', linewidth=2, label='CLT Normal Distribution')
    
    ax2.set_title(
        f"Sample Means (n={sample_size}, samples={num_samples})"
    )
    ax2.set_xlabel("Sample Mean")
    ax2.set_ylabel("Density")
    ax2.legend()
    st.pyplot(fig2)

# --- Explanation of Results ---
st.markdown("---")
st.header("Key Observations")
st.write(f"""
- **Population Distribution:** The plot on the left shows the distribution of the original population data. Notice its shape, which is {selected_distribution.lower()}.
- **Distribution of Sample Means:** The plot on the right displays the distribution of the means of the samples taken from the population. The black curve shows the theoretical normal distribution predicted by the CLT.
- **The Magic of CLT:** As you increase the **Sample Size** and **Number of Samples**, you'll notice that:
    1. The histogram of sample means becomes more bell-shaped
    2. The histogram converges to the theoretical normal curve
    3. The spread decreases as sample size increases (narrower curve)
- **Key Parameters:** 
    - Population mean (μ) = {population_mean:.2f}
    - Theoretical standard error (σ/√n) = {std_error:.4f}
""")