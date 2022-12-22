import argparse
from xml_class import LegalDoc

def parse_args():
    # Create an argument parser object
    parser = argparse.ArgumentParser(description='Process legal documents.')

    # Add arguments
    parser.add_argument('path', type=str, help='Path to folder containing xml files.')
    parser.add_argument('language', type=str, help='Language of the documents (e.g. Danish, English).')
    parser.add_argument('--padding', action='store_true', help='Add padding to data.')
    parser.add_argument('--unknown', action='store_true', help='Add unknown tokens to data.')

    # Parse arguments
    return parser.parse_args()

def create_processor(args):
    # Create an instance of the LegalDoc class
    return LegalDoc(path=args.path, language=args.language, add_padding=args.padding, add_unknown=args.unknown)

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_args()

    # Create a processor object
    processor = create_processor(args)

    # Load xml files and extract data
    df = processor.xml_loader()

    # Process data
    df_sentences = processor.preperation_for_labelling(df, 'text')