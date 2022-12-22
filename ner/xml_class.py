import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


### Tokenization 
import nltk
nltk.download('popular')
from nltk.tokenize import sent_tokenize, word_tokenize


class LegalDoc:
    def __init__(self, path: str, language: str, add_padding: bool = False, add_unknown: bool = False):
        self.path = path
        self.language = language
        self.add_padding = add_padding
        self.add_unknown = add_unknown

    def xml_loader(self):
        """
        Loads xml files from the specified path and creates dataframes for the titles, summaries, and rulings. 
        Removes specific ruling specifications manually.
        """
        files_in_folder = os.listdir(self.path)
        files_in_folder.remove('.DS_Store')

        # Making empty lists    
        rulings = []
        titles = []
        summaries = []
        text_id = []
        
        for file in files_in_folder:
            # Loading one file from the folder
            with open(self.path + file, "r") as f:
                data_temp = f.read()

            # Making soup 
            soup = BeautifulSoup(data_temp, "xml")

            # Using find() to extract attributes of the first instance of the tag 
            title = soup.find('DOKTITEL')
            summary = soup.find('DOKRESUME')
            ruling_temp = soup.find('AFGR')

            # Finding children of N1 in 'Afgr' and taking the last one as this refers to the ruling 
            ruling = ruling_temp.findChildren('N1')[-1]

            # Appending text to lists
            rulings.append(ruling.text)
            titles.append(title.text)
            summaries.append(summary.text)

            #Creating text id
            text_id.append(file)

        # Creating dataframes
        df_ruling = pd.DataFrame(np.column_stack([rulings, text_id]),
                            columns =['text', 'text_id'])

        df_Title = pd.DataFrame(np.column_stack([titles, text_id]),
                            columns =['text', 'text_id'])

        df_summary = pd.DataFrame(np.column_stack([summaries, text_id]),
                            columns =['text', 'text_id'])

        # Removing specific ruling specifications manually
        string_remove = ['Thi kendes for ret', 'KendelseForkyndelse', 'Thi bestemmes', 'Thi kendes for ret', 'Kendelse',
                        'Landsrettens begrundelse og resultat', 'Rettens begrundelse og resultat', ]

        for string in string_remove:
            df_ruling['text'] = df_ruling['text'].str.replace(string, ' ')

        # Concatenating the dataframes
        df = pd.concat([df_ruling, df_Title, df_summary], ignore_index=True)

        return df
    
    def preperation_for_labelling(self, df, col_name: str):
        """
        Tokenizes the sentences in the specified column of the dataframe and returns a new dataframe with the sentence-tokenized texts.
        """
        paragraph_sent = []
        sentence_list = []

        for paragraph in df[col_name]:
            paragraph_sent = sent_tokenize(paragraph, language = self.language)

            for sent in paragraph_sent:
                sentence_list.append(sent)

        df_sentences = pd.DataFrame(np.column_stack([sentence_list]),
                    columns =[col_name])
        
        pd.DataFrame.to_csv(df_sentences, "df_ruling_words_test.csv", index = False)

        return df_sentences