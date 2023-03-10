
## The Tag, the Whole Tag, and Nothing but the Tag: Training and utilizing a Named-Entity Recognition model for Danish legal documents

This project contains the code used to preprocess documents of a custom Named Entity Recognition (NER) model for Danish legal documents. The project consists of two fine-tuned BERT models that classify relevant tokens into eight labels. These models were trained on a dataset of manually annotated legal documents from Karnov Group. The best-performing model achieved an accuracy of 84% (F-score).

In addition to training the model, we also examined how it could be used by legal professionals. We conducted a network analysis to assess document similarity and proposed implementations to increase document readability and optimize search algorithms. Our results suggest that this NER model has the potential to be a valuable tool for legal professionals when reviewing large amounts of legal documents.

Unfortunately the training data and final models cannot be made avaliable before further arrangements are made with Karnov Group due to an NDA.

# Performance

## xlm-roBERTa-large fine-tuned for NER legal text 

<img src="/ner/figure/xlmRobertLarge_results.png" width=60% height=60%>

## nb-bert fine-tuned for NER legal text 

<img src="/ner/figure/nb-bert_results.png" width=60% height=60%>

# Performance per epoch

## xlm-roBERTa-large fine-tuned for NER legal text 

```
Epochs Steps   LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
-----  ------  -------------  --------  ------  ------  ------  ------
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

## nb-bert fine-tuned for NER legal text 

```
Epochs Steps   LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
-----  ------  -------------  --------  ------  ------  ------  ------
  0       0         366.22    602.84    0.59    0.33    3.34    0.01
  6     200       84762.82  61860.50   76.27   75.42   77.14    0.76
 13     400        4594.51   6602.65   80.00   80.60   79.41    0.80
 19     600        2160.12   3074.67   79.25   79.09   79.41    0.79
 26     800        2499.17   2071.58   82.67   80.92   84.49    0.83
 32    1000        3593.82   1831.51   81.36   79.39   83.42    0.81
 39    1200        1527.32   1546.96   81.05   79.79   82.35    0.81
 46    1400         152.67   1430.36   81.20   79.34   83.16    0.81
 52    1600         115.33   1372.29   80.68   78.83   82.62    0.81
 59    1800         156.56   1379.78   82.46   80.77   84.22    0.82
 65    2000        2187.34   1433.32   81.57   79.80   83.42    0.82
```
## Project Organization
The organization of the project is as follows:

```
????????? LICENSE                    <- the license of this code
????????? README.md                  <- The top-level README for this project.
????????? .github            
???   ????????? workflows              <- workflows to automatically run when code is pushed
???   ???    ????????? run.sh        
????????? NER                        <- The main folder for scripts
    ????????? document_similarity    <- Functionf for Document Similarity implementation
    ????????? figure                 <- Folder containing figures    
    ????????? training   
    ???   ????????? config.cdf         <- The config file used for training
    ????????? preprocessing          <- Folder containing preprocessing scripts
        ????????? main.py            <- Main file for running XML preprocessing of legal documents
        ????????? xml_class.py       <- Class for processing XML files 
```

# LegalDoc Class

LegalDoc contains several methods for processing legal documents. The xml_loader method reads xml files from a specified path, extracts certain data from them, and stores the data in dataframes.

## __init__ 

The constructor for the LegalDoc class. It takes three arguments: path, language, add_padding, and add_unknown. path is the file path for a directory containing xml files, language is the language of the documents, and add_padding and add_unknown are optional boolean arguments with default values of False. The constructor initializes the class variables path, language, add_padding, and add_unknown with the provided values.

## xml_loader

A method that loads xml files from a specified directory, extracts the titles, summaries, and rulings from the files, and creates dataframes for each. It also removes specific ruling specifications from the rulings dataframe and concatenates the dataframes into a single dataframe. The method returns the resulting dataframe.

## preperation_for_labelling 

A method that takes a dataframe and a column name as arguments, tokenizes the sentences in the specified column, and returns a new dataframe with the sentence-tokenized texts. The method also writes the resulting dataframe to a CSV file.

# Document_similarity_function.py

The functions in this python file are used to extract named entity tags from a list of documents, create a network graph based on the similarity of the documents, and find the top 5 most similar documents for each document. The named entity tags are extracted using a specified natural language processing model, and the document similarity is calculated using cosine similarity and a TfidfVectorizer. The resulting data and graphs can be used for further analysis and visualization.

## extract_tags_todf

A function that takes a list of documents and a model name and returns a dataframe of named entity tags extracted from the documents using the specified model. The dataframe has columns for the entity text, label, and document id.

## create_network 

A function that takes a dataframe of named entity tags and a threshold value and creates a network graph where nodes represent documents and edges connect documents with a cosine similarity above the threshold. The function also writes the graph to a file in GEXF format.

## find_most_similar 

A function that takes a dataframe of named entity tags and returns a list of the top 5 most similar documents for each document, based on cosine similarity. The function first groups the dataframe by document id and converts the list of entity text values for each group into a list of strings. It then uses a TfidfVectorizer to compute the document-term matrix and uses cosine similarity to compute the pairwise similarities between the document vectors. Finally, it iterates over the documents, extracts the row of the similarity matrix corresponding to the current document, zips the row with the indices of the documents, and sorts the list by the similarity values. It then selects the top 5 documents with the highest similarity values.






