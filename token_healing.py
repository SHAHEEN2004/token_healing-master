import logging
from autocorrect import Speller

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def heal_tokens(tokens):
    spell = Speller(lang='en')

    healed_tokens = []
    for token in tokens:
        # Check if the token is misspelled
        if token != spell(token):
            # Get the most likely correct spelling
            corrected = spell(token)
            healed_tokens.append(corrected)
        else:
            healed_tokens.append(token)

    return healed_tokens


def heal_tokens_in_file(input_file, output_file):
    try:
        logger.info(f"Reading input file: {input_file}")
        with open(input_file, 'r') as file:
            tokens = file.read().split()

        logger.info("Performing token healing...")
        healed_tokens = heal_tokens(tokens)

        logger.info(f"Writing output file: {output_file}")
        with open(output_file, 'w') as file:
            file.write(' '.join(healed_tokens))

        logger.info("Token healing completed successfully.")

    except IOError as e:
        logger.error(f"An error occurred while processing the files: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
heal_tokens_in_file(input_file, output_file)