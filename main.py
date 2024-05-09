import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request

app = Flask(__name__)

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    # Informações do formulário HTML
    remetente = request.form['remetente']
    destinatario = request.form['email']
    mensagem = request.form['mensagem']

    # Configuração do servidor SMTP
    servidor_smtp = "smtp.gmail.com"
    porta = 587
    usuario = "raffa.alves.souza@gmail.com"  # Substitua pelo seu e-mail
    senha = "Dark2305#"  # Substitua pela sua senha

    # Criando a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Assunto do E-mail"
    corpo = mensagem
    msg.attach(MIMEText(corpo, 'plain'))

    # Enviando o e-mail
    try:
        server = smtplib.SMTP(servidor_smtp, porta)
        server.starttls()
        server.login(usuario, senha)
        texto_email = msg.as_string()
        server.sendmail(remetente, destinatario, texto_email)
        server.quit()
        return 'E-mail enviado com sucesso!'
    except Exception as e:
        return f"Erro ao enviar e-mail: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
