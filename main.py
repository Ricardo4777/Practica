from dotenv import load_dotenv
import re

import os

from ec.llm.service.InferenceService import InferenceService
from ec.llm.utils.const import CLEAN_TEXT

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    print(os.getenv('OPENAI_API_KEY'))
    # custom_dict = {'a': 'b'}
    # print(custom_dict['c'])
    # print(custom_dict.get('c', 'kepler'))

    print(InferenceService().convert_to_binary('1200'))