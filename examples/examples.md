[mmtb](../README.md)/examples

# Code Examples

> [!NOTE]
>Each code example begins by selecting the experiments to be evaluated. To do this, a graphical user interface opens when you run a code example script.
>The window contains three panes: the upper left frame lists all available experiments, the lower left frame lists all currently selected experiments, and the right frame displays experiment information.
>An experiment can be added to the selected list of experiments either by double-clicking on it or by simply selecting it with a single click and using the associated `Add' button.
>An experiment can be removed from this list in almost the same way.
>
>![grafik](https://github.com/user-attachments/assets/b59a1c91-f60d-462c-8a75-e57eefac7e3e)
>
>Initially only 3 experiments will be shown, but by adding the `mmtb.db` from [Zenodo](https://zenodo.org/uploads/13898880) the list of experiments will be extended.
>
>A filter function is also available to filter the available experiments according to selected parameters. Click on the 'Filter' button, check the parameters you want to filter and set their values accordingly.
>
>After selecting the experiments and pressing the `Confirm` button, the window closes and the evaluation begins.

## Plotting and Basic Usage
+ **plotting_example.py**:

  Plots RX and TX data over time for the selected experiments.

+ **basic_use_example.py**:

  Access and convert important data from selected experiments into numpy arrays for further use.

## Synchronization
+ **corr_sync_example.py**:

  Plots the normalized fluorescence and the **correlation-based** metric function over time.
  The gray vertical lines indicate the estimated points of synchronization.

+ **dcorr_sync_example.py**:

  Plots the normalized fluorescence and the **differential-correlation-based** metric function over time.
  The gray vertical lines indicate the estimated points of synchronization.

## Detection
+ **corr_detec_example.py**:

  Displays the detection samples over time in a scatter plot, where each detection sample is color-coded based on its associated symbol (baseline truth).
  In addition, the plot includes thresholds used to discriminate between the detection samples, as well as the **correlation-based** metric function from which the detection samples were drawn.

+ **dcorr_detec_example.py**:

  Displays the detection samples over time in a scatter plot, where each detection sample is color-coded based on its associated symbol (baseline truth).
  In addition, the plot includes thresholds used to discriminate between the detection samples, as well as the **differential-correlation-based** metric function from which the detection samples were drawn.
