import re

class AmharicDataCleaner:
    def __init__(self, data = None):
        self.data = data

    def normalize_char_level_missmatch(self, input_token):
        replacements = [
            (re.compile(r'(ሉ[ዋአ])'), 'ሏ'),
        ]
        for pattern, replacement in replacements:
            input_token = pattern.sub(replacement, input_token)
        return input_token
    
    def remove_punc_and_special_chars(self, text):
        if text is None:
            raise ValueError("Input text cannot be None")
        try:
            normalized_text = re.sub('[\!\@\#\$\%\^\«\»\&\*\(\)\…\[\]\{\}\;\“\”\›\’\‘\"\'\:\,\.\‹\/\<\>\?\\\\|\`\´\~\-\=\+\፡\።\፤\;\፦\፥\፧\፨\፠\፣]', '',text)
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

