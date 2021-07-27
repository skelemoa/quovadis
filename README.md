[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/quo-vadis-skeleton-action-recognition/skeleton-based-action-recognition-on-ntu-rgbd-1)](https://paperswithcode.com/sota/skeleton-based-action-recognition-on-ntu-rgbd-1?p=quo-vadis-skeleton-action-recognition)

# Quo Vadis, Skeleton Action Recognition ?

This repository contains datasets and scripts for the paper <a href="https://arxiv.org/pdf/2007.02072v1.pdf">Quo Vadis, Skeleton Action Recognition ?</a>, accepted for publication at International Journal of Computer Vision <i> IJCV </i>.

This paper primarily contributes towards benchmarking of exisiting skeleton human action recognition models on larger datasets like <a href = "http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp">NTU-120</a> and also provides insight on how these models performs for *in the wild* data as well.

<img src = "static/main_datasets.png"/>

We also introduce 3 new skeleton human action datasets:

- [Skeletics-152](./skeletics-152/)
- [Skeleton-mimetics](./skeleton-mimetics/)
- [Metaphorics](./metaphorics/)

The details about each of these datasets can be found in [skeletics-152 README](./skeletics-152/README.md), [skeleton-mimetics README](./skeleton-mimetics/README.md) and [metaphorics README](./metaphorics/README.md).

### Pre Trained models

This repository contains pre-trained model weights for all the models that were trained as mentioned in the paper. The weights of different models for different datasets can be found [here](./Pre%20Trained%20Models/)

### Scripts

The scripts needed to parse VIBE skeleton data into usable VA-CNN and GCN formats can be found [here](./Scripts/)

### Citation
```
@article{Gupta2021,
author={Gupta, Pranay and Thatipelli, Anirudh and Aggarwal, Aditya and Maheshwari, Shubh and Trivedi, Neel and Das, Sourav and Sarvadevabhatla, Ravi Kiran},
title={Quo Vadis, Skeleton Action Recognition?},
journal={International Journal of Computer Vision},
year={2021},
month={May},
day={05},
issn={1573-1405},
doi={10.1007/s11263-021-01470-y},
url={https://doi.org/10.1007/s11263-021-01470-y}
}
```
