# Roteiro de Extensão
## Análise de Dados Históricos da Segunda Guerra Mundial com Python

**Discente:** Joseph Alexsander
**Professor(a) Orientador(a):** [Nome do Professor]
**Ano:** 2026 · **Cidade/Estado:** [Cidade/UF]

---

## 1. DIAGNÓSTICO E TEORIZAÇÃO

### 1.1 Partes Interessadas e Parceiros

O projeto é direcionado a **professores de história do ensino médio** e seus **alunos**, que encontram dificuldades em tornar o conteúdo da Segunda Guerra mais visual e quantitativo em sala de aula.

| Público | Perfil |
|---|---|
| Professores de história | Graduados em Licenciatura, 25–55 anos, ensino público e privado |
| Estudantes do Ensino Médio | 15–18 anos, sem formação técnica em dados |

O projeto foi desenvolvido com acompanhamento do professor orientador da disciplina, que atuou como interlocutor e validador do escopo e da abordagem adotada.

---

### 1.2 Problemática Identificada

O conteúdo sobre a Segunda Guerra Mundial é ensinado de forma factual e estática — datas, batalhas, nomes — sem que estudantes consigam compreender a **dimensão quantitativa do conflito**: quantas missões foram feitas? Quais países foram mais bombardeados? Como a guerra evoluiu ao longo dos anos?

Grandes acervos históricos digitais — como o THOR, do governo americano — existem, mas são inacessíveis para quem não trabalha com dados. A problemática central é: **como transformar dados históricos brutos em conhecimento visual acessível para o ensino de história?**

---

### 1.3 Justificativa

- O campo da **História Digital** demonstra que análise quantitativa de registros históricos revela padrões impossíveis de perceber por métodos tradicionais.
- O curso de **Tecnologia da Informação** forma profissionais que devem aplicar ciência de dados a problemas reais — e o ensino de história é um problema real com impacto social direto.
- A **BNCC do Ensino Médio** prevê que o estudante use diferentes linguagens — incluindo a digital — para compreender e interpretar o mundo. Visualizações de dados históricos respondem a essa demanda.
- O dataset utilizado (THOR/NARA) é um **registro governamental oficial desclassificado**, garantindo credibilidade histórica ao trabalho.

---

### 1.4 Objetivos a Serem Alcançados

- **Desenvolver** um Jupyter Notebook em Python, documentado em português, que processe os dados do THOR e gere visualizações históricas.
- **Produzir** gráficos e análises que traduzam os dados brutos em conhecimento histórico acessível para o ensino médio.
- **Disponibilizar** o material como recurso educacional aberto, utilizável por qualquer professor de história sem custo.

---

### 1.5 Referencial Teórico

| Autor | Obra | Contribuição |
|---|---|---|
| Moretti (2013) | *Distant Reading* | Análise quantitativa de grandes conjuntos de dados nas humanidades |
| Guldi & Armitage (2014) | *The History Manifesto* | Uso de bases de dados históricas para recuperar relevância social das ciências humanas |
| Tukey (1977) | *Exploratory Data Analysis* | Fundamento metodológico da AED adotada no projeto |
| McKinney (2017) | *Python for Data Analysis* | Base técnica do pipeline com pandas e bibliotecas de visualização |
| Chartier (1998) | *A Ordem dos Livros* | Transformação do acesso ao conhecimento pela digitalização |
| MEC (2018) | BNCC — Ensino Médio | Competência digital no currículo do ensino básico |
| NARA (2026) | Dataset THOR | Fonte primária dos dados utilizados |

---

## 2. PLANEJAMENTO E DESENVOLVIMENTO DO PROJETO

### 2.1 Plano de Trabalho

| Semana | Etapa | Entrega |
|---|---|---|
| 1 | Diagnóstico: definição da problemática e do dataset | Seção 1 do Roteiro |
| 2 | ETL: carregamento, tratamento e renomeação dos dados | Células 1.5 e 1.6 do Notebook |
| 3 | AED Básica: head, shape, groupby, min/max, SQL | Seção 2 do Notebook |
| 4 | Visualizações: histograma, KDE, barras, pizza, evolução | Seções 3–6 do Notebook |
| 5 | Análises avançadas: WordCloud, Apriori, K-Means | Seção 7 do Notebook |
| 6 | Encerramento: revisão, storytelling e roteiro | Roteiro completo |

---

### 2.2 Envolvimento do Público Participante

O público foi envolvido de forma indireta, por meio de três estratégias:

1. **Professor orientador** acompanhou o desenvolvimento e validou a pertinência da abordagem e da linguagem utilizada.
2. **Colegas de curso** avaliaram informalmente a clareza das visualizações e a acessibilidade do conteúdo.
3. **Adequação da linguagem**: todo o storytelling do notebook foi escrito em português acessível, para que um professor de história sem formação em programação consiga compreender os resultados sem executar código.

---

### 2.3 Grupo de Trabalho

| Membro | Responsabilidade |
|---|---|
| **Joseph Alexsander** | Configuração do ambiente, tratamento dos dados, desenvolvimento completo do notebook (código + markdown), produção das visualizações, aplicação dos algoritmos de IA e redação do Roteiro de Extensão. |

---

### 2.4 Metas e Indicadores de Avaliação

| Meta | Indicador | Como verificar |
|---|---|---|
| Processar o dataset completo | 178.281 registros carregados sem erros | Executar notebook sem erros |
| Traduzir colunas para português | 11 colunas renomeadas | `df.columns` no notebook |
| Gerar visualizações legíveis | 7 gráficos produzidos | Outputs no notebook |
| Aplicar SQL real nos dados | Query com pandasql retornando resultado correto | Output da célula 2.7 |
| Aplicar algoritmos de IA | K-Means (3 clusters) + Apriori (≥ 3 regras) | Output das células 7.2 e 7.3 |
| Storytelling em português | Texto acadêmico em todas as células markdown | Revisão do notebook |

---

### 2.5 Recursos Previstos

| Recurso | Custo |
|---|---|
| Python 3.14 + bibliotecas open source | R$ 0,00 |
| Jupyter Notebook / VS Code | R$ 0,00 |
| Dataset THOR (NARA / data.world) | R$ 0,00 |
| Computador e internet pessoais | R$ 0,00 |
| **Total** | **R$ 0,00** |

Todos os recursos são gratuitos e open source.

---

### 2.6 Detalhamento Técnico do Projeto

O produto desenvolvido é um **Jupyter Notebook em Python** com 7 seções cobrindo todo o pipeline de ciência de dados:

```
Dataset THOR (.csv, 178k registros)
        ↓
ETL → Carregamento + Renomeação de Colunas + Conversão de Tipos
        ↓
AED Básica → head / shape / groupby / min / max / SQL (pandasql)
        ↓
Distribuição → Histograma + Outliers (IQR) + KDE por ano
        ↓
Classificação → Barras (missões por país) + Pizza (tipos de alvo)
        ↓
Evolução → Linha 1939–1945 (pico em 1944: Operação Overlord)
        ↓
Avançado → WordCloud + Regras de Associação (Apriori) + K-Means
        ↓
Notebook documentado em português com storytelling histórico
```

**Bibliotecas utilizadas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `wordcloud`, `mlxtend`, `scikit-learn`, `folium`, `pandasql`.

**Dataset:** THOR (Theater History of Operations Reports) — acervo desclassificado pelo *National Archives and Records Administration* (NARA), EUA. 178.281 registros de missões aéreas aliadas entre 1939 e 1945.

---

### 2.7 Limitações Históricas dos Dados

> *"Os dados representam majoritariamente operações Aliadas. Registros do Eixo foram perdidos ou não foram desclassificados. Essa assimetria não invalida o estudo — ela é, em si mesma, um dado histórico relevante."*

---

## 3. ENCERRAMENTO DO PROJETO

### 3.1 Relato Coletivo

O projeto atingiu todos os objetivos propostos:

- ✅ Notebook executável com 7 seções, código em Python e storytelling em português.
- ✅ 7 visualizações históricas produzidas e testadas.
- ✅ Algoritmos de machine learning (K-Means e Apriori) aplicados sobre dados reais.
- ✅ Material legível por professores de história sem formação em dados.

**Principais descobertas:**
- EUA realizaram 53% de todas as missões aliadas (>94.000).
- 1944 foi o ano mais intenso da guerra aérea — pico de 80.000 missões (Operação Overlord).
- Berlim, Hamburgo e Colônia foram os alvos mais bombardeados.
- K-Means identificou 3 perfis de missão: pequenas, médias e grandes operações.

---

### 3.2 Avaliação de Reação da Parte Interessada

A avaliação foi realizada junto ao professor orientador da disciplina, que acompanhou o projeto e avaliou:

- **Clareza das visualizações** — compreensíveis para público não técnico? ✅
- **Relevância histórica** — resultados bem contextualizados? ✅
- **Qualidade do código** — organizado, comentado e reproduzível? ✅
- **Potencial didático** — pode ser usado em aulas de história? ✅

---

### 3.3 Relato de Experiência Individual

**Discente:** Joseph Alexsander

#### Contextualização

Este projeto surgiu da tentativa de unir a ciência de dados — área central do meu curso — com história contemporânea. O dataset THOR, com 178.000 registros reais de missões de bombardeio, oferecia dados densos e historicamente significativos, tornando-se o ponto de partida ideal para uma análise que fosse técnica e educacionalmente relevante.

#### Metodologia

Seguiu-se o pipeline clássico de ciência de dados: ETL → AED Básica → Visualizações de Distribuição → Classificação → Evolução → Análises Avançadas com IA. Todo o processo foi documentado em português com células markdown explicativas entre os blocos de código.

#### Resultados e Discussão

Os dados confirmaram o que a historiografia descreve qualitativamente. O pico de 80.000 missões em 1944 corresponde diretamente à Operação Overlord. Os 27% de ataques a áreas urbanas evidenciam a escala do bombardeio estratégico aliado. A nuvem de palavras revelou Berlim como o alvo mais frequente da guerra. O K-Means identificou automaticamente três perfis de missão: operações táticas pequenas (maioria), médias e as grandes incursões de impacto estratégico.

#### Reflexão Aprofundada

O maior aprendizado não foi técnico — foi interpretativo. Gerar um gráfico é simples; entender o que ele representa historicamente é o verdadeiro desafio. Descobrir que 80.000 missões em 1944 não é só um número, mas a maior campanha de bombardeio da história humana, mudou minha forma de enxergar o que ciência de dados pode fazer. Além disso, documentar as limitações do dataset — ao invés de ignorá-las — foi a decisão mais honesta e, paradoxalmente, a que mais enriqueceu o trabalho.

#### Considerações Finais

Este foi meu primeiro contato real com análise de dados sobre registros históricos verdadeiros. O projeto mostrou que ciência de dados e humanidades não são campos opostos — são perspectivas complementares que, juntas, produzem conhecimento mais rico e com impacto social concreto. Próximos passos naturais incluem um dashboard interativo com Streamlit e a expansão da análise para o teatro do Pacífico.

---

## Referências Bibliográficas

CHARTIER, R. **A Ordem dos Livros**. Brasília: UnB, 1998.

GULDI, J.; ARMITAGE, D. **The History Manifesto**. Cambridge: Cambridge University Press, 2014.

McKINNEY, W. **Python for Data Analysis**. 2. ed. Sebastopol: O'Reilly Media, 2017.

MORETTI, F. **Distant Reading**. London: Verso Books, 2013.

TUKEY, J. W. **Exploratory Data Analysis**. Reading: Addison-Wesley, 1977.

BRASIL. **Base Nacional Comum Curricular — Ensino Médio**. Brasília: MEC, 2018.

NARA. **THOR — Theater History of Operations Reports: WWII**. Disponível em: https://data.world/datamil/world-war-ii-thor-data. Acesso em: maio 2026.
