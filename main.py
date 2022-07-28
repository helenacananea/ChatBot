#!/usr/bin/env python3
# coding=utf-8
import asyncio
import os
import sys
import time
import re
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Session name, API ID and hash to use; loaded from environmental variables
load_dotenv()
TG_API_BOT_TOKEN = os.environ.get('TG_API_BOT_TOKEN')
TG_API_ID = int(os.environ.get('TG_API_ID', '0'))
TG_API_HASH = os.environ.get('TG_API_HASH')

options_menu: str = '' \
                    'Olá! Sou a Luna, a Assistente Virtual da Autoridade ' \
                    'Nacional de Proteção de Dados (ANPD). ' \
                    'Apenas os serviços listados abaixo estão disponíveis. ' \
                    'Aos poucos, outros serviços serão incluídos. Para navegar em ' \
                    'nosso conteúdo, DIGITE O NÚMERO do tópico. \n\r' \
                    '1 O que trata a LGPD? \n\r'\
                    '2 O que são dados pessoais e dados pessoais sensíveis? \n\r' \
                    '3 Quais dados são protegidos pela LGPD? \n\r' \
                    '4 O que é a Autoridade Nacional de Proteção de Dados Pessoais - ANPD? \n\r' \
                    '5 Quando a LGPD entrou em vigor? \n\r' \
                    '6 Quer seguir nosso Instagram? \n\r' \
                    '7 Quer saber qual a nossa página do gov.br? \n\r' \
                    '8 Deseja ver nosso canal  do Youtube? \n\r' \
                    '9 Gostaria de seguir nosso LinkedIn? \n\r' \
                    '10	Almeja falar com a Ouvidoria do ANPD? \n\r' \
                    '11 Tem mais dúvidas? Veja nesse espaço as perguntas mais frequentes! \n\r' \
                    'Os dados serão protegidos pela Lei Geral de Proteção de Dados (Lei 13.709/2018) \n\r' \
                    'Agradecemos o contato. Estamos encerrando o atendimento!'

bot = TelegramClient("bot", api_id=TG_API_ID, api_hash=TG_API_HASH).start(bot_token=TG_API_BOT_TOKEN)


def process_message_multi(message):
    """
        Process messages commands
        :param message:
        :return: Response message
        """
    msg = str(message).lower()
    response = 0

    # Opções
    if re.search(r'\b1\b', msg):
        message_response = "A Lei Geral de Proteção de Dados Pessoais (Lei n. 13.709, de 2018) " \
                           "dispõe sobre o tratamento de dados pessoais das pessoas naturais, " \
                           "definindo as hipóteses em que tais dados podem legitimamente ser utilizados por " \
                           "terceiros e estabelecendo mecanismos para proteger os titulares dos dados contra " \
                           "usos inadequados. A Lei é aplicável ao tratamento de dados realizado por pessoas naturais" \
                           ", bem como por pessoas jurídicas de direito público ou privado. Possui, conforme o " \
                           "art.1º, o objetivo de proteger os direitos fundamentais de liberdade e de privacidade, " \
                           "assim como o livre desenvolvimento da personalidade da pessoa natural."

    elif re.search(r'\b2\b', msg):
        message_response = "A LGPD, no art. 5º, inciso I, define dado pessoal como" \
                           "a informação relacionada a uma pessoa natural identificada ou identificável. Segundo o " \
                           "art. 12, § 2º, da LGPD, poderão ser igualmente considerados como dados pessoais aqueles " \
                           "utilizados para formação do perfil comportamental de determinada pessoa natural, caso " \
                           "identificada. \n\r" \
                           " \n\r" \
                           "São dados pessoais sensíveis aqueles aos quais a LGPD conferiu uma proteção ainda maior" \
                           ", por estarem diretamente relacionados aos aspectos mais íntimos da personalidade de " \
                           "um indivíduo. De acordo com o art. 5º, II, são aqueles relativos à origem racial ou " \
                           "étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de " \
                           "caráter religioso, filosófico ou político, dados referentes à saúde ou à vida sexual," \
                           "dados genéticos ou biométricos, quando vinculados a uma pessoa natural. "

    elif re.search(r'\b3\b', msg):
        message_response = " É garantida proteção a todos os dados cujos titulares são pessoas naturais, estejam " \
                           "eles em formato físico ou digital.  Assim, a LGPD não alcança os dados titularizados por " \
                           "pessoas jurídicas."

    elif re.search(r'\b4\b', msg):
        message_response = "A ANPD é o órgão da administração pública federal responsável por zelar pela proteção de " \
                           "dados pessoais e por regulamentar, implementar e fiscalizar o cumprimento da LGPD no " \
                           "Brasil."

    elif re.search(r'\b5\b', msg):
          message_response = "A Lei entrou em vigor de maneira escalonada: \n\r " \
                              "•	Em 28 de dezembro de 2018, quanto aos arts. 55-A, 55-B, 55-C, 55-D, 55-E, 55-F, " \
                              "55-G, 55-H, 55-I, 55-J, 55-K, 55-L, 58-A e 58-B, que tratam sobre a constituição da " \
                              "Autoridade Nacional de Proteção de Dados – ANPD e do Conselho Nacional de Proteção " \
                              "de Dados Pessoais e da Privacidade – CNPD; \n\r" \
                              "•	Em 18 de setembro de 2020, quanto aos demais artigos da Lei, com exceção dos " \
                              "dispositivos que tratam da aplicação de sanções administrativas; e \n\r" \
                              "•	Em 1º de agosto de 2021, quanto aos arts. 52, 53 e 54, que tratam das sanções " \
                             "administrativas."

    elif re.search(r'\b6\b', msg):
          message_response = " https://www.instagram.com/anpdgov/"


    elif re.search(r'\b7\b', msg):
          message_response = "https://www.gov.br/anpd/pt-br"

    elif re.search(r'\b8\b', msg):
        message_response = " https://www.youtube.com/channel/UCDqacQvXpk4VU9MEOvPTekg"

    elif re.search(r'\b9\b', msg):
         message_response = "https://www.linkedin.com/company/anpdgov/"

    elif re.search(r'\b10\b', msg):
        message_response = "https://falabr.cgu.gov.br/publico/Manifestacao/SelecionarTipoManifestacao.aspx?ReturnUrl=%2f"

    elif re.search(r'\b11\b', msg):
        message_response = "https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes-2013-anpd"


    else:
        message_response = options_menu

    if response != 0:
        message_response = f"Fail send broker command!!! Error: {response}"

    return message_response


@bot.on(events.NewMessage(pattern='/id'))
async def start(event):
    await event.reply(f'Id: {event.chat_id}')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/?'))
async def start(event):
    """Send a message when the command /start is issued."""
    print(event.chat_id)
    print(event.message.text)
    response = process_message_multi(str(event.message.text))

    if response != "":
        await event.reply(response)
    raise events.StopPropagation


@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    #await event.respond("Invalid command")
    print(event.chat_id)
    print(event.message.text)
    response = process_message_multi(str(event.message.text))

    if response != "":
        await event.reply(response)
    raise events.StopPropagation


def main():
    """Start the bot."""
    print("Executando chatbot ANPD")
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()
