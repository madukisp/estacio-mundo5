<style>
.custom-font {
  font-family: 'Arial', sans-serif;
  font-size: 16px;
}
</style>

<div class="custom-font">

<p align="center">
<img src="https://i.pinimg.com/originals/1a/21/6f/1a216fb0afdce66e7ffd9c9dbfce393b.jpg" alt="Logo do Projeto" width="200"/>
</p>
<h2 align="center">RPG0034  - Empregando Metodos Ageis</h2>
<h3 align="center">Missão Prática | Nível 4 | Mundo 5</h3>

* **Aluna:** Amanda Duque Kawauchi
* **Matrícula:** 202209170254
* **Campus:** Morumbi
* **Curso:** Desenvolvimento Full-Stack
* **Disciplina:** RPG0034  - Dando inteligência ao software
* **Turma:** 2024.3
* **Semestre Letivo:** 5º Semestre

<div style="page-break-before: always;"></div>

---

Análise de Sentimentos - Mentira, Rumores e Verdades

Projeto focado na análise de sentimentos dos tweets relacionados aos principais clubes de futebol da Inglaterra. Um projeto que traz à tona as nuances das opiniões digitais - ora exaltando os clubes, ora criticando suas gestões, e, muitas vezes, envolvendo até falsas alegações, mal-entendidos e opiniões controversas.

Live no dia da publicação do tweet, múltiplos usuários com opiniões divergentes, linguagem ambígua, criticando, exaltando, mas sem nunca mencionar os reais fatos ou evidências. A única coisa que falta para entender de fato o sentimento por trás das palavras é a ANÁLISE DETALHADA com VADER.

### Contextualização

Recentemente, a empresa onde trabalho como **Analista de Data Science** foi contratada para explorar a percepção pública sobre **clubes de futebol ingleses**. Várias publicações foram feitas, contendo desde simples exaltações até acusações mais duras, criando um ambiente repleto de boatos e desinformações.

Nosso objetivo é separar o verdadeiro sentimento por trás dos tweets. Desvendar o tom de cada mensagem: é verdadeiramente apoio ou ironia camuflada? Positivo, negativo, neutro?

### Processo de Análise

1. **Instalação de Ferramentas**  
   Utilizamos `nltk` e o **VADER Sentiment Analyzer** para realizar a análise. Isso envolveu:
   - **Instalar bibliotecas**: Instalação do NLTK para manipulação de textos.
   - **Download dos recursos**: Baixar o lexicon do VADER, essencial para detecção de sentimentos.

2. **Importação do Analisador e Definição de Texto Inicial**  
   Definimos um exemplo simples, como:
   ```
   "This is a wonderful campsite. I loved the serenity and the birds chirping in the morning."
   ```
   Queremos entender como o VADER lida com termos positivos.

3. **Análise dos Tweets**  
   Em seguida, a análise dos tweets:
   ```
   "@ChelseaFC For the first time in a long while, my heart was relaxed while watching Chelsea. Really enjoyed it today. Come on, CHELSEA!!!"
   ```
   Tweets como esse, carregados de sentimentos, ora positivos, ora frustrados. Onde está a verdade? O VADER nos ajudou a ver.

### Resultados e Discussão

- Cada tweet foi analisado, trazendo um dicionário de sentimentos:
  - **neg**: Pontuação negativa.
  - **neu**: Pontuação neutra.
  - **pos**: Pontuação positiva.
  - **compound**: Uma nota geral sobre o sentimento, variando de -1 (extremamente negativo) a 1 (extremamente positivo).

Exemplo:
```
Tweet: "@WestHamUtd we need to keep @CH14_ and get @HirvingLozano70 to complement"
Resultado: {'neg': 0.0, 'neu': 0.684, 'pos': 0.316, 'compound': 0.6369}
```
Observamos uma **neutralidade predominante** misturada com um tom de apoio positivo.

### Conclusão

A análise revelou a mistura de **emoções verdadeiras** e **boatos não confirmados** que as redes sociais são capazes de espalhar. Ao identificar o sentimento dos tweets, conseguimos ver que muitos usuários estavam apenas desabafando suas frustrações, enquanto outros mostravam apoio genuíno. O próximo passo? Continuar investigando e mergulhar mais fundo nos **dados sociais**, para que possamos de fato **trazer à luz** as verdades escondidas nas entrelinhas dos comentários.

O projeto mostrou que, mesmo em meio a boatos e falsas informações, **há sempre uma verdade nas emoções**. Agora, precisamos da aplicação prática desse conhecimento - seja para **derrubar as mentiras**, seja para **fortalecer a base dos apoiadores**.

A **PRISÃO DOS FALSOS DADOS** foi feita, agora resta entender como usar a **VERDADE DOS SENTIMENTOS**.

</div>