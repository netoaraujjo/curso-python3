import csv


def le_arquivo():
    with open('desafio-ibge.csv', encoding='latin1') as arquivo:
        dados = csv.reader(arquivo)
        for i, dado in enumerate(dados):
            if i == 0:
                continue
            print(f'{dado[8]}: {dado[3]}')


if __name__ == '__main__':
    le_arquivo()