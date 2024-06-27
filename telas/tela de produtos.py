from flet import *

def main(page:Page):
    page.title="Produtos"
    container1=Container(
        bgcolor="#042326",
        width=300,
        height=400,
        margin=margin.all(20),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        #border=border.only(top=BorderSide(15, color="#0A3A40"), bottom=BorderSide(15, color="#0A3A40")),
        img_src = "barra azul.png",
        shadow=BoxShadow(
            spread_radius=10,
            color="#0A3A40",
            blur_style=ShadowBlurStyle.OUTER
        )
    )

    container2=Container(
        bgcolor="#042326",
        width=300,
        height=400,
        margin=margin.all(20),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        # border=border.only(top=BorderSide(15, color="#0A3A40"), bottom=BorderSide(15, color="#0A3A40")),
        img_src = "barra lilas.png",
        shadow=BoxShadow(
            spread_radius=10,
            color="#0A3A40",
            blur_style=ShadowBlurStyle.OUTER
        )

    )

    container3=Container(
        content=Column(
            controls=[
                Row(controls=
                    Image(src="barra marrom.png")
                    ], alignment=MainAxisAlignment.CENTER,
            Row(
                controls=[
                    Text("Barra Marrom", size=20)
                    ], alignment=MainAxisAlignment.CENTER
            ),
            Rowc(
                controls=[
                    Text("Essa barra e ceral é muit saborosa.", width=200, text_align=TextAlign.JUSTIFY)
                ]

                    )


    )

    linha=Row(controls=[container1,container2,container3])
    page.add(linha)
    page.update()

if __name__ == '__main__':
    app(target=main)