import math
import time
import pandas as pd
import numpy as np

import tensorflow.compat.v2 as tf
import tensorflow_probability as tfp


class MCMC_competition:


    def __init__(self, data) -> None:
        self.data = pd.read_csv(data, index_col = "Unnamed: 0")

    
    def target_log_prob(self, param):

        '''
        Log density of our two-dimensional GMM.
        '''

        mu_1, mu_2, sigma_1, sigma_2 = param
        
        log_dens = tf.math.reduce_sum(tf.math.log(
            1/(2*tf.math.sqrt(2*math.pi*sigma_1**2)) * tf.math.exp(-0.5*(self.data - mu_1)**2/sigma_1**2) + 
            1/(2*tf.math.sqrt(2*math.pi*sigma_2**2)) * tf.math.exp(-0.5*(self.data - mu_2)**2/sigma_2**2))) - 0.5 * (mu_1**2 + mu_2**2) - (sigma_1 + sigma_2)
        
        return(log_dens)


    def sample_GMM(self):

        start_time = time.time()

        '''
        Your Code starts here
        '''

        #User Inputs
        dtype = np.float32
        init_state = dtype([1, 1, 1, 1])
        num_samples = 1000
        num_burnin = 250
        kernel = tfp.mcmc.MetropolisAdjustedLangevinAlgorithm(
                target_log_prob_fn=self.target_log_prob,
                step_size=0.03)

        #Generate Samples
        samples = tfp.mcmc.sample_chain(
            num_results=num_samples,
            current_state=init_state,
            kernel=kernel,
            num_burnin_steps=num_burnin,
            trace_fn=None,
            seed=42)

        #Calculate ESS
        effective_sample_size = tfp.mcmc.effective_sample_size(samples).numpy()
        ESS_mean = round(np.mean(effective_sample_size))


        '''
        Your Code ends here
        '''

        end_time = time.time()

        #Metrics
        duration_sec = end_time - start_time
        Ess_per_sec = round(ESS_mean/duration_sec, 2)

        return(Ess_per_sec)