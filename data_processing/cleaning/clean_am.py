import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from database.database_manager import DatabaseManager

db_manager = DatabaseManager()

class AmharicDataCleaner:
    def __init__(self, data = None):
        self.data = data

    def normalize_char_level_missmatch(self, input_token):
        replacements = [
            # labialized characters
            (re.compile(r'(ሉ[ዋአ])'), 'ሏ'),
            (re.compile(r'(ሙ[ዋአ])'), 'ሟ'),
            (re.compile(r'(ቱ[ዋአ])'), 'ቷ'),
            (re.compile(r'(ሩ[ዋአ])'), 'ሯ'),
            (re.compile(r'(ሱ[ዋአ])'), 'ሷ'),
            (re.compile(r'(ሹ[ዋአ])'), 'ሿ'),
            (re.compile(r'(ቁ[ዋአ])'), 'ቋ'),
            (re.compile(r'(ቡ[ዋአ])'), 'ቧ'),
            (re.compile(r'(ቹ[ዋአ])'), 'ቿ'),
            (re.compile(r'(ሁ[ዋአ])'), 'ኋ'),
            (re.compile(r'(ኑ[ዋአ])'), 'ኗ'),
            (re.compile(r'(ኙ[ዋአ])'), 'ኟ'),
            (re.compile(r'(ኩ[ዋአ])'), 'ኳ'),
            (re.compile(r'(ዙ[ዋአ])'), 'ዟ'),
            (re.compile(r'(ጉ[ዋአ])'), 'ጓ'),
            (re.compile(r'(ደ[ዋአ])'), 'ዷ'),
            (re.compile(r'(ጡ[ዋአ])'), 'ጧ'),
            (re.compile(r'(ጩ[ዋአ])'), 'ጯ'),
            (re.compile(r'(ጹ[ዋአ])'), 'ጿ'),
            (re.compile(r'(ፉ[ዋአ])'), 'ፏ'),
            # other characters
            (re.compile(r'[ሃኅኃሐሓኻ]'), 'ሀ'),
            (re.compile(r'[ሑኁዅ]'), 'ሁ'),
            (re.compile(r'[ኂሒኺ]'), 'ሂ'),
            (re.compile(r'[ሔዄ]'), 'ሄ'),
            (re.compile(r'[ሕኅ]'), 'ህ'),
            (re.compile(r'[ኆሖኾ]'), 'ሆ'),
            (re.compile(r'[ሠ]'), 'ሰ'),
            (re.compile(r'[ሡ]'), 'ሱ'),
            (re.compile(r'[ሢ]'), 'ሲ'),
            (re.compile(r'[ሣ]'), 'ሳ'),
            (re.compile(r'[ሤ]'), 'ሴ'),
            (re.compile(r'[ሥ]'), 'ስ'),
            (re.compile(r'[ሦ]'), 'ሶ'),
            (re.compile(r'[ዓኣዐ]'), 'አ'),
            (re.compile(r'[ዑ]'), 'ኡ'),
            (re.compile(r'[ዒ]'), 'ኢ'),
            (re.compile(r'[ዔ]'), 'ኤ'),
            (re.compile(r'[ዕ]'), 'እ'),
            (re.compile(r'[ዖ]'), 'ኦ'),
            (re.compile(r'[ጸ]'), 'ፀ'),
            (re.compile(r'[ጹ]'), 'ፁ'),
            (re.compile(r'[ጺ]'), 'ፂ'),
            (re.compile(r'[ጻ]'), 'ፃ'),
            (re.compile(r'[ጼ]'), 'ፄ'),
            (re.compile(r'[ጽ]'), 'ፅ'),
            (re.compile(r'[ጾ]'), 'ፆ'),
            # standardize ቊ and ኵ
            (re.compile(r'[ቊ]'), 'ቁ'),
            (re.compile(r'[ኵ]'), 'ኩ'),
        ]
        for pattern, replacement in replacements:
            input_token = pattern.sub(replacement, input_token)
        return input_token
    
    def remove_punc_and_special_chars(self, text):
        if text is None:
            raise ValueError("Input text cannot be None")
        try:
            normalized_text = re.sub('[\!\@\#\$\%\^\«\_\°\é\»\&\*\(\)\…\[\]\{\}\;\“\”\›\’\‘\"\'\:\,\.\‹\/\<\>\?\\\\|\`\´\~\-\=\+\፡\።\፤\;\፦\፥\፧\፨\፠\፣]', '',text)
            return normalized_text
        except Exception as e:
            raise ValueError(
                "An error occurred while removing punctuation and special characters from the input text. Exception: {}".format(e)) from e
    
    def remove_ascii_and_numbers(self, text_input):
        if text_input is None:
            raise ValueError("Input text cannot be None")
        try:
            rm_num_and_ascii = re.sub('[A-Za-z0-9]', '', text_input)
            return re.sub('[\'\u1369-\u137C\']+', '', rm_num_and_ascii)
        except Exception as e:
            raise ValueError(
                "An error occurred while removing ASCII characters and numbers from the input text. Exception: {}".format(e)) from e

    def remove_newline_and_extra_space(self, text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def remove_emojis(self, text):
        # Define a regular expression pattern to match emojis
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # Emojis
                                u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # Transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # Flags (iOS)
                                u"\U00002500-\U00002BEF"  # Chinese characters
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # Combining enclosing keycap
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        
        # Remove emojis from the text
        clean_text = emoji_pattern.sub('', text)
        
        return clean_text

    

async def clean_and_insert_data():
    cleaner = AmharicDataCleaner()

    raw_data = await db_manager.get_raw_text_data()  

    # Clean and insert data
    for data in raw_data:
        cleaned_data = cleaner.normalize_char_level_missmatch(data[1])
        cleaned_data = cleaner.remove_punc_and_special_chars(cleaned_data)
        cleaned_data = cleaner.remove_ascii_and_numbers(cleaned_data)
        cleaned_data = cleaner.remove_newline_and_extra_space(cleaned_data)
        cleaned_data = cleaner.remove_emojis(cleaned_data)

        await db_manager.insert_cleaned_text_data(data[0], cleaned_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(clean_and_insert_data())