from  flet import Page,TextField,ElevatedButton,app,Text
# Page: é usando para criar e configurar a aparencia da pagina, na verdade do projeto
# é nela que trabalhamos as routes de novas telas.
#TextField: Campo de entrada de Texto, no qual entramos com dados, podemos configurar diferentes paramentros de entrada
#ElevatedButton, que nada mais é que um botão

def main(pagina:Page):
    # esse parametro vai ter tudo que uma Page faz e tem
    pagina.title="Segunda Tela"
    # usando o window_max, quer dizer que você so pode abrir ate essa medida
    pagina.window_max_width=600
    pagina.window_max_height=700
    # essa é a largura real dela
    pagina.window_width=600
    pagina.window_height=700
    # Definindo o tamanho minimo
    pagina.window_min_width=400
    pagina.window_min_height=550
# posso carregar o meu projeto no centro da tela
    pagina.window_center()
    pagina.bgcolor="#FFFAF0"
    #Colocando elementos na tela
    # vai me pertimir pegar dados da tela
    t_field_nome=TextField(label="Digite o seu nome")
    t_field_salario=TextField(label="Salario")
    # o text é o texto que aparece dentro do botão
    btn_calcular=ElevatedButton(text="Calcular")
    def calculando(e):
        # eu posso pegar o valor de dentro do TextField usando o atributo value
        txt_resposta.value=f"Nome: {t_field_nome.value} tem o salario R$ {t_field_salario.value}"
       # Limpando os campos ja digitados
        t_field_nome.value=""
        t_field_nome.update()
        t_field_salario.value=""
        t_field_salario.update()
        txt_resposta.update()


    # todo evento é construido dentro de uma função
    btn_calcular.on_click=calculando

    # o value vai ser o valor inicial do nosso texto
    # o size vai modificar o tamanho do texto
    txt_resposta=Text(value="Resposta",size=30)

    # estou usando o add para adicionar elementos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()

# ela carrega a nossa pagina, ou no nosso projeto
# ela é resposavel de determinar se vai ser uma aplicação local ou web
app(target=main)