'''
[PY-A09] Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de centímetros para metros.
'''

import tkinter as tk

def cm_To_mts():
    cm = entry_cm.get().strip()    
    if cm.isdecimal():
        resultado = int(cm)/100     
        entry_mt.delete(0, tk.END)  # Limpa o conteúdo atual
        entry_mt.insert(0, resultado)  # Insere o novo texto

janela = tk.Tk()

janela.title('Conversor de Medidas')
janela.geometry('300x300')

# Para a entrada de centimetros
entry_cm = tk.Entry(janela)
entry_cm.place(x=30, y=20, width=100, height=30)
lbl_cm = tk.Label(janela, text='Centimetros', font=("Arial", 12),fg='black')
# Posicionamento da label usando.place() para afastá-la da borda
lbl_cm.place(x=30, y=50, width=100, height=50)


# Para a entrada de metros
entry_mt = tk.StringVar()
entry_mt = tk.Entry(janela)
entry_mt.place(x=150, y=20, width=100, height=30)
lbl_mt = tk.Label(janela, text='Metros', font=("Arial", 12),fg='black')
lbl_mt.place(x=150, y=50, width=100, height=50)


btn_converter = tk.Button(janela, text='Converter',font=("Arial", 12),fg='black', command=cm_To_mts)
btn_converter.place(x=90, y=100, width=100, height=50)

msg = '''
Entre com o valor em Centimetros
o resultado aparece no campo Me-
tros após clicar Converter
'''
lbl_resultado = tk.Label(janela, text=msg, font=("Arial", 12), fg="Blue")
lbl_resultado.place(x=30, y=150)


janela.mainloop()
