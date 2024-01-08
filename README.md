# Processed-Data

This repository stores the preprocessed data for paper: 
<br>[SignDiff: Learning Diffusion Models for American Sign Language Production](https://arxiv.org/abs/2308.16082)

## How2Sign for ASLP

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- https://drive.google.com/file/d/1fGSrRAxhik2hTr9m4yut_IgsVuKvlsVe/view?usp=sharing

It can be used in the training of ASL production models. 
<br>*Note: Because I later processed more data, the link above is four times the size of the one in the paper and is the result of the full How2Sign processing.*

## Phoenix-14T for GSLP

After preprocessing [Phoenix-14T](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/) dataset, the condensed data set obtained is as follows:

- https://drive.google.com/file/d/1O60O-pTEso5FWQ8GJdJKVvb87UE5jsu-/view?usp=sharing

It can be used in the training of GSL production models.

## How2Sign for SignDiff

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- https://drive.google.com/file/d/1DHmePcRpc5TJ1XkjOfA8VYKKLGCL8nlJ/view?usp=sharing

It can be used for the diffusion model training of pose2video in sign language. (Based on [ControlNet](https://github.com/lllyasviel/ControlNet/blob/main/docs/train.md))

## How2Sign for Vid2Vid

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- https://aistudio.baidu.com/datasetdetail/220064

It can be used for the diffusion model training of pose2video in sign language. (Based on [Vid2Vid](https://github.com/NVIDIA/vid2vid))

## Tool for Data

Our pre-processing tools: the data cleansing tool and the three-step 2Dto3D tool.

Stay tuned. The data above should be sufficient for the time being.

## Related Work

- https://github.com/BenSaunders27/ProgressiveTransformersSLP
