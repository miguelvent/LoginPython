from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_chat='*')],
    [sg.Checkbox('Deseja salvar seu Login?')],
    [sg.Button9('Entrar')]
]
# Janela
janela = sg.Window('Login', layout)
# Leitura de ações e eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
        if eventos == 'Entrar':
            if valores ['usuario'] == 'Vent' and valores ['senha'] == '240805': 
                print('Seja Bem vindo, Vent!')