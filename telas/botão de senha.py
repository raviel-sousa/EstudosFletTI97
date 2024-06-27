import flet as ft


def main(page: ft.Page):

    def counter(e):
        tf.counter_text = f"{len(tf.value)}/8"
        page.update()

    page.window_width = 800
    page.window_height = 600

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.theme = ft.Theme(color_scheme_seed="pink")

    tf = ft.TextField(
        # label="Name",
        hint_text="Password",
        width=380,
        border_color="pink",
        border_radius=ft.border_radius.all(5),
        color="pink",
        cursor_color="pink",
        multiline=True,
        content_padding=20,
        capitalization=ft.TextCapitalization.CHARACTERS,
        counter_text="0/8",
        on_change=counter,
        password=True,
        can_reveal_password=True,
        helper_text="Your password must be at least 8 characters."
    )
    page.add(tf)


ft.app(target=main)