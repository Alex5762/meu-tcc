<h1 align="center">📜 Análise de Dados Históricos: Segunda Guerra Mundial</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter Notebook" />
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Gemini_AI-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white" alt="Gemini API" />
</p>

## 📌 Sobre o Projeto

Este projeto é o resultado de um Trabalho de Conclusão de Curso (TCC) focado em **Ciência de Dados e História Digital**. O objetivo principal é transformar dados brutos e desclassificados pelo governo americano em conhecimento visual e acessível sobre a Segunda Guerra Mundial.

Utilizando o dataset **THOR (Theater History of Operations Reports)**, exploramos mais de 178 mil registros de missões de bombardeio para responder a perguntas históricas através de programação em Python.

---

## 🚀 Funcionalidades e Pipeline de Dados

O projeto segue um pipeline clássico de análise de dados:

1. **ETL (Extração, Transformação e Carga):** Limpeza de dados, tradução de colunas e formatação de datas.
2. **Tratamento de Anomalias:** Uso da fórmula matemática do Intervalo Interquartil (IQR) para identificação e remoção de *outliers*.
3. **Análise Exploratória (AED):** Uso do `pandas` e consultas SQL (via `pandasql`) para agrupamentos e estatísticas descritivas.
4. **Visualização de Dados:** Construção de gráficos interativos e estáticos com `matplotlib` (Evolução temporal, gráficos de barras e setores).
5. **Integração com IA Generativa:** Uso da API do **Google Gemini** (`google-generativeai`) nativamente no código Python para ler tabelas e gerar resumos textuais como um "historiador digital".

---

## 📂 Estrutura do Repositório

* `notebooks/projeto_analise_tcc.ipynb` 👉 **[ARQUIVO PRINCIPAL]** O Jupyter Notebook contendo todo o código Python, os gráficos gerados e a documentação interativa.
* `notebooks/roteiro_extensao.ipynb` 👉 Caderno focado na documentação e no *storytelling* da pesquisa.
* `docs/Documentacao_Metodologia_e_IA.md` 👉 Declaração das metodologias aplicadas e do uso de Inteligência Artificial como assistente de programação (*Pair Programming*).
* `docs/Organizacao_da_Equipe.md` 👉 Divisão das tarefas para a apresentação do projeto.

---

## 💻 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/Alex5762/meu-tcc.git
   ```
2. Abra a pasta do projeto no VS Code ou suba os arquivos no **Google Colab**.
3. Instale as dependências (caso rode localmente):
   ```bash
   pip install pandas matplotlib pandasql google-generativeai
   ```
4. Abra o arquivo `projeto_analise_tcc.ipynb` e execute as células sequencialmente.

> **Aviso sobre a API de IA:** Para rodar a seção 7.3 (Inteligência Artificial), você precisará gerar uma chave gratuita no [Google AI Studio](https://aistudio.google.com/app/apikey) e inseri-la no código.

---
Feito com 💻 e ☕ por **Joseph Alexsander** e equipe.
