#containers - espaço que vc reserva pra trabaçhar com ele, para mudar cor, forma e etc

#content=Text(value=) - é possível colocar coisas dentro do container
                                        #content=Text(weight=) - largura do texto
                                        #width=, height= - vc deve defininr a largura e a altura
                                        #padding - altera o conteudo de dentro
                                        #marges - conteúdo externo
from flet import *

def main(page:Page):

    page.title="Trabalhando com Container"
    container1=Container(
        # content=Text("Text 1",
        #              size=64,
        #              weight=FontWeight.W_600,
        #              color="ffffff"
        #              ),
        bgcolor=colors.BLUE_400,
        width=550,
        height=550,
        #padding=45
        #padding = padding.all(190),
        #padding=padding.symmetric(vertical=90, horizontal=40))
        #padding = padding.only(top=87, left=50),
        #border=border.olny(top=BorderSide(5,color=colors.AMBER_500), bottom=BorderSide)
        # margin=margin.all(40),
        # gradient=LinearGradient(
        #     begin=alignment.top_center,
        #     end=alignment.bottom_center,
        #     colors=[colors.BLUE,colors.BLUE_ACCENT_200],
        #border_radius=border_radius.only(top_left=80,top_right=80,bottom_left=80,bottom_right=80),
        image_src="imgPagina.png",
        shadow=BoxShadow(
            spread_radius=10 #bordinha branca antes da sombra
            blur_radius=25, #desfoque
            color=colors.BLUE_GREY_400,
            offset=Offset(0, 0), #trablaha nos X e Y
            blur_style=ShadowBlurStyle.OUTER, #tipo do shadow
        )
        shadow=ShadowBlurStyle.INNER
        )


    page.add(container1)
    page.update()

if __name__ == '__main__':
    app(target=main)