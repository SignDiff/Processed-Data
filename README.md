# Processed-Data

This repository stores the preprocessed data for paper: 
<br>[SignDiff: Learning Diffusion Models for American Sign Language Production](https://arxiv.org/abs/2308.16082)

**Note:** This work has not been accepted yet, and I am currently very busy and do not have time to submit my paper at a recent academic conference. Maybe it will be accepted at some conference in the fall and that might be a good time to open up the code.

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

It can be used for the GAN model training of pose2video in sign language. (Based on [Vid2Vid](https://github.com/NVIDIA/vid2vid))

## Tool for Data

Our pre-processing tools: the data cleansing tool and the three-step 2Dto3D tool.

Stay tuned. The data above should be sufficient for the time being.

```
@misc{fang2024signllm,
      title={SignLLM: Sign Languages Production Large Language Models}, 
      author={Sen Fang and Lei Wang and Ce Zheng and Yapeng Tian and Chen Chen},
      year={2024},
      eprint={2405.10718},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{fang2023signdiff,
      title={SignDiff: Learning Diffusion Models for American Sign Language Production}, 
      author={Sen Fang and Chunyu Sui and Xuedong Zhang and Yapeng Tian},
      year={2023},
      eprint={2308.16082},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Related Work

- https://github.com/BenSaunders27/ProgressiveTransformersSLP
- https://github.com/lllyasviel/ControlNet
