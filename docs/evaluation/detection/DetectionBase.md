[mmtb](../../../README.md)/[evaluation](../..//evaluation.md)/[detection](../detection.md)/DetectionBase

## mmtb.types

**class** <span style="color:purple;">DetectionBase</span> (detec_data: DetectionData | None, skip_n_symbols: int = 0)

This class represents the base class for any detector, which may be used to write a custom detection by inheriting from class and implementing the abstract methods.

> Parameters:
+ `detec_data: DetectionData | None`

    Dataclass to store the detection data for later analysis.

+ `skip_n_symbols: int` ( &middot; &ge; 0)

    Number of initially transmitted symbols ignored/skipped (usually due to rapidly changing fluorescence at the start of a transmission).

> Methods

+ **@abstractmethod** <span style="color:mediumpurple;">\_\_call\_\_</span> (sample_val: float | None) -> `str | None`

    This is the `__call__` abstract dunder method for this class, which receives data sequentially. Returns the detect symbol character in form of a `str` upon succesful detection; otherwise returns `False`.

    `Note`: If *sample_val* is `None` the implemented method should return immediately.