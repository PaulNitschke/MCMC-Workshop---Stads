import numpy as np
import pandas as pd
import seaborn as sns

def generate_data(num_samples:int = 50, num_modes:int = 2, mu:list = [-2, 2], sigma: list = [1, 1], name: str = None) -> np.ndarray:

    '''
    Generates Gaussian Mixture Model data.

    Args:
    - num_samples, required, the number of samples, for a higher amount of samples our algorithms become numerically unstable, so consider a value around 50.as_integer_ratio
    - num_modes, required, the number of Gaussian distributions
    - mu, required, the means of the respective normal distributions, example: mu = [-2, 2] is a GMM with means at -2 and 2
    - sigma, required, the deviations of the respective normal distributions, example: sigma = [1,1] is a GMM with unit variance
    - name, optional, name of the data so that it can be saved

    Returns:
    - a numpy array of the samples
    - if name, saves the numpy array to a csv
    '''
    
    np.random.seed(420)
    samples = np.zeros(num_samples)

    which_mode = np.random.multinomial(1, [1/num_modes]*num_modes, size = num_samples)

    for idx_mode in range(num_modes):
        samples_mode = np.random.normal(loc = mu[idx_mode], scale = sigma[idx_mode], size = num_samples) * which_mode[:,idx_mode]
        samples = samples + samples_mode
    
    if name:
        pd.DataFrame(samples).to_csv(f"{name}.csv")

    return samples

def visualize_data(data: np.array):
    sns.set_style('whitegrid')
    _ = sns.kdeplot(data)