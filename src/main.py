from random import choice
from time import sleep
import os

class JokenPo:
    def __init__(self):
        self._dados = {'pedra': '✊', 'papel': '🖐️', 'tesoura': '✌️'}

    def pc_joga(self):
        sorteio = choice(list(self._dados.keys()))
        return self._dados.get(sorteio)

    def usuario_joga(self, emoj):
        return self._dados.get(emoj.lower(), 'invalido')

    def verifica_vencedor(self, escolha_usuario, escolha_aleatoria):
        user = self.usuario_joga(escolha_usuario)

        if user == 'invalido':
            return 'opcao invalida! Tente Novamente.'
        
        if user == escolha_aleatoria:
            return 'EMPATE'

        valores = (
            (user == '✊' and escolha_aleatoria == '✌️') or
            (user == '🖐️' and escolha_aleatoria == '✊') or
            (user == '✌️' and escolha_aleatoria == '🖐️')
        )

        return 'VITORIA' if valores else 'DERROTA'

def resultado(jogador, pc):
    tamanho = f'{"JOKENPO":=^30}'

    if jogador == 'invalido':
        return

    print(tamanho)
    print(f'Meu jogo: [{jogador} ] VS PC: [ ]'.center(len(tamanho)))
    print('=' * len(tamanho))
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(tamanho)
    print(f'Meu jogo: [{jogador} ] VS PC: [{pc} ]'.center(len(tamanho)))
    print('=' * len(tamanho))

def menu():
    meu_menu = '=' * 20
    print(meu_menu)
    print('MENU DE OPÇÕES'.center(len(meu_menu)))
    print(meu_menu)
    print('- PEDRA')
    print('- PAPEL')
    print('- TESOURA')
    print('- ENTER PARA SAIR')
    print('=' * len(meu_menu))
    

jogo = JokenPo()

while True:
    menu()
    opcao = input('escolha uma opcao: ')
    minha_jogada = jogo.usuario_joga(opcao)

    if opcao == '':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('SISTEMA SENDO ENCERRADO...')
        sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('SISTEMA ENCERRADO COM SUCESSO!!!')
        break
    if minha_jogada == 'invalido':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('opcao invalida! Tente Novamente.')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    escolha_pc = jogo.pc_joga()
    os.system('cls' if os.name == 'nt' else 'clear')
    resultado(minha_jogada, escolha_pc)
    jogada = jogo.verifica_vencedor(opcao, escolha_pc,)
    print(f'{jogada:-^15}'.center(30))
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')