import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from mmtb.experiments import get_selected_experiments


matplotlib.rcParams["font.family"] = "Arial"
matplotlib.rcParams["font.size"] = 15

##################
# !!! Notes !!!  # 
################################################################################################################################################
# - This sample code demonstrates the general retrieval of data from the data classes in ExperimentData, using a few data classes as examples. #
# - See the documentation for more details.                                                                                                    #
################################################################################################################################################

if __name__ == "__main__":


    # Get experiment data (3 options):
    experiment_data = get_selected_experiments() # Opens up the window for experiment selection
    #experiment_data = get_selected_experiments(select_files=['(2024-08-22) NMSED_5s_wEX_RT_6cm']) # Direct experiment data acces without selection window
    #experiment_data = get_selected_experiments(use_prev_selected_files=True) # Uses previously selected experiments; if no previously selected exist for the current file exist, will raise error.


    # Loops thorugh all selected experiment data
    for experiment in experiment_data: # Iterates through list of ExperimentData instances.
        
        # RX-related data
        rx_fluorescence_values = np.array(experiment.rx_data.fluorescence_vals)
        rx_raw_intensity_values = np.array(experiment.rx_data.intensity_vals)
        rx_relative_time_values = np.array(experiment.rx_data.rel_times)
        rx_timestamps_values = np.array(experiment.rx_data.timestamps)

        # TX-related data
        tx_intensity_values = np.array(experiment.tx_data.intensity_vals)
        tx_relative_times = np.array(experiment.tx_data.rel_times)
        tx_timestamps_values = np.array(experiment.tx_data.timestamps)
        tx_event_symbols = np.array(experiment.tx_data.event_symbols)

        # For ease of use, TxData includes a convenient method of obtaining the TX intensity function (e.g. for plotting).
        tx_itensity_function = experiment.tx_data.intensity_function() # Retruns DataPointList instance.

        
        plt.plot(tx_itensity_function.times, tx_itensity_function.values)
        plt.ylabel("TX Intensity [%]")
        plt.xlabel("Time [s]")
        plt.show()