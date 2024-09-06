# -*- coding: utf-8 -*-
"""
  Script para envio de mensagens em massa.
  Autor: Vanessa Stangherlin
  Objetivo: Enviar mensagens para uma lista de contatos.
  O script espera um numero de minutos entre cada mensagem, 
  especificado no arquivo de configuração.  
"""
import os
import time

import pandas as pd
import pywhatkit as kit
import typer

import config


def main(tag_pessoas: str, tag_mensagem: str):
    if os.path.exists(f"{config.DATA_FOLDER}/{config.DATA_FILE}"):
        lista_pessoas = pd.read_excel(
            f"{config.DATA_FOLDER}/{config.DATA_FILE}",
            sheet_name="pessoas",
            dtype=str,
            engine="openpyxl",
        )
        pessoas = lista_pessoas[
            lista_pessoas["tag"].str.contains(tag_pessoas, case=False)
        ]

        if len(pessoas) == 0:
            print("Nenhuma pessoa encontrada.")
            return 1

        lista_mensagens = pd.read_excel(
            f"{config.DATA_FOLDER}/{config.DATA_FILE}",
            sheet_name="mensagens",
            dtype=str,
            engine="openpyxl",
        )
        mensagens = lista_mensagens[
            lista_mensagens["tag"].str.contains(tag_mensagem, case=False)
        ]

        if len(mensagens) == 0:
            print("Nenhuma mensagem encontrada.")
            return 1

        for _, mensagem in mensagens.iterrows():
            for _, pessoa in pessoas.iterrows():
                print(f"Enviando mensagem para {pessoa['nome']}...")
                kit.sendwhatmsg(
                    pessoa["numero"],
                    mensagem["mensagem"].format(pessoa["nome"]),
                    time.localtime().tm_hour,
                    time.localtime().tm_min + config.MSG_INTERVAL,
                )
                # time.sleep(config.MSG_INTERVAL * 60)
        return 0
    else:
        print(f"Arquivo {config.DATA_FILE} não encontrado.")
        return 1


if __name__ == "__main__":
    typer.run(main)
