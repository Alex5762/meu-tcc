# Organização da Equipe e Roteiro de Apresentação

**Projeto:** Análise de Dados Históricos da Segunda Guerra Mundial com Python  
**Equipe:** Joseph Alexsander, [Integrante 2], [Integrante 3] e [Integrante 4]

Este documento organiza a divisão de tarefas para a apresentação do projeto. A ideia é estruturar o grupo como uma "Squad" de tecnologia, garantindo que todos os integrantes tenham um papel claro, uma fala definida e saibam exatamente o que explicar (mesmo quem não tem tanta facilidade com a programação).

---

## 👥 Divisão de Papéis

### 1. Desenvolvedor Principal / Analista de Dados
**Responsável:** Joseph Alexsander  
**Papel:** É o líder técnico do projeto. Vai explicar a estrutura geral do código e a lógica de programação.
*   **O que deve falar na apresentação:**
    *   Apresentar o Jupyter Notebook e explicar rapidamente as bibliotecas utilizadas (`pandas`, `matplotlib`, etc).
    *   Explicar como o banco de dados (THOR) foi importado para dentro do Python.
    *   Mostrar as linhas de código que geraram os visuais (gráficos de pizza e barras).

### 2. Engenheiro de Qualidade de Dados (QA / Limpeza)
**Responsável:** [Nome do Colega 1]  
**Papel:** Explica a parte de higienização dos dados. Mostra para a banca que dados reais dão trabalho e vêm com problemas de formatação.
*   **O que deve falar na apresentação:**
    *   O que significa a etapa de ETL (Extração, Transformação e Limpeza).
    *   A necessidade de traduzir e formatar colunas de datas.
    *   Como a equipe utilizou a matemática (regra do IQR) para identificar e remover anomalias e registros absurdos (*outliers*) da base de dados.

### 3. Especialista de Domínio / "O Historiador"
**Responsável:** [Nome do Colega 2]  
**Papel:** Não vai falar nada de código. É a pessoa responsável por "traduzir" os gráficos gerados pelo Python para a História real.
*   **O que deve falar na apresentação:**
    *   Apresentar as descobertas: Explicar o gráfico de evolução temporal, mostrando o motivo do pico de bombardeios em 1944 (Operação Overlord/Dia D).
    *   Comentar os resultados dos países líderes de missões (EUA) e o foco em áreas urbanas como alvos.
    *   Garantir a relevância social do trabalho.

### 4. Responsável por Inovação e Inteligência Artificial
**Responsável:** [Nome do Colega 3]  
**Papel:** Fica com o fechamento do trabalho, focado na parte moderna e "hypada" da tecnologia.
*   **O que deve falar na apresentação:**
    *   Explicar a exigência do "Uso de IA" no projeto.
    *   Mostrar a Seção 7.3 do caderno, onde o código em Python se conecta com a nuvem do Google.
    *   Ressaltar que o grupo treinou um **Modelo de Machine Learning (Regressão Logística)** ensinado pelo próprio professor e demonstrar a previsão em tempo real.

---

## 💡 Dicas para o Grupo no Dia da Apresentação

1. **Foco na lógica:** Não deixem ninguém ler código linha por linha (ex: ficar falando `df.head()`). Expliquem a **função** do bloco de código.
2. **Passagem de Bastão:** Pensem na apresentação como uma linha de montagem. O *QA* limpa o dado e passa a palavra para o *Desenvolvedor*, que cria o gráfico e passa a palavra para o *Historiador* analisar. Fica super profissional.
3. **Plano de Backup:** Pelo menos duas pessoas do grupo devem ter o arquivo `.ipynb` aberto no seu próprio computador ou Google Colab, caso a internet caia ou o PC de um trave na hora H.
