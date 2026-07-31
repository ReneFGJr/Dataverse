#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import ssl
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

# --------------------------------------------------------
# Carrega configurações
# --------------------------------------------------------

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

SUBJECT = os.getenv("SUBJECT")
BODY = os.getenv("BODY")


def testar_smtp():

    print("=" * 70)
    print("TESTE DE ENVIO SMTP")
    print("=" * 70)

    print(f"Servidor : {SMTP_SERVER}")
    print(f"Porta     : {SMTP_PORT}")
    print(f"Usuário   : {SMTP_USERNAME}")
    print(f"Destino   : {TO_EMAIL}")
    print("=" * 70)

    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg.set_content(BODY)

    try:

        print("\nConectando ao servidor...\n")

        smtp = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
            timeout=60
        )

        # ----------------------------------------------------
        # MOSTRA TODA A CONVERSA SMTP
        # ----------------------------------------------------
        smtp.set_debuglevel(1)

        print("\n>>> EHLO")
        smtp.ehlo()

        print("\n>>> STARTTLS")
        context = ssl.create_default_context()
        smtp.starttls(context=context)

        print("\n>>> EHLO (após TLS)")
        smtp.ehlo()

        print("\n>>> LOGIN")
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

        print("\n>>> SENDMAIL")
        smtp.send_message(msg)

        print("\n")
        print("=" * 70)
        print("EMAIL ENVIADO COM SUCESSO!")
        print("=" * 70)

        smtp.quit()

    except Exception as e:

        print("\n")
        print("=" * 70)
        print("ERRO DURANTE O ENVIO")
        print("=" * 70)
        print(type(e).__name__)
        print(e)
        print("=" * 70)


if __name__ == "__main__":
    testar_smtp()