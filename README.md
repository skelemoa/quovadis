[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/quo-vadis-skeleton-action-recognition/skeleton-based-action-recognition-on-ntu-rgbd-1)](https://paperswithcode.com/sota/skeleton-based-action-recognition-on-ntu-rgbd-1?p=quo-vadis-skeleton-action-recognition)

# Quo Vadis, Skeleton Action Recognition ?

This repository contains datasets and scripts for the paper <a href="https://arxiv.org/pdf/2007.02072v1.pdf">Quo Vadis, Skeleton Action Recognition ?</a>

This paper primarily contributed towards benchmarking of exisiting skeleton human action recognition models on larger datasets like <a href = "http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp">NTU-120</a> and also provides insight on how these models performs for *in the wild* data as well.

<img src = "static/main_datasets.png"/>

This paper introduced 2 new skeleton human action datasets:

- Skeletics-152
- Skeleton-mimetics
- Metamorphics

The details about each of these datasets can be found in [skeletics-152 README](./skeletics-152/README.md), [skeleton-mimetics README](./skeleton-mimetics/README.md) and [metamorphics README](./metamorphics/README.md).

### Pre Trained models

This repository contains pre trained models weights for all the models that were trained as mentioned in the paper. The weights of different models for different datasets can be found [here](./Pre%20Trained%20Models/)

### Scripts

This repository contains scripts needed to parse the VIBE skeleton data into usable VaCNN and GCN formats. The scripts and instructions to use those scripts can be found [here](./Scripts/)

### Citation
```
@misc{gupta2020quo,
    title={Quo Vadis, Skeleton Action Recognition ?},
    author={Pranay Gupta and Anirudh Thatipelli and Aditya Aggarwal and Shubh Maheshwari and Neel Trivedi and Sourav Das and Ravi Kiran Sarvadevabhatla},
    year={2020},
    eprint={2007.02072},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
