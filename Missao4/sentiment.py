import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Criar o analisador de sentimento VADER
sia = SentimentIntensityAnalyzer()

# Definindo um texto inicial para análise
user_input = "Este é um acampamento maravilhoso. Amei a serenidade e o canto dos pássaros pela manhã."

# Analisar o sentimento do texto
sentiment = sia.polarity_scores(user_input)

# Exibir o resultado
print(sentiment)


tweets = [
    "O goleiro do Bayer Leverkusen, Bernd Leno, não irá para o Napoli. Seu agente, Uli Ferber, para o Bild: Posso confirmar que houve negociações com o Napoli, que encerramos. Napoli não é uma opção. Atlético de Madrid e Arsenal são os outros rumores fortes. #B04 #AFC",
    "Gary Speed contra o Blackburn em St James em 2001/02, alguém? #NUFC #BEL #JAP #WorldCup",
    "@ChelseaFC Não o faça se arrepender e comece com ele no lugar de Hoofiz",
    "@LiverpoolFF @AnfieldEdition Ele é um mentiroso, inventado. Eu o deixei de seguir, assim como muitos outros. Totalmente falso. #LFC",
    "@theesk @Everton Não sabia que Kenwright deve sair no final do mês. Sinceramente, você acha que ele estaria interessado em nós?",
    "Relatório: Vinculado ao #Everton e #Wolves, os italianos estão prontos para assinar com um ponta avaliado em £4,5 milhões",
    "@ChelseaFC Pela primeira vez em muito tempo, meu coração ficou tranquilo enquanto assistia ao Chelsea. Realmente gostei hoje. Vamos, CHELSEA!!!",
    "Pogba marca, Pogba dá assistências. Mas amanhã os jornais não dirão isso, em vez disso, dirão como ele vai acabar na Juve porque está infeliz, frustrado, tem rancores com Mourinho e assim por diante #mufc",
    "@WestHamUtd precisamos manter o @CH14_ e trazer o @HirvingLozano70 para complementar",
    "@brfootball @aguerosergiokun @ManCity Que gênio. Pep levando a mentalidade vencedora com ele, conquistando liga após liga. Craque"
]


# Analisando o sentimento de cada tweet
for tweet in tweets:
    sentiment = sia.polarity_scores(tweet)
    print(f"Tweet: {tweet}")
    print(f"Resultado da análise: {sentiment}\n")
