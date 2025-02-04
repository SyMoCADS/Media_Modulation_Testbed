[mmtb](../../README.md)/[dtypes](../dtypes.md)/SynchronizationData

# mmtb.dtypes.SynchronizationData

**class** <span style="color:purple;">SynchronizationData</span> (metric_coeffs: DataPointList | None, detection_metric_coeffs: DataPointList | None)

> Parameters

+ `metric_coeffs: DataPointList | None`
+ `detection_metric_coeffs: DataPointList | None`

> Attributes

+ `metric_coeffs: DataPointList`
+ `detection_metric_coeffs: DataPointList`
+ `symbol_starts: list`

> Methods

+ <span style="color:mediumpurple;">append\_ metric\_coeff</span> (metric_coeff: DataPoint) -> `None`

    Appends the DataPoint to metric_coeffs.

+ <span style="color:mediumpurple;">append_detection_metric_coeff</span>  (detection_metric_coeff: DataPoint) -> `None`

    Appends the DataPoint to detection_metric_coeffs.

+ <span style="color:mediumpurple;">extend_metric_coeff</span> (metric_coeffs: DataPointList) -> `None`

    Extends metric_coeffs by the DataPointList.

+ <span style="color:mediumpurple;">extend_detection_metric_coeff</span> (detection_metric_coeffs: DataPointList) -> `None`

    Extends detection_metric_coeffs by the DataPointList.