#Xml import 
from bs4 import BeautifulSoup
import os

#Datahandling
import pandas as pd
import numpy as np

### Tokenization 
import nltk
nltk.download('popular')
from nltk.tokenize import sent_tokenize, word_tokenize


def xml_loader(path):
    
    """
    - Add type hints on input and output
    - add function description
    - understand the pad and unk embeddings, add an argument which makes these optional. 
        E.g. add_padding = True and add_unknown = True
    """
    
    path = path
    files_in_folder = os.listdir(path)
    files_in_folder.remove('.DS_Store')

    # Making empty lists    

    rulings = []
    titles = []
    summaries = []

    for file in files_in_folder:
        
        # Loading one file from the folder
        
        with open(path + file, "r") as f:
            data_temp = f.read()
        
    # Making soup 
    soup = BeautifulSoup(data_temp, "xml")
    

    # Using find() to extract attributes of the first instance of the tag 
    
    title = soup.find('DOKTITEL')
    summary = soup.find('DOKRESUME')
    ruling_temp = soup.find('AFGR')
        
    # Finding children of N1 in 'Afgr' and taking the last one as this refers to the ruling 
    
    ruling = ruling_temp.findChildren('N1')[-1]
    
    #ruling = ruling_child.findChildren("TXT")[-1]
    
    # Appending text to lists
    
    rulings.append(ruling.text)
    titles.append(title.text)
    summaries.append(summary.text)
    
    
    
    df_ruling = pd.DataFrame(np.column_stack([rulings, text_id]),
                  columns =['Ruling', 'text_id'])
    
    # Removing specific ruling specifications manually
    
    string_remove = ['Thi kendes for ret', 'KendelseForkyndelse', 'Thi bestemmes', 'Thi kendes for ret', 'Kendelse']
    
    for string in string_remove:
        df_ruling = df_ruling.replace(string_remove, '')
        
    df_Title = pd.DataFrame(np.column_stack([titles, text_id]),
                    columns =['Title', 'text_id'])

    df_summary = pd.DataFrame(np.column_stack([summaries, text_id]),
                    columns =['Summary', 'text_id'])
    
    return df_ruling, df_Title, df_summary


def preperation_for_labelling(df, col_name):
    
    counter = 0
    paragraph_sent = []
    word_tok = []
    sent_id = []
    word_list = []
    
    for paragraph in df[col_name]:
        
    paragraph_sent = sent_tokenize(paragraph, language = 'danish')
    
    for sent in paragraph_sent:
        
        sentence.append(sent)
        
        word_tok = word_tokenize(sent, language = 'danish')
        
        counter+=1       

        for word in word_tok:
            word_list.append(word)
            sent_id.append(counter)

    df_ruling_words = pd.DataFrame(np.column_stack([word_list, sent_id]),
                  columns =['Word', 'sent_id'])
    
    return df_ruling_words
