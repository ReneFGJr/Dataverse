pip install python-dotenv

Arquivo .env

# ===========================
# Configuração SMTP Office365
# ===========================

SMTP_SERVER=smtp.office365.com
SMTP_PORT=587

SMTP_USERNAME=datarepository@ipen.br
SMTP_PASSWORD=SUA_SENHA_AQUI

# E-mail remetente
FROM_EMAIL=datarepository@ipen.br

# Destinatário do teste
TO_EMAIL=seuemail@exemplo.com

# Mensagem
SUBJECT=Teste SMTP Python
BODY=Este é um teste de envio realizado via Python.
