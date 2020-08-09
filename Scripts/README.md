# VIBE Data parsing scripts

This folder contains script which can be used to parse the VIBE skeleton data of skeletics-152 and skeleton-mimetics

There are two main scripts:

1. <b>create_vacnn_data.py</b> (Parses VIBE data into VaCNN format)
2. <b>create_gcn_data.py</b> (Parses VIBE data into GCN format)


- VaCNN data is stored in <b>.h5</b> format
- GCN data is stored in <b>.npy</b> format

### GCN data structure:

GCN data is stored is most standard format used by most of the GCN based models.

The data is stored in <b>N x C x T x V x M </b>, where
- N = Number of samples
- C = Number of channels (C = 3 for 3d data)
- T = Number of Frames (T = 300 by default)
- V = Number of Joints (V = 25 by default)
- M = Number of Persons (M = 2 by default)


### How to run scripts

```python3 create_vacnn_data.py INPUT_PATH OUTPUT_PATH```


```python3 create_gcn_data.py INPUT_PATH OUTPUT_PATH```

 Where

 - INPUT_PATH =  path to the directory containing VIBE .json files
 - OUTPUT_PATH =  path where parsed data needs to be saved.
