# Script: Writing Readme Files

## Data ecosystem in Python

## Metrics stack

## Basic machine learning stack

- scikit-learn

- xgboost

  - machine learning algorithms under the gradien boosting framework (e.g., gradient
    boosted trees)

  - very good start for regression / prediction problems

  - can be integrated into scikit-learn workflow

- sktime

  - unified interface for time series learning tasks (e.g., forecasting, classification,
    clustering, etc.)

  - implements lots of algorithms and is compatible with scikit-learn

- keras

  - simple, but powerful, entry point to neural networks and deep learning

  - framework agnostic (pytorch, jax, ...)

- pymc

  - bayesian modeling and probabilistic programming

- ...

## Advanced machine learning stack

- (jax and pytorch in bold because they are frameworks)

- jax

  - developed at google and nvidia

  - accelerator-oriented array computation (run on CPU, GPU, TPU)

  - designed for high-performance numerical computing and machine learning

- flax

  - neural networks and deep learning ecosystem for jax

- pytorch

  - developed at meta AI

  - very similar to jax

  - on top of jax: has built-in support for neural networks, optimizers, etc.

- torchvision

  - algorithms and common transformations for computer vision

- transformers

  - APIs and tools to download / train state-of-the-art pretrained models

  - natural Language Processing, Computer Vision, Audio, Multimodal

  - framework agnostic (jax, pytorch)

- ...
