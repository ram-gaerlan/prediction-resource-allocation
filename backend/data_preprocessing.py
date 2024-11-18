import pandas as pd
import numpy as np


# Function to combine mock data (weather, demographic, topographic)
def combine_data():
    # Create mock data for weather, demographic, and topography
    weather_data = {'temperature': np.random.uniform(20, 30, 5), 'humidity': np.random.uniform(50, 80, 5)}
    demographic_data = {'population': np.random.randint(500, 1000, 5), 'households': np.random.randint(100, 300, 5)}
    topographic_data = {'altitude': np.random.uniform(0, 200, 5), 'slope': np.random.uniform(0, 30, 5)}

    # Combine data into a single DataFrame
    data = pd.DataFrame({**weather_data, **demographic_data, **topographic_data})
    return data
