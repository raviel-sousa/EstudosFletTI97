#Criar uma aplicação que vai pegar o nome e o endereço da pessoa, pegue a rua, numero, bairro, cep separados, e vai mostrar na tela em dois elementos Text:
#Nome: Carlos
#Endereço: Rua srrsrrs Numero srsr CEP:00000

from flet import Page, TextField, ElevatedButton, app, Text

def main (pagina:Page):
######  define tudo que a minha tela vai possuir
    pagina.title = "Exercício 1"

    pagina.window_center()

######  colocandom elementos na minha tela
    t_field_nome = TextField(label="Nome")

    t_field_rua=TextField(label="Rua")
    t_field_bairro=TextField(label="Bairro")
    t_field_numero=TextField(label="Numero")
    t_field_cep=TextField(label="Cep")

    btn_exibir=ElevatedButton(text="Exibir")

    def exibir(e):
        txt_responda.value = f"Nome: {t_field_nome.value}"
        t_field_nome.value = ""
        t_field_nome.update()
        txt_resposta2.value = f"""
 Endereço
 Rua: {t_field_rua.value}
 Bairro: {t_field_bairro.value}
 Número: {t_field_numero.value}
 CEP: {t_field_cep.value}
         """
        t_field_rua.value = ""
        t_field_rua.update()
        t_field_bairro.value = ""
        t_field_bairro.update()
        t_field_numero.value = ""
        t_field_numero.update()
        t_field_cep.value = ""
        t_field_cep.update()

        txt_responda.update()
        txt_resposta2.update()

    btn_exibir.on_click = exibir

    #ativar o Txt

    txt_responda = Text(value="Resposta", size=20)
    txt_resposta2 = Text(value="", size=20)


######  adicionei os elementos da minha tela - COLOQUE NA ORDEM CEEEEEERRRTAAAAA


    pagina.add(t_field_nome)
    pagina.add(t_field_rua)
    pagina.add(t_field_bairro)
    pagina.add(t_field_numero)
    pagina.add(t_field_cep)
    pagina.add(btn_exibir)
    pagina.add(txt_responda)
    pagina.add(txt_resposta2)



    pagina.update()
app(target = main)
