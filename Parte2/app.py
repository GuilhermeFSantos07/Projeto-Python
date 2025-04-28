import tkinter as tk
from tkinter import messagebox
from alunos import Alunos

class MenuPrincipal(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller

        label = tk.Label(self, text="Menu principal", font=("Arial", 16))
        label.pack(pady=10, padx=10)

        btn_cadastro = tk.Button(self, text="Cadastro",
                                command=lambda: controller.show_frame("TelaCadastro"))
        btn_cadastro.pack(pady=5)

        btn_altera = tk.Button(self, text="Alterar",
                               command=lambda: controller.show_frame("TelaAtualizar"))
        btn_altera.pack(pady=5)

        btn_lista = tk.Button(self, text="Lista",
                                command=lambda: controller.show_frame("TelaLista"))
        btn_lista.pack(pady=5)

class TelaCadastro(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller

        label = tk.Label(self, text="Cadastro de Aluno", font=("Arial", 14))
        label.grid(row=0, column=1, pady=10)

        tk.Label(self, text="Nome:").grid(row=1, column=0, sticky="e")
        self.entrada_nome = tk.Entry(self)
        self.entrada_nome.grid(row=1, column=1)

        tk.Label(self, text="ID (Opcional):").grid(row=2, column=0, sticky="e")
        self.entrada_id = tk.Entry(self)
        self.entrada_id.grid(row=2, column=1)

        tk.Label(self, text="Serie:").grid(row=3, column=0, sticky="e")
        self.serie_var = tk.StringVar()
        self.serie_var.set("1")
        self.opcao_serie = tk.OptionMenu(self, self.serie_var, *[str(i) for i in range(1, 10)])
        self.opcao_serie.grid(row=3, column=1)

        tk.Label(self, text="Turno:").grid(row=4, column=0, sticky="e")
        self.turno_var = tk.StringVar()
        self.turno_var.set("Matutino")
        self.opcao_turno = tk.OptionMenu(self, self.turno_var, "Matutino", "Vespertino")
        self.opcao_turno.grid(row=4, column=1)

        tk.Label(self,text="Turma").grid(row=5, column=0, sticky="e")
        self.turma_var = tk.StringVar()
        self.turma_var.set("1")
        self.opcao_turma = tk.OptionMenu(self, self.turma_var, *[str(i) for i in range(1,6)])
        self.opcao_turma.grid(row=5, column=1)

        tk.Label(self, text="Nota1:").grid(row=6, column=0, sticky="e")
        self.entrada_nota1 = tk.Entry(self)
        self.entrada_nota1.grid(row=6, column=1)

        tk.Label(self, text="Nota 2:").grid(row=7, column=0, sticky="e")
        self.entrada_nota2 = tk.Entry(self)
        self.entrada_nota2.grid(row=7, column=1)

        tk.Label(self, text="Nota 3:").grid(row=8, column=0, sticky="e")
        self.entrada_nota3 = tk.Entry(self)
        self.entrada_nota3.grid(row=8, column=1)

        tk.Label(self, text="Média:").grid(row=9, column=0, sticky="e")
        self.entrada_media = tk.Entry(self, state="readonly")
        self.entrada_media.grid(row=9, column=1)

        tk.Label(self, text="Aprovação:").grid(row=10, column= 0, sticky="e")
        self.entrada_aprov = tk.Entry(self, state="readonly")
        self.entrada_aprov.grid(row=10, column=1)

        self.btn_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_aluno)
        self.btn_cadastrar.grid(row=11, column=1, pady=10)

        self.btn_voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("MenuPrincipal"))
        self.btn_voltar.grid(row=11, column=0, pady=10)

    def cadastrar_aluno(self):
        nome = self.entrada_nome.get()
        aluno_id = self.entrada_id.get()
        serie = self.serie_var.get()
        turno = self.turno_var.get()
        turma = self.turma_var.get()
        try:
            nota1 = float (self.entrada_nota1.get())
            nota2 = float (self.entrada_nota2.get())
            nota3 = float (self.entrada_nota3.get())
        except:
            messagebox.showerror("Erro, as notas devem ser numéricas")
            return
        
        for n in (nota1, nota2, nota3):
            if n < 0.0 or n > 10.0:
                messagebox.showerror("As notas devem estar entre 0 e 10")
                return
        
        media = (nota1 + nota2 + nota3)/3
        aprovacao = "Aprovado" if media >= 6 else "Reprovado"

        self.entrada_media.config(state="normal")
        self.entrada_media.delete(0, tk.END)
        self.entrada_media.insert(0, f"{media: .2f}")
        self.entrada_media.config(state="readonly")

        self.entrada_aprov.config(state="normal")
        self.entrada_aprov.delete(0, tk.END)
        self.entrada_aprov.insert(0, aprovacao)
        self.entrada_aprov.config(state="readonly")

        aluno = Alunos()
        aluno.nome = nome
        aluno.serie = serie
        aluno.turno = turno
        aluno.turma = turma
        aluno.nota1 = nota1
        aluno.nota2 = nota2
        aluno.nota3 = nota3
        aluno.aprovacao = aprovacao
        if aluno_id:
            aluno.idaluno = aluno_id
        msg = aluno.inserirAluno()
        messagebox.showinfo("Cadastro", msg)
        self.limpar_campos()

    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_id.delete(0, tk.END)
        self.entrada_nota1.delete(0, tk.END)
        self.entrada_nota2.delete(0, tk.END)
        self.entrada_nota3.delete(0, tk.END)
        self.entrada_media.config(0, state="normal")
        self.entrada_media.delete(0, tk.END)
        self.entrada_media.config(0, state="readonly")
        self.entrada_aprov.config(0, state="normal")
        self.entrada_aprov.delete(0, tk.END)
        self.entrada_aprov.config(0, state="readonly")

class TelaAtualizar(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller

        label = tk.Label(self, text="Alterar Notas do Aluno", font=("Arial", 14))
        label.grid(row=0, column=1, pady=10)

        self.modo_procura = tk.StringVar(value="ID")
        btn_ID = tk.Radiobutton(self, text="Pesquisar Por ID", variable=self.modo_procura, value="ID")
        btn_nome = tk.Radiobutton(self, text="Procurar Por Nome", variable=self.modo_procura, value="Nome")
        btn_ID.grid(row=1, column=0, padx=10)
        btn_nome.grid(row=1, column=1, padx=10)

        tk.Label(self, text="Pesquisar:").grid(row=2, column=0, sticky="e")
        self.entrada_pesquisa = tk.Entry(self)
        self.entrada_pesquisa.grid(row=2, column=1, sticky="w")

        self.btn_buscar = tk.Button(self, text="Buscar", command=self.buscar_aluno)
        self.btn_buscar.grid(row=2, column=2, padx=5)

        self.resultado_busca = tk.Listbox(self, width=50)
        self.resultado_busca.grid(row=3, column=0, columnspan=3, pady=10)
        self.resultado_busca.bind("<<ListboxSelect>>", self.selecao)

        tk.Label(self, text="Nota 1:").grid(row=4, column=0, sticky="e")
        self.entrada_nota1 = tk.Entry(self)
        self.entrada_nota1.grid(row=4, column=1)

        tk.Label(self, text="Nota 2:").grid(row=5, column=0, sticky="e")
        self.entrada_nota2 = tk.Entry(self)
        self.entrada_nota2.grid(row=5, column=1)

        tk.Label(self, text="Nota 3:").grid(row=6, column=0, sticky="e")
        self.entrada_nota3 = tk.Entry(self)
        self.entrada_nota3.grid(row=6, column=1)

        self.btn_alterar = tk.Button(self, text="Alterar Notas", command=self.alterar_aluno)
        self.btn_alterar.grid(row=7, column=1, pady=10)

        self.btn_voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("MenuPrincipal"))
        self.btn_voltar.grid(row=7, column=0, pady=10)

        self.aluno_selecionado_id = None

    def buscar_aluno(self):
        modo = self.modo_procura.get()
        criterio = self.entrada_pesquisa.get()
        self.resultado_busca.delete(0, tk.END)
        self.aluno_selecionado_id = None
        if modo == "ID":
            aluno = Alunos()
            msg = aluno.procurarAluno(criterio)
            if "encontrado" in msg.lower():
                self.resultado_busca.insert(tk.END, f"ID: {aluno.idaluno} | Nome: {aluno.nome}")
                self.preencher_notas(aluno)
                self.aluno_selecionado_id = aluno.idaluno
            else:
                messagebox.showerror("Erro", msg)
        else:
            aluno = Alunos()
            resultados = aluno.procurarPorNome(criterio)
            if resultados:
                for resultado in resultados:
                    mostrar = f"ID: {resultado[0]} | Nome: {resultado[1]}"
                    self.resultado_busca.insert(tk.END, mostrar)
            else:
                messagebox.showerror("Erro", "Nenhum aluno com esse nome")
    
    def selecao(self, event):
        if self.modo_procura.get() == "Nome":
            if not self.resultado_busca.curselection():
                return
            index = self.resultado_busca.curselection()[0]
            texto_selecionado = self.resultado_busca.get(index)
            aluno_id = texto_selecionado.split("|")[0].strip().replace("ID: ", "")
            aluno = Alunos()
            msg = aluno.procurarAluno(aluno_id)
            if "encontrado" in msg.lower():
                self.preencher_notas(aluno)
                self.aluno_selecionado_id = aluno.idaluno

    def preencher_notas(self, aluno):
        self.entrada_nota1.delete(0, tk.END)
        self.entrada_nota1.insert(0, str(aluno.nota1))
        self.entrada_nota2.delete(0, tk.END)
        self.entrada_nota2.insert(0, str(aluno.nota2))
        self.entrada_nota3.delete(0, tk.END)
        self.entrada_nota3.insert(0, str(aluno.nota3))

    def alterar_aluno(self):
        if not self.aluno_selecionado_id:
            messagebox.showerror("Erro", "Selecione um aluno primeiro")
            return
        try:
            nota1 = float(self.entrada_nota1.get())
            nota2 = float(self.entrada_nota2.get())
            nota3 = float(self.entrada_nota3.get())
        except:
            messagebox.showerror("Erro", "As notas devem ser numericas")
            return
        for n  in (nota1, nota2, nota3):
            if n < 0.0 or n > 10.0:
                messagebox.showerror("Erro", "Notas devem estar entre 0.0 e 10.0")
                return
            
        media = (nota1 + nota2 + nota3)/3
        aprovacao = "Aprovado" if media >= 6 else "Reprovado"

        aluno = Alunos()
        aluno.idaluno = self.aluno_selecionado_id
        aluno.nota1 = nota1
        aluno.nota2 = nota2
        aluno.nota3 = nota3
        aluno.media = media
        aluno.aprovacao = aprovacao

        msg = aluno.atualizarAluno()
        messagebox.showinfo("Alteração", msg)
        self.limpar_campos()

    def limpar_campos(self):
        self.entrada_pesquisa.delete(0, tk.END)
        self.entrada_nota1.delete(0, tk.END)
        self.entrada_nota2.delete(0, tk.END)
        self.entrada_nota3.delete(0, tk.END)
        self.resultado_busca.delete(0, tk.END)
        self.aluno_selecionado_id = None

class TelaLista(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.controller = controller

        label = tk.Label(self, text="Listagem de alunos", font=("Arial", 14))
        label.grid(row=0, column=1, pady=10)

        tk.Label(self, text="Série:").grid(row=1, column=0, sticky="e")
        self.serie_var = tk.StringVar(value=1)
        self.opcao_serie = tk.OptionMenu(self, self.serie_var, *[str(i) for i in range(1,10)])
        self.opcao_serie.grid(row=1, column=1, sticky="w")

        tk.Label(self, text="Turno:").grid(row=2, column=0, sticky="e")
        self.turno_var = tk.StringVar(value="Matutino")
        self.opcao_turno = tk.OptionMenu(self, self.turno_var, "Matutino", "Vespertino")
        self.opcao_turno.grid(row=2, column=1, sticky="w")

        tk.Label(self, text="Turma").grid(row=3, column=0, sticky="e")
        self.turma_var = tk.StringVar(value="1")
        self.opcao_turma = tk.OptionMenu(self, self.turma_var, *[str(i) for i in range(1,6)])
        self.opcao_turma.grid(row=3, column=1, sticky="w")

        self.btn_listar = tk.Button(self, text="Listar", command=self.listar_alunos)
        self.btn_listar.grid(row=4, column=1, pady=10)

        self.txt_resultado = tk.Text(self, width=50, height=10)
        self.txt_resultado.grid(row=5, column=0, columnspan=3, pady=10)

        self.btn_voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("MenuPrincipal"))
        self.btn_voltar.grid(row=6, column=0, pady=10)

    def listar_alunos(self):
        serie = self.serie_var.get()
        turno = self.turno_var.get()
        turma = self.turma_var.get()

        aluno = Alunos()
        resultados = aluno.listarAlunos(serie, turno, turma)
        self.txt_resultado.delete(1.0, tk.END)
        if resultados:
            for r in resultados:
                self.txt_resultado.insert(tk.END, f"Nome: {r[0]} | Média: {r[1]:.2f} | {r[2]}\n")
            else:
                self.txt_resultado.insert(tk.END, "Nenhum aluno encontrado")

class MultiPageApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Sistema de notas")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPrincipal, TelaCadastro, TelaAtualizar, TelaLista):
            page_name = F.__name__
            frame = F(container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPrincipal")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()     

if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()