from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        mensagem = request.form['mensagem']
        enviar_email(email, mensagem)
        return 'Mensagem enviada com sucesso!'
    return render_template('index.html')

def enviar_email(email, mensagem):
    remetente = 'raffa.alves.souza@gmail.com'
    destinatario = 'raffa.alves.souza@gmail.com'
    assunto = 'Nova mensagem do site'
    corpo_email = f'E-mail: {email}\nMensagem: {mensagem}'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, 'Dark2305#')
        server.sendmail(remetente, destinatario, corpo_email)
        server.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

if __name__ == '__main__':
    app.run(debug=True)
