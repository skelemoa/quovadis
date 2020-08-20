# Pre Trained Models

This folder contains pre trained models weights for the different models trained and mentioned in the paper.

There 3 sub folder within this folder, namely:

1. <b>NTU 120</b> (Contains model weights for NTU 120 datasets)
2. <b>skeletics-152</b> (Contains models weights for skeletics-152 dataset)
3. <b>skeleton-mimetics</b> (Contains models weights for skeleton-mimetics dataset)

The weights are stored in standard <b>.pt</b> format, and can be easily used using the method mentioned in respective model github repo.

<i><b>NOTE: </b>Pre trained model weights for VaCNN on NTU 120 can be dowloaded from here. [Cross Subject](https://drive.google.com/file/d/1gbJ2c8TwqMdPQfdrZYAtCHMihx7P8tjx/view?usp=sharing) and [Cross Setup](https://drive.google.com/file/d/1PmdHy7kuP4LWSTYvurvpv0rUjCnf1Ava/view?usp=sharing)

### Naming Convention:

The weight files are named in according to the dataset on which it is trained, stream name and epoch number.

For example, <i>ntu_xset_2sSDGCN_bone_epoch_31.pt</i> file contains weight for 2s-SDGCN model's bone stream trained on NTU-120 Cross setup(Xset) till epoch 31

And similarly all other model weight files are named

<i><b>NOTE: MsG3D requires 2 separate files for weights and checkpoints, which are added using " weights " and " checkpoint " in the file name</i></b>


### Github repo link for Models:

Following is the list of different models codes. Instruction to use pretrained weights are given in the README of each of the models:

- [MsG3D](https://github.com/kenziyuliu/MS-G3D)
- [ShiftGCN](https://github.com/kchengiva/Shift-GCN)
- [VaCNN](https://github.com/microsoft/View-Adaptive-Neural-Networks-for-Skeleton-based-Human-Action-Recognition)
- [DgNN](https://github.com/kenziyuliu/Unofficial-DGNN-PyTorch)
- [GCN-NAS](https://github.com/xiaoiker/GCN-NAS)
