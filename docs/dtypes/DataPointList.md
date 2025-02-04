[mmtb](../../README.md)/[dtypes](../dtypes.md)/DataPointList

#mmtb.dtypes.DataPointList

**class** <span style="color:purple;">DataPointList</span> (time: Sequence[float | datetime], value: Sequence[float])

> Parameters

+ `times: Sequence[float | datetime]`
+ `values: Sequence[float]`

> Attributes

+ `times: list[float | datetime]`
+ `values: list[float]`

> Methods

+ <span style="color:mediumpurple;">\_\_ len\_\_</span> (None) -> `int`
    
    Dunder method that returns the length of the DataPointList.

+ <span style="color:mediumpurple;">\_\_iter\_\_</span> (None) -> `Iterator`
    
    Dunder method that returns an Iterator for DataPointList, which upon calling `__next__()` return a DataPoint.

+ <span style="color:mediumpurple;">\_\_getitem\_\_</span> (index: int | slice) -> `DataPoint | DataPointList`
    
    This dunder method returns either the specified entry from the DataPointList as a DataPoint if the index is of type `int`, or returns the specified section of the DataPointList as a separate DataPointList if the index is of type `slice`.

+ <span style="color:mediumpurple;">append</span> (data_point: DataPoint) -> `None`

    Appends a DataPoint to the DataPointList.

+ <span style="color:mediumpurple;">extend</span> (other: DataPointList) -> `None`

    Extends the DataPointList by the other given DataPointList.

+ <span style="color:mediumpurple;">pop</span> (index: int) -> `None`

    Removes an entry from the DataPointList at the specified index.

+ <span style="color:mediumpurple;">clear</span> (None) -> `None`

    Clears the entire DataPointList, removing all entries.