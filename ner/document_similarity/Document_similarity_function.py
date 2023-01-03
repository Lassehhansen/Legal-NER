import pandas as pd
import networkx as nx
import spacy
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_tags_todf(documents, model: str):
    # Initialize an empty list to store the entities
    ents_list = []
    nlp = spacy.load(model)

    # Iterate over the documents
    for doc_id, doc in enumerate(documents):
        # Perform NER inference on the document
        doc = nlp(doc)

        # Extract the entities from the doc
        ents = [(ent.text, ent.label_) for ent in doc.ents]

        # Add the document id to each entity
        ents = [(text, label, doc_id) for text, label in ents]

        # Add the entities to the list
        ents_list.extend(ents)

    # Create a dataframe from the entities, with columns for the entity text, label, and document id
    df = pd.DataFrame(ents_list, columns=['Entity Text', 'Entity Label', 'Doc ID'])

    return df

def create_network(df, threshold):
    # Filter the dataframe to include only rows with the 'NRM' label
    #df_filtered = df[df['Entity Label'] == 'NRM']

    # Group the filtered dataframe by the 'Doc ID' column and extract a list of the 'Entity Text' values for each group
    documents = df.groupby('Doc ID')['Entity Text'].apply(list).tolist()

    # Convert the list of lists into a list of strings
    documents = [' '.join(doc) for doc in documents]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Use the TfidfVectorizer to compute the document-term matrix
    doc_term_matrix = vectorizer.fit_transform(documents)

    # Compute the pairwise cosine similarities between the document vectors
    similarities = cosine_similarity(doc_term_matrix)

    # Create a graph object
    G = nx.Graph()

    # Add nodes to the graph for each document
    for i, doc in enumerate(documents):
        G.add_node(i)

    # Only add edges between nodes with a similarity above the threshold
    for i in range(len(similarities)):
        for j in range(i+1, len(similarities[i])):
            if similarities[i][j] >= threshold:
                G.add_edge(i, j, weight=similarities[i][j])

    # pos = nx.spring_layout(G)

    # Draw the graph
    # fig, ax = plt.subplots(figsize=(20, 10))
    # nx.draw_networkx(G, ax=ax)
    # plt.show()

    # Writing to gexf format to import into Gephi
    nx.write_gexf(G, 'network_3threshold.gexf')

def find_most_similar(df):
    
    documents = df.groupby('Doc ID')['Entity Text'].apply(list).tolist()

    # Convert the list of lists into a list of strings
    documents = [' '.join(doc) for doc in documents]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Use the TfidfVectorizer to compute the document-term matrix
    doc_term_matrix = vectorizer.fit_transform(documents)

    # Compute the pairwise cosine similarities between the document vectors
    similarities = cosine_similarity(doc_term_matrix)
    
    # Initialize an empty list to store the top 5 most similar documents for each document
    most_similar_docs = []

    # Iterate over the documents
    for i, doc in enumerate(documents):
        # Extract the row of the similarity matrix corresponding to the current document
        row = similarities[i, :]

        # Zip the row with the indices of the documents and sort the list by the similarity values
        most_similar = sorted(zip(row, range(len(documents))), key=lambda x: x[0], reverse=True)

        # Exclude the first element (which corresponds to the similarity of the current document to itself)
        most_similar = most_similar[1:]

        # Extract the top 5 documents with the highest similarity values
        top_k = most_similar[:5]

        # Append the top 5 most similar documents to the list
        most_similar_docs.append(top_k)

    return most_similar_docs

def main():
    legal_df2 = pd.read_csv('df_for_implementation.csv')
    legal_docs = legal_df2['text']
    df = extract_tags_todf(legal_docs, 'da_core_news_sm')
    create_network(df, 0.3)
    most_similar_docs = find_most_similar(df)

if __name__ == '__main__':
    main()