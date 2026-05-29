# Documentação de Desenvolvimento do Projeto

**Projeto:** Análise de Dados Históricos da Segunda Guerra Mundial com Python (Dataset THOR)  
**Autor:** Joseph Alexsander  

---

## 1. Resumo das Atividades Realizadas

O projeto consistiu em aplicar um pipeline completo de Análise e Ciência de Dados sobre um dataset com registros reais de missões de bombardeio da Segunda Guerra Mundial. Foram executadas as seguintes etapas técnicas:

*   **ETL (Extração e Limpeza):** Carregamento da base de dados (mais de 178 mil linhas), conversão de colunas de datas para formatos adequados e tradução dos nomes das variáveis para português.
*   **Análise Exploratória Básica:** Utilização de ferramentas estatísticas do Pandas (`describe`, `groupby`, `min`, `max`) e consultas nativas via SQL utilizando a biblioteca `pandasql`.
*   **Tratamento de Anomalias:** Cálculo e aplicação da regra do Intervalo Interquartil (IQR) para a identificação matemática e remoção de registros fora do padrão (*outliers*).
*   **Visualização de Dados:** Geração de gráficos analíticos com `matplotlib`, incluindo Histogramas de distribuição, Gráficos de Barras, Gráficos de Setores (Pizza) e evolução temporal em Gráfico de Linhas.
*   **Integração de Machine Learning:** Treinamento de um modelo preditivo de **Regressão Logística** usando a biblioteca `scikit-learn` para classificar e prever a origem das operações aéreas com base em dados de latitude e longitude.

---

## 2. Declaração de Uso de Inteligência Artificial

Em conformidade com as diretrizes modernas de desenvolvimento de software, declara-se que foi utilizada **Inteligência Artificial Generativa** como ferramenta oficial de apoio técnico (metodologia de *Pair Programming* ou "Programação em Dupla") durante todo o ciclo de vida deste projeto.

A IA atuou como um "assistente de programação" sob a estrita direção, supervisão e revisão do autor principal, atuando nas seguintes frentes:

*   **Auxílio de Sintaxe:** Esclarecimento de dúvidas sobre o uso das bibliotecas `pandas` e `matplotlib`, fornecendo estruturas iniciais de código para serem adaptadas à base de dados do THOR.
*   **Correção de Erros (Debugging):** Análise rápida de mensagens de erro (*tracebacks*) durante as etapas de limpeza de dados e execução do código, orientando sobre como corrigir incompatibilidades de tipagem.
*   **Recomendação de Boas Práticas:** Sugestões valiosas para manter o código limpo, legível e organizado (*Clean Code* focado no nível Júnior), como a estruturação do Jupyter Notebook e a lógica para tratar os *outliers*.
*   **Formatação e Storytelling:** Auxílio na construção do layout das células de texto (*Markdown* e *HTML*), garantindo que as explicações estivessem bem diagramadas, com alto contraste visual e tabelas organizadas para facilitar a leitura da banca avaliadora.

O uso dessa tecnologia demonstra o domínio não apenas de programação, mas também de **Engenharia de Prompts**, uma competência técnica altamente requisitada no mercado de tecnologia atual.
