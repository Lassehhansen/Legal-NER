
## The Tag, the Whole Tag, and Nothing but the Tag”: Fine-tuning and utilizing a pre-trained BERT model for (Fine-Grained) Name Entity Recognition in Danish legal documents


*Include a short description of which models you have tried and conclusions from comparing these models. This should be no longer than an abstract. This section can also include questions regarding the assignment.* 

# Performance
*This should include a table of performance metrics of different models. The performance metrics should at least include accuracy and F1-score.*

## Project Organization
The organization of the project is as follows:

*Correct this to reflect any changes you make*

```
├── LICENSE                    <- the license of this code
├── README.md                  <- The top-level README for this project.
├── .github            
│   └── workflows              <- workflows to automatically run when code is pushed
│   │    └── pytest.yml        <- A workflow which runs pytests upon push
├── classification             <- The main folder for scripts
│   ├── tests                  <- The pytest test suite
│   │   └── ...
|   └── ...
├── .gitignore                 <- A list of files not uploaded to git
├── requirement.txt            <- A requirements file of the required packages.
└── assignment_description.md  <- the assignment description
```

## LegalDoc Class

This is a class called LegalDoc that contains several methods for processing legal documents. The xml_loader method reads xml files from a specified path, extracts certain data from them, and stores the data in dataframes. The preperation_for_labelling method takes a dataframe and a column name as input, tokenizes the sentences in the specified column, and returns a new dataframe with the sentence-tokenized texts.

Here is a brief overview of the methods and their inputs and outputs:

 -xml_loader:

Input: a path to a folder containing xml files, a language string, and optional boolean values for adding padding and unknown tokens.
Output: a dataframe containing the extracted data.

- preperation_for_labelling:

Input: a dataframe and a column name.
Output: a new dataframe with the sentence-tokenized texts.







