# Central Limit Theorem (CLT) Interactive Demo

An interactive web application that visually demonstrates the Central Limit Theorem using Streamlit. Users can explore how sample means from different population distributions converge to a normal distribution as sample size increases.

## Key Features

- **Interactive controls** for:
  - Population distribution selection (Uniform, Normal, Exponential)
  - Adjustable sample size (1-500)
  - Adjustable number of samples (1-10000)
- **Visualizations**:
  - Population distribution histogram
  - Sampling distribution of sample means
  - Theoretical normal curve predicted by CLT
- **Real-time parameter display**:
  - Population mean (μ)
  - Theoretical standard error (σ/√n)


## Requirements
- Python 3.7+
- streamlit
- numpy
- matplotlib
- scipy

## Understanding CLT

The Central Limit Theorem (CLT) states that the average of independent random variables approaches a normal distribution as the sample size increases, regardless of the original population's distribution. This demo illustrates:
- Convergence to normality with larger sample sizes
- Decreasing standard error as sample sizes grow
- CLT's independence from the shape of the population distribution

🔗 [Check out the application here!](https://clt-demo-app.streamlit.app/)
![Demo Screenshot](image/app-screenshot.png)