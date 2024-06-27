#Criar uma aplicação que a pessoa vai digitar o salário e vc vai
# calcular quanto é 10% desse salario e mostrar a resposta na tela

from flet import Page, TextField, Text, ElevatedButton, app

def main (pagina:Page):
    pagina.title="Exercício 2"

    pagina.window_center()

    t_field_salario=TextField(label="Qual o seu salário?")
    btn_calcular=ElevatedButton(text="Resultado")

    def calculando(e):

        desconto= float(t_field_salario.value) * 0.1
       # descontoT= float(t_field_salario.value) - desconto

        txt_resposta.value = f"10% do seu salário é R${desconto}."
        txt_resposta.update()
        t_field_salario.value = ""
        t_field_salario.update()

    btn_calcular.on_click=calculando
    txt_resposta=Text(value="Resposta", size=20)

    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()
app(target=main)
