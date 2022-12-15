"""
Contains function for loading, batching and converting data.
"""

from itertools import islice
from typing import Iterable, List, Tuple

import numpy as np
import torch

import datasets
from datasets.dataset_dict import DatasetDict

from gensim.models.keyedvectors import KeyedVectors
from torch import nn
import random

def load_data() -> DatasetDict:
    """Load the conllpp dataset.

    Returns:
        DatasetDict: A dictionary containing the train, test and dev sets.
    """
    dataset = datasets.load_dataset("conllpp")
    return dataset


def load_sst2() -> DatasetDict:
    """load the sst2 dataset. Do note that the test, train set here does correspond to the original test and train set. 
    As the official test set is hidden (to ensure that researcher does not accidentally or intentionally train on it) 
    we have created a new test set by using excluding 1000 random samples from the train set.

    Returns:
        DatasetDict: A dictionary containing the train, test and dev sets.
    """

    dataset = datasets.load_dataset("glue", "sst2")

    # don't change the seed or n_test
    random.seed(10) # seed to ensure the test set is the same for everyone
    n_test = 1000 # number of test samples
    bool_is_test = [0 if i >= n_test else 1 for i in range(dataset["train"].num_rows)]
    random.shuffle(bool_is_test)
    
    # create list of indices for the test and train set
    test_idx = [i for i, is_test in enumerate(bool_is_test) if is_test]
    train_idx = [i for i, is_test in enumerate(bool_is_test) if not is_test]


    # overwrite existing test and train set
    dataset["test"] = dataset["train"].select(np.array(test_idx))
    dataset["train"] = dataset["train"].select(np.array(train_idx))

    return dataset



def batch(dataset: Iterable, batch_size: int) -> Iterable:
    """Creates batches from an iterable.

    Args:
        dataset (Iterable): Your dataset you want to batch given as an iterable (e.g. a list).
        batch_size (int): Your desired batch size

    Returns:
        Iterable: An iterable of tuples of size equal to batch_size.

    Example:
        >>> batches = batch([1,2, 3, 4, 5], 2)
        >>> print(list(batches))
        [(1, 2), (3, 4), (5,)]
    """
    iterable_dataset = iter(dataset)
    while True:
        chunk = tuple(islice(iterable_dataset, batch_size))
        if not chunk:  # when the dataset/chunk is empty break the while loop
            break
        yield chunk


def gensim_to_torch_embedding(gensim_wv: KeyedVectors) -> Tuple[nn.Embedding, dict]:
    """
    Convert a gensim KeyedVectors object into a pytorch Embedding layer.

    Args:
        gensim_wv: gensim KeyedVectors object

    Returns:
        torch.nn.Embedding: torch Embedding layer
        dict: dictionary of word to index mapping
    """
    embedding_size = gensim_wv.vectors.shape[1]

    # create unknown and padding embedding
    unk_emb = np.mean(gensim_wv.vectors, axis=0).reshape((1, embedding_size))
    pad_emb = np.zeros((1, gensim_wv.vectors.shape[1]))

    # add the new embedding
    embeddings = np.vstack([gensim_wv.vectors, unk_emb, pad_emb])

    weights = torch.FloatTensor(embeddings)

    emb_layer = nn.Embedding.from_pretrained(embeddings=weights, padding_idx=-1)

    # creating vocabulary
    vocab = gensim_wv.key_to_index
    vocab["UNK"] = weights.shape[0] - 2
    vocab["PAD"] = emb_layer.padding_idx

    return emb_layer, vocab

def prepare_batch(tokens: List[List[str]], labels: List[List[int]]) -> Tuple[torch.Tensor, torch.Tensor]:
    """Prepare a batch of data for training.

    Args:
        tokens (List[List[str]]): A list of lists of tokens.
        labels (List[List[int]]): A list of lists of labels.

    Returns:
        Tuple[torch.Tensor, torch.Tensor]: A tuple of tensors containing the tokens and labels.
    """    
    pass