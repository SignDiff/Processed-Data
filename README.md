# Processed-Data

This repository stores the preprocessed data for paper: 
<br>[SignDiff: Learning Diffusion Models for American Sign Language Production](https://arxiv.org/abs/2308.16082)

**Note:** We're going to start a company, and the code is not going to be public.

## How2Sign for ASLP

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- [https://huggingface.co/datasets/SignDiff/how2sign-pre.zip](https://huggingface.co/datasets/FangSen9000/SignDiff/blob/main/how2sign-pre.zip)

It can be used in the training of ASL production models. 
<br>*Note: Because I later processed more data, the link above is four times the size of the one in the paper and is the result of the full How2Sign processing.*

## Phoenix-14T for GSLP

After preprocessing [Phoenix-14T](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/) dataset, the condensed data set obtained is as follows:

- [https://huggingface.co/datasets/SignDiff/phoenix-pre.zip](https://huggingface.co/datasets/FangSen9000/SignDiff/blob/main/phoenix-pre.zip)

It can be used in the training of GSL production models.

## How2Sign for SignDiff

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- [https://huggingface.co/datasets/SignDiff/How2Sign-Diff.zip](https://huggingface.co/datasets/FangSen9000/SignDiff/blob/main/How2Sign-Diff.zip)

It can be used for the diffusion model training of pose2video in sign language. (Based on [ControlNet](https://github.com/lllyasviel/ControlNet/blob/main/docs/train.md))

## How2Sign for Vid2Vid

After preprocessing [How2Sign](https://how2sign.github.io/) dataset, the condensed data set obtained is as follows:

- https://aistudio.baidu.com/datasetdetail/220064

It can be used for the GAN model training of pose2video in sign language. (Based on [Vid2Vid](https://github.com/NVIDIA/vid2vid))

## Tool for Data

Our pre-processing tools: the data cleansing tool at [SignDiff/tool](https://github.com/SignDiff/Processed-Data/tree/main/tools).

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

@misc{fang2025signdiffdiffusionmodelamerican,
      title={SignDiff: Diffusion Model for American Sign Language Production}, 
      author={Sen Fang and Chunyu Sui and Yanghao Zhou and Xuedong Zhang and Hongbin Zhong and Yapeng Tian and Chen Chen},
      year={2025},
      eprint={2308.16082},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2308.16082}, 
}
```

## Related Work

- https://github.com/BenSaunders27/ProgressiveTransformersSLP
- https://github.com/lllyasviel/ControlNet
