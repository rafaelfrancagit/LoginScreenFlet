import flet as ft
import string as str


def main(page: ft.Page):
    # Configuração da página
    page.title = "Login Screen"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def check_password(mensagem):
        dlg = ft.AlertDialog(title=ft.Text(mensagem))
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Função chamada quando o botão é clicado
    def btn_click(e):
        # Verifica se ambos os campos de entrada (nome e senha) estão preenchidos / Verifica se senha preenche requisitos de segurança básicos
        if all([name_input.value, pass_input.value]):
            if len(pass_input.value) >= 6:
                if any(char.isupper() for char in pass_input.value):
                    if any(char in str.punctuation for char in pass_input.value):
                        check_password("Bem vindo " + name_input.value)
                    else:
                        check_password(
                            "A senha precisa ter ao menos 1 caracter especial"
                        )
                else:
                    check_password("A senha precisa ter ao menos 1 letra maiúscula")
            else:
                check_password("A senha precisa ter ao menos 6 caracteres")
        else:
            check_password("Preencha todos os campos")

    # Componentes da interface do usuário
    page.appbar = ft.AppBar(title=ft.Text("Login Screen"), center_title=True)
    name_input = ft.TextField(label="Nome", autofocus=True, hint_text="Digite seu nome")
    pass_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    submit_btn = ft.ElevatedButton(text="Enviar", width=600, on_click=btn_click)
    page.update()
    page.add(name_input, pass_input, submit_btn)


ft.app(target=main)
