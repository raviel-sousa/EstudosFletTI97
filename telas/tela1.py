import flet as ft

#cria o layout da pagina
def main(page:ft.Page):
    page.title="Primeira pagina"
    tf_nome=ft.TextField(label="Digite o seu nome", color="#8B008B")    #caixa de texto
    btn_cadastrar=ft.ElevatedButton(text="Cadastrar", color="green")    #botão

    #mostrar na pagina
    page.add(tf_nome)
    page.add(btn_cadastrar)

    #eventos - ex: ao clicar botões
    def enviarNome(e):
        print(tf_nome.value) #para mostrar o que a pessoa digitou no Run do python

    btn_cadastrar.on_click=enviarNome   #não colocar parentes

    #toda vez que eu alterar a minha página eu devo dar um update
    page.update()

if __name__ == '__main__':
    #cria a pagina pra mim, baseado em algum layout
    ft.app(target=main)
    #defini qual layout que ele deve rodar, no cas o que acabei de criar acima "main"
    #target - mirar


#ft.app(main) - p aplicativo