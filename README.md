
## The Tag, the Whole Tag, and Nothing but the Tag”: Fine-tuning and utilizing a pre-trained BERT model for (Fine-Grained) Name Entity Recognition in Danish legal documents


*Include a short description of which models you have tried and conclusions from comparing these models. This should be no longer than an abstract. This section can also include questions regarding the assignment.* 

# Performance
![xlm-Roberta-Large-Fine-tune](/ner/figure/xlmRobertLarge_results.png)

# Performance per epoch

```
Epoch Steps   LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
----  ------  -------------  --------  ------  ------  ------  ------
  0       0         930.71    580.89    0.02    0.01    0.13    0.00
  6     200       59137.80  60075.65   75.45   74.71   76.20    0.75
 13     400        5045.91   6005.56   81.79   82.85   80.75    0.82
 19     600        1313.73   2661.95   82.09   81.18   83.02    0.82
 26     800         730.59   1810.62   81.88   80.15   83.69    0.82
 32    1000         393.56   1445.48   83.11   81.15   85.16    0.83
 39    1200         316.62   1301.49   81.36   81.31   81.42    0.81
 46    1400         244.48   1205.96   81.29   81.56   81.02    0.81
 52    1600         180.75   1112.71   82.60   82.06   83.16    0.83
 59    1800         247.30   1129.31   82.53   82.31   82.75    0.83
 65    2000         160.00   1072.10   83.82   82.51   85.16    0.84
```
## Project Organization
The organization of the project is as follows:

```
├── LICENSE                    <- the license of this code
├── README.md                  <- The top-level README for this project.
├── .github            
│   └── workflows              <- workflows to automatically run when code is pushed
│   │    └── run.sh        
├── NER                        <- The main folder for scripts
│   ├── tests                  
│   │   └── ...
|   └── ...
├── .gitignore                 <- A list of files not uploaded to git
└── requirement.txt            <- A requirements file of the required packages.
```

## LegalDoc Class

This is a class called LegalDoc that contains several methods for processing legal documents. The xml_loader method reads xml files from a specified path, extracts certain data from them, and stores the data in dataframes. The preperation_for_labelling method takes a dataframe and a column name as input, tokenizes the sentences in the specified column, and returns a new dataframe with the sentence-tokenized texts.

Here is a brief overview of the methods and their inputs and outputs:

- xml_loader:

Input: a path to a folder containing xml files, a language string, and optional boolean values for adding padding and unknown tokens.
Output: a dataframe containing the extracted data.

- preperation_for_labelling:

Input: a dataframe and a column name.
Output: a new dataframe with the sentence-tokenized texts.

## parse_args()
The parse_args() function is used to parse command-line arguments passed to the script when it is executed. It does this using the argparse module, which is a standard Python library for parsing command-line arguments.

The function creates an argument parser object using the argparse.ArgumentParser() constructor, and specifies a description for the script. The add_argument() method is then used to add arguments to the parser. In this case, the script has three arguments:

path, a required string argument specifying the path to the folder containing the xml files.
language, a required string argument specifying the language of the documents.
padding, an optional boolean argument that adds padding to the data if specified.
unknown, an optional boolean argument that adds unknown tokens to the data if specified.
The parse_args() function returns the parsed arguments using the parse_args() method of the argument parser object.

## create_processor(args)
The create_processor() function is used to create an instance of the LegalDoc class. It takes a single argument, args, which is a namespace object containing the parsed command-line arguments.

The function creates an instance of the LegalDoc class using the LegalDoc() constructor, and passes in the values of the path, language, padding, and unknown arguments as keyword arguments. The function then returns the created instance of the LegalDoc class.







