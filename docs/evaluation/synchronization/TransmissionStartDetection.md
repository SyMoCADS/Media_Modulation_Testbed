[mmtb](../../../README.md)/[evaluation](../..//evaluation.md)/[synchronization](../synchronization.md)/TransmissonStartDetection

## mmtb.types

**class** <span style="color:purple;">TransmissonStartDetection</span>
 (training_data_length: int, false_alarm_probaility: float)

> Parameters:

+ `training_data_length: int` ( &middot; > 0)

    Number of consecutive samples used to determine the start of transmission detection threshold.

+ `false_alarm_probaility: float` (0 < &middot; < 1)

    Specifies the false alarm probability (left tail probability) of transmission start detection.

> Methods

+ <span style="color:mediumpurple;">\_\_call\_\_</span> (sample_val: float) -> `bool`

    This is the `__call__` dunder method for this class, which receives data sequentially. Returns `True` only if a transmission has been detected, i.e., a sample has fallen below the previously calculated threshold; otherwise returns `False`.


+ <span style="color: mediumpurple;">enough_training_samples</span> (None) -> `bool`

    Returns `True` if enough samples have been collected to from the first training data set.