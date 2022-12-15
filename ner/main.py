from src.preprocessing import xml_loader, preperation_for_labelling

def main(path):

    df_ruling, df_Title, df_summary = xml_loader(path)
    
    df_ruling_words  = preperation_for_labelling(df_ruling, 'Ruling')
    df_title_words  = preperation_for_labelling(df_Title, 'Title')
    df_summary_words  = preperation_for_labelling(df_summary, 'Summary')
    
    
if __name__=="__main__":
    main(path="dommedump/")