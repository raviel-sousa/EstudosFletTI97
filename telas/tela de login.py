from flet import *


colorPrimary="#5d305f"
secondecolor="#77457a"
colorBar="#0A0A0D"
fontColor="#ffffff"
colorTeste="#734636"
backgroundColor="#ffffff"

def main (pagina:Page):

    pagina.window_max_width=1080
    pagina.window_max_height=1920

    pagina.window_width=350
    pagina.window_height=700

    pagina.window_min_width=300
    pagina.window_min_height=700

    pagina.window_center()

    pagina.title = "Tela de Login"
    pagina.bgcolor=backgroundColor
    imageLogin=Image(src="imgPagina.png")


    t_field_username = TextField(label="Username:")
    t_field_senha = TextField(label="Senha:")
                                                        #deixar a senha oculta

    btn_login = ElevatedButton(text="Login", width=300,
                                style=ButtonStyle(
                                                shape=RoundedRectangleBorder(radius=0),
                                                bgcolor={
                                                    MaterialState.DEFAULT:colorTeste,
                                                    MaterialState.HOVERED:colorPrimary
                                                },
                                                color=fontColor
                               ))



    lineImg=Row(controls=[imageLogin],alignment=MainAxisAlignment.CENTER)
    line1 = Row(controls=[t_field_username],alignment=MainAxisAlignment.CENTER)
    line2 = Row(controls=[t_field_senha],alignment=MainAxisAlignment.CENTER)
    line3 = Row(controls=[btn_login],alignment=MainAxisAlignment.CENTER)
    coluna = Column(controls=[lineImg,line1,line2,line3])

    def logado(e):
        txt_login.value = f"{len(t_field_username.value)}/8, você está logado."

        t_field_username.value = ""
        t_field_username.update()
        t_field_senha.value = ""
        t_field_senha.update = ()

        txt_login.update()

    btn_login.on_click = logado

    txt_login = Text(value="...", size=20)

    txt_login = TextField(
        counter_text="0/8",
        password=True,
        #can_revelal_password=True,
        helper_text="Sua senha deve possuir 8 caracteres."
    )
    pagina.add(coluna)
    pagina.add(t_field_username)
    pagina.add(t_field_senha)
    pagina.add(btn_login)
    pagina.add(txt_login)
    pagina.update()

if __name__ == '__main__':
    app(target = main)