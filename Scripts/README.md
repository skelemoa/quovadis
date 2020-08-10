# VIBE Data parsing scripts

This folder contains script which can be used to parse the VIBE skeleton data of skeletics-152 and skeleton-mimetics

There is one main script:

1. <b>parse_vibe_data.py</b> (Parses VIBE data into VaCNN and GCN format)


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


### How to run script

```python3 parse_vibe_data.py INPUT_PATH OUTPUT_PATH```

 Where

 - INPUT_PATH =  path to the directory containing VIBE .json files
 - OUTPUT_PATH =  path where parsed data needs to be saved.

After the script is finished a <b>vacnn_data.h5</b> file will be created with VaCNN data and labels.

Also two more files will be created, <b> gcn_train_data.npy </b> and <b> gcn_train_label.npy </b> which will contain data and label respectively.

<i><b>(NOTE: To parse different splits of dataset give the input path accordingly)</i></b>
