# Assignment 4: Named entity recognition using LSTMs

In this assignment, the goal  is to use LSTMs and word embeddings to detect named entities in unstructured texts.

This assignment is a bit larger than what you have worked on already and might take some time - both in terms of coding but also in terms of training and experimenting with the LSTM models.

I have also included a directory for what is called *unit testing* -  a process of checking code to make sure that it's working as expected. The pre-implemented tests should pass and that you are welcome to add more tests. You can read more here about [testing](https://realpython.com/python-testing/) and [Github workflows](https://docs.github.com/en/actions/using-workflows/about-workflows).

Please also tick off the boxes if you have completed the task by putting an X in the box in the markdown for this description.

## Assignment tasks

You are provided with:
- A trainable LSTM model using word embeddings, written in ```pytorch```.
- Some utility classes and functions for converting word embeddings to ```pytorch``` format.
- A skeleton outline for a ```main.py``` function.

You will need to:

- [ ] Complete the documentation on existing classes and functions by adding docstrings and code comments.
- [ ] Complete the `prepare_batch` function in the module [data.py](../ner/data.py). This functions prepares a batch of inputs for the LSTM. 
  - *Hint:* examine the starter code from the classroom notebook. If this takes a long time you can always save the processed dataset and read it in.
- [ ] Train an LSTM model trained for English NER using the conllpp dataset. This should include two experiments:
  - [ ] One comparing the effect of the word embedding size, you can see available word embedding on gensim [here](https://github.com/RaRe-Technologies/gensim-data).
  - [ ] And one other which you select yourself, such as:
    - Compare the effect of the hidden layers size of the LSTM
    - Compare a bidirectional LSTM with your unidirectional LSTM (You can do this by setting the `bidirectional=True`)
    - Compare the effect of different word embeddings of similar size (e.g. trained on different domains)
    - Compare the `nn.RNN` as opposed to the `nn.LSTM` block
    - Compare the effect of different optimizers
  - [ ] Your training loop should periodically be applied to the validation set. If the model performs better save it. You can save the model using `torch.save` and load it using `torch.load`.
    - [ ] This is known as early stopping: If the model hasn't improved in over N epochs (e.g. 10 epochs), stop the training. 
  - [ ] Using the best performing model calculate the (micro) F1 score and accuracy of the model on the test set. To do this, you should use the ```seqeval``` package - more info [here](https://github.com/chakki-works/seqeval)
  - [ ] Fill out the readme to illustrate your results.
  
- *BONUS TASKS*:
  - [ ] It is quite normal to use more than one embedding at the same time (by concatenating them). Does this increase your performance?
  - [ ] Train an LSTM model trained for sentiment classification. Here you will need to modify the existing LSTM. 
    - A good idea is to start of by examining the documentation for the LSTM module. Here you can use the `load_sst2` function supplied to load some sentiment data. I have created a rough outline for how this would work in the `SentenceLSTM` in `LSTM.py`.


## Intended learning goals
- Learning to read, understand, and work with code made by other people
- Understand how to build an RNN using recurrent layers using ```pytorch```
- Experimenting with named entity recognition including the structure of its labels and how to train a model
- Conducting meaningful experiments to influence the performance of the model
- Implementing a simple version of early stopping and batch processing


## FAQ

<br /> 
<details>
  <summary> Pytest: How do I test the code and run the test suite?</summary>

The tests should run automatically with you push to Github. However, you can also run tests manually.

To run the test suite (pytests) you will need to install the required dependencies. This can be done using 


```
pip install -r requirements.txt
pip install pytest

python -m pytest
```

which will run all the test in the `tests` folder.

Specific tests can be run using:

```
python -m pytest path/to/test_script.py
```

**VS Code**
You can also run your test directly in VS Code. See the guide on the [pytest integration](https://code.visualstudio.com/docs/python/testing) here.

**Code Coverage**
If you want to check code coverage you can run the following:
```
pip install pytest-cov

python -m pytest --cov=.
```
</details>
<br /> 
