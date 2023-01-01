from tkinter import Tk, ttk, Text, Button
#from ttkthemes import ThemedTk
from ttkbootstrap import Style
from googletrans import Translator

translator = Translator()

def traduzir(evento=None):
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)
    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0',resultado.text)
    saida.configure(state='disabled')


#janela = ThemedTk(theme='equilux')
style = Style(theme='cyborg')
janela = style.master
janela.title('midnight translator')
janela.iconphoto('icone.png')
frame_geral = ttk.Frame()


values = ['pt', 'es', 'en']

#entradas
frame_entrada = ttk.Frame(frame_geral)

label_entradas = ttk.Label(frame_entrada,text='Entrada:', font=('Abys', 20))
combo_entrada = ttk.Combobox(frame_entrada, values=values)
combo_entrada.set('pt')


label_entradas.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1)
frame_entrada.pack()

entrada = Text(frame_geral,height=10, width=50, font=('Abys', 15))
entrada.pack(padx=10, fill='both', expand='yes')

#saidas
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(frame_saida,text='saida:', font=('Abys', 20))
combo_saida = ttk.Combobox(frame_saida, values=values)
combo_saida.set('en')


label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1)
frame_saida.pack()

saida = Text(frame_geral,height=10, width=50, font=('Abys', 15), state='disabled')
saida.pack(padx=10, fill='both', expand='yes')

botao = ttk.Button(
    frame_geral,
    text='Traduzir!',
    #font=(None, 15),
    command=traduzir)
    #state='disabled')
botao.pack(fill='both', padx=10, pady=10)

janela.bind('<Return>', traduzir)
frame_geral.pack()

janela.mainloop()