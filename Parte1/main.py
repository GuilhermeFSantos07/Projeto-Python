if __name__ == '__main__':
    alunos = []

    try:
        quantidade = int(input("Digite a quantidade de alunos a ser cadastrado: "))
    except ValueError:
        print("Digite um valor valido")
    
    for q in range(quantidade):
        nome = input(f"Digite o nome do Aluno de número {q + 1}: ")
        notas = []
        for n in range(3):
            nota = float(input(f"Digite a nota {n + 1} do aluno {nome}: "))
            notas.append(nota)
        alunos.append({"nome": nome, "notas": notas})

    for aluno in alunos:
        x = aluno.get("notas")
        media = sum(aluno["notas"])/len(aluno["notas"])
        print(f"Aluno: {aluno["nome"]} \nNotas: {x}\nMedia: {media: .2f}")
        if media >= 6:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")