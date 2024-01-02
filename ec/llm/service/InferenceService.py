import os
from openai import OpenAI, RateLimitError
from time import sleep  #  función sleep para pausar la ejecución si se alcanza el límite

from ec.llm.utils.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT


class InferenceService:
    def __init__(self):
        api_key = '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'  # Reemplaza 'TU_CLAVE_DE_API_AQUI' con tu propia clave de API de OpenAI
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')

        # Inicializa el cliente de OpenAI pasando la clave de la API como argumento
        self.__openai_client = OpenAI(api_key=api_key)

        self.__prompt_template = 'Convert {number} to binary'

    def __inference(self, prompt):
        try:
            return CLEAN_TEXT(self.__openai_client.completions.create(
                model=self.__model,
                prompt=prompt,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            ).choices[0].text)
        except RateLimitError as e:
            print(f"Se alcanzó el límite de cuota: {e}")
            #  60 segundos antes de reintentar
            sleep(60)
            return self.__inference(prompt)  # Reintenta la solicitud después del tiempo de espera

   # def invoke(self, year: str) -> str:
    #    prompt = self.__prompt_template.format(year=year)
     #   return self.__inference(prompt)
#convierte  un numero naturala su representacion binaria a traves de la ia
    def convert_to_binary(self, number: int) -> str:
        prompt = self.__prompt_template.format(number=number)
        return self.__inference(prompt)