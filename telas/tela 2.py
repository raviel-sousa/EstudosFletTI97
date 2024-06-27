from flet import Page,TextField,Text,ElevatedButton,app
                    #Page - é usado para criar  configurar a aprenca da página, ou seja ou do projeto
                    #é nela que trabalha,ps as routes (rotas) de novas telas.

                    #TextField - Campo de entrada de Texto, no qual entramos com dados, podemos configurar diferentes parametros de etrada

                    #ElevatedButton - botão

                    #app -  essa função carrega a nossa página ou projeto
                    #ela é responsável por determinar se vai ser uma aplicação local ou web

def main (pagina:Page):
    #esse parametro vai ter tudo que uma Page faz e tem
    pagina.title="Segunda Tela"

        # largura das páginas máxima que a pessoa pode abrir
    pagina.window_max_width=600
    pagina.window_max_height=700

        # essa é a largura real da tela
    pagina.window_width = 600
    pagina.window_height = 700

        #definindo tamanho minimo
    pagina.window_min_width=400
    pagina.window_min_height=550

        #posso carregar o prjeto no centro da tela
    pagina.window_center()
        #cor de fundo da pagina
    pagina.bgcolor="#732F35"
    pagina.window_opacity=20



    #Colocando elementos na tela
    t_field_nome=TextField(label="Digite o seu nome")
    t_field_salario=TextField(label="Salario")

    #o text é o texto que aparece dentro do botão
    btn_calcular=ElevatedButton(text="Calcular")

    # criei um evento para o botão - ao clicar ele vai fazer...
    # todo evento é construindo dentro de uma função
    def calculando(e):
        print(t_field_nome.value)
        print(t_field_salario)
        txt_resposta.value=f"Nome: {t_field_nome.value} tem o salario R$ {t_field_salario.value}"
        t_field_nome.value=""   #limpando os campos ja digitando
        t_field_nome.update()
        t_field_salario.value=""
        t_field_salario.update()   #limpando os campos ja digitando

        txt_resposta.update()
        #t_field_nome - peguei a referencia do nome
            #.value - estou me referindo ao valor

    btn_calcular.on_click=calculando
        #criei um evento para o botão - ao clicar ele vai fazer...
        #todo evento é construindo dentro de uma função

    txt_resposta=Text(value="Resposta", size=20)



    #estou usando o add para adicionar elementos da minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)

    pagina.add(txt_resposta)


    pagina.update()

app(target=main)