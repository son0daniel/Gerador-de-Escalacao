#PERFIL DO TWITTER: https://twitter.com/EscalacaoSFC
#Importação de bibliotecas
from time import sleep #Da biblioteca time importa-se a função 'sleep'
import tweepy #Importa a biblioteca que permite acesso a API do Twitter
import random #Biblioteca para gerar números aleatórios
from os import environ #Biblioteca que obtém as variáveis de ambiente

#Obtenção das variáveis de ambiente
API_Key = environ.get('API_Key')
API_Secret = environ.get('API_Secret')
Access_Token = environ.get('Access_Token')
Access_Secret = environ.get('Access_Secret')

#Pegando as chaves da conta @EscalacaoSFC disponível no Twitter Developer (somente para contas desenvolvedoras)
auth = tweepy.OAuthHandler(API_Key, API_Secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if __name__ == "__main__":
    while True:
        while True:
            try:
                #Obtém a leitura do todo o conteúdo dos blocos de notas
                texto_times = open("times.txt", 'r', encoding='utf8')
                texto_gol = open("Jogadores/0_goleiros.txt", 'r', encoding='utf8')
                texto_latdir = open("Jogadores/1_latdir.txt", 'r', encoding='utf8')
                texto_zag = open("Jogadores/2_zagueiros.txt", 'r', encoding='utf8')
                texto_latesq = open("Jogadores/3_latesq.txt", 'r', encoding='utf8')
                texto_volantes = open("Jogadores/4_volantes.txt", 'r', encoding='utf8')
                texto_meias = open("Jogadores/5_meias.txt", 'r', encoding='utf8')
                texto_atacantes = open("Jogadores/6_atacantes.txt", 'r', encoding='utf8')
                texto_tec = open("Jogadores/7_tecnicos.txt", 'r', encoding='utf8')

                times = []
                for x in texto_times: 
                    times.append(str(x).replace("\n", ""))

                #Listas dos componentes do time
                goleiros = []  #Lista que armazena os goleiros do bloco de notas 0_goleiros.txt
                for x in texto_gol:
                    goleiros.append(str(x))

                latdir = [] #Lista que armazena os laterais-direitos do bloco de notas 1_latdir.txt
                for x in texto_latdir:
                    latdir.append(str(x))

                zagueiros = [] #Lista que armazena os zagueiros do bloco de notas 2_zagueiros.txt
                for x in texto_zag:
                    zagueiros.append(str(x))

                latesq = [] #Lista que armazena os laterais-esquerdos do bloco de notas 3_latesq.txt
                for x in texto_latesq:
                    latesq.append(str(x))

                volantes = [] #Lista que armazena os volantes do bloco de notas 4_volantes.txt
                for x in texto_volantes:
                    volantes.append(str(x))

                meias = [] #Lista que armazena os volantes do bloco de notas 5_meias.txt
                for x in texto_meias:
                    meias.append(str(x))

                atacantes = [] #Lista que armazena os volantes do bloco de notas 6_atacantes.txt
                for x in texto_atacantes:
                    atacantes.append(str(x))
                
                tecnicos = [] #Lista que armazena os técnicos do bloco de notas 7_tecnicos.txt
                for x in texto_tec:
                    tecnicos.append(str(x).replace("\n", ""))

                formacao = [0] * 4 #Lista de até 4 posições para armazenar a formação tática
                total = 0 #A soma geral da formação tática que tem de ser igual a 10

                #Geração aleatória da formação tática
                while total < 10:
                    total = 0
                    formacao = [0] * 4
                    formacao[0] = random.randint(3, 5)
                    formacao[1] = random.randint(0, 3)
                    total = formacao[0] + formacao[1] + formacao[2] + formacao[3]
                    while formacao[2] > 5 or formacao[2] == 0:
                        formacao[2] = random.randint(1, (9 - total))
                    total = formacao[0] + formacao[1] + formacao[2] + formacao[3]
                    while formacao[3] > 4 or formacao[3] == 0:
                        formacao[3] = random.randint(1, (10 - total))
                    total = formacao[0] + formacao[1] + formacao[2] + formacao[3]

                texto = "" #Variável que armazena o texto da formação tática (ex: 4-4-2)
                if formacao[1] == 0:
                    texto = str(formacao[0]) + "-" + str(formacao[2]) + "-" + str(formacao[3])
                else:
                    texto = str(formacao[0]) + "-" + str(formacao[1]) + "-" + str(formacao[2]) + "-" + str(formacao[3])

                mandante = bool(random.randint(0, 1)) #Definição aleatória se o time é mandante ou não (ex: Santos x Portuguesa ou Portuguesa x Santos)
                confronto = ""
                if mandante:
                    confronto = "Santos x " + times[random.randrange(0, len(times))]
                else:
                    confronto = times[random.randrange(0, len(times))] + " x Santos"
                intro = "Peixão escalado para " + confronto + "\n" + texto + "\n" #Texto introdutório do tweet

                escalacao = [None] * 11
                nome_pos = [None] * 11
                indice = random.randrange(0, len(goleiros))
                escalacao[0] = goleiros[indice]
                nome_pos[0] = "GOL" #Abreviatura da posição
                indice = 0

                if formacao[0] > 3:
                    indice = random.randrange(0, len(latdir))
                    while latdir[indice] in escalacao: #Caso o jogador já esteja na escalação...
                        indice = random.randrange(0, len(latdir)) #...retorne outro valor
                    escalacao[1] = latdir[indice]
                    nome_pos[1] = "LAD"
                    indice = random.randrange(0, len(latesq))
                    while latesq[indice] in escalacao:
                        indice = random.randrange(0, len(latesq))
                    escalacao[formacao[0]] = latesq[indice]
                    nome_pos[formacao[0]] = "LAE"


                cont = 2
                for x in range(formacao[0] - (2 if formacao[0] > 3 else 0)):
                    while zagueiros[indice] in escalacao:
                        indice = random.randrange(0, len(zagueiros))
                    escalacao[cont] = zagueiros[indice]
                    nome_pos[cont] = "ZAG"
                    cont += 1

                while None in escalacao:
                    escalacao.remove(None) 
                    nome_pos.remove(None)

                for x in range(formacao[1]):
                    indice = random.randrange(0, len(volantes))
                    while volantes[indice] in escalacao:
                        indice = random.randrange(0, len(volantes))
                    escalacao.append(volantes[indice])
                    nome_pos.append("VOL")

                for x in range(formacao[2]):
                    indice = random.randrange(0, len(meias))
                    while meias[indice] in escalacao:
                        indice = random.randrange(0, len(meias))
                    escalacao.append(meias[indice])
                    nome_pos.append("MEI")

                for x in range(formacao[3]):
                    indice = random.randrange(0, len(atacantes))
                    while atacantes[indice] in escalacao:
                        indice = random.randrange(0, len(atacantes))
                    escalacao.append(atacantes[indice])
                    nome_pos.append("ATA")

                count = 0
                indice = random.randrange(0, len(escalacao))
                for x in escalacao:
                    intro+= (nome_pos[count] + " " + str(x).replace("\n", "") + (" (Z)\n" if count == indice else "\n")) #(Z) = capitão do time
                    count+=1
                
                #Suplentes
                suplentes = []
                reserva_pos = []
                indice = random.randrange(0, len(goleiros))
                while goleiros[indice] in suplentes or goleiros[indice] in escalacao: #Caso o jogador já esteja na escalação ou no banco de reservas...
                    indice = random.randrange(0, len(goleiros)) #...retorne outro valor
                suplentes.append(goleiros[indice])
                reserva_pos.append("GOL")

                indice = random.randrange(0, len(latdir))
                while latdir[indice] in suplentes or latdir[indice] in escalacao:
                    indice = random.randrange(0, len(latdir))
                suplentes.append(latdir[indice])
                reserva_pos.append("LAD")

                indice = random.randrange(0, len(latesq))
                while latesq[indice] in suplentes or latesq[indice] in escalacao:
                    indice = random.randrange(0, len(latesq))
                suplentes.append(latesq[indice])
                reserva_pos.append("LAE")

                indice = random.randrange(0, len(zagueiros))
                while zagueiros[indice] in suplentes or zagueiros[indice] in escalacao:
                    indice = random.randrange(0, len(zagueiros))
                suplentes.append(zagueiros[indice])
                reserva_pos.append("ZAG")

                for x in range(2):
                    indice = random.randrange(0, len(meias))
                    while meias[indice] in suplentes or meias[indice] in escalacao:
                        indice = random.randrange(0, len(meias))
                    suplentes.append(meias[indice])
                    reserva_pos.append("MEI")

                indice = random.randrange(0, len(atacantes))
                while atacantes[indice] in suplentes or atacantes[indice] in escalacao:
                    indice = random.randrange(0, len(atacantes))
                suplentes.append(atacantes[indice])
                reserva_pos.append("ATA")

                indice = random.randrange(0, len(tecnicos))
                while tecnicos[indice] in suplentes or tecnicos[indice] in escalacao:
                    indice = random.randrange(0, len(tecnicos))
                tecnico = tecnicos[indice]
                intro+= "\nTEC " + tecnico

                final = "Suplentes:\n\n" 
                count = 0
                for x in suplentes:
                    final+= (reserva_pos[count] + " " + x)
                    count+=1
                    
                tweet = api.update_status(intro) #Primeiro tweet onde se apresenta os titulares do time e o treinador
                sleep(10) #Intervalo de 10 segundos para evitar spam
                resp = api.update_status(final, in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True) #Segundo tweet onde os suplentes são apresentados
                #Intervalo de 30 minutos entre cada tweet
                print("Vai dormir")
                sleep(900)
                print("Dormiu")
                sleep(900) 
            except tweepy.TweepError as e:
                print(e.reason) #Erro relacionado ao Twitter (excesso de caracteres ou proibição de postagem)
            except ValueError:
                print("erro " + str(total)) #Erro de geração de formação tática