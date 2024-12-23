from PySimpleGUI import PySimpleGUI as sg  # Chamamos o Pysimplegui como sg (mais rápido de escrever)

# Função para calcular a TMB
def calculadora_tmb(sexo, peso, altura, idade):
    if sexo == "M":
        return 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif sexo == "F":
        return 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    else:
        return None

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text( 'Sexo'), sg.Button('M'), sg.Button('F'),],
    [sg.Text('Peso em KG ', size=(10, 1)), sg.Input(key='Peso')],
    [sg.Text('Altura em cm', size=(10, 1)), sg.Input(key='Altura')],
    [sg.Text('Idade', size=(10, 1)), sg.Input(key='Idade')],
    [sg.Button('Calcular TMB')],
    [sg.Text('', key='Resultado', size=(30, 2), text_color='black')]
]

# Janela
janela = sg.Window('Calculadora TMB', layout)
sexo = None  # Variável para armazenar o sexo escolhido

# Ler dados
while True:
    event, values = janela.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event in ['M', 'F']:
        sexo = event    
        sg.popup(f'Sexo selecionado: {sexo}')
    
    if event == 'Calcular TMB':
        try:
            peso = float(values['Peso'])
            altura = float(values['Altura'])
            idade = int(values['Idade'])

            if sexo:
                tmb = calculadora_tmb(sexo, peso, altura, idade)
                if tmb:
                    janela['Resultado'].update(f'Sua TMB é: {tmb:.2f} calorias/dia')
                else: 
                    sg.popup('Selecione o sexo antes de calcular.')
            
            else:
                sg.popup('Selecione o sexo antes!')

        except ValueError:
            sg.popup("Erro: Insira valores válidos para peso, altura e idade.")

# Fechar a janela
janela.close()
