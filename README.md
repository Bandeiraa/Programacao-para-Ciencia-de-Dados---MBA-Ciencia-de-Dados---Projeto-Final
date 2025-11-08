# Análise de Consumo e Sustentabilidade Energética no Brasil
**Disciplina:** Programação para Ciência de Dados  
**Curso:** MBA Ciência de Dados — UNIFOR  
**Instrutor:** Cássio Pinheiro  

**Integrantes:**  
- Francisco Davi Bandeira Falcão (2528443)  

**Repositório GitHub:** [https://github.com/Bandeiraa/Programacao-para-Ciencia-de-Dados---MBA-Ciencia-de-Dados---Projeto-Final](https://github.com/Bandeiraa/Programacao-para-Ciencia-de-Dados---MBA-Ciencia-de-Dados---Projeto-Final)  
**Data de Entrega:** 14/11/2024  

---

# Objetivo do Projeto
Este projeto tem como objetivo analisar o **consumo de energia elétrica no Brasil**, com foco em sustentabilidade e eficiência energética.  
A proposta é identificar **padrões regionais**, **variações de consumo entre setores (residencial, comercial, industrial)** e **indicadores de eficiência energética**, utilizando ferramentas de análise de dados em Python.

**Problema:** compreender como diferentes regiões e tipos de consumidores contribuem para o consumo energético total e como isso se relaciona com o desenvolvimento sustentável.  

**Público-alvo:** estudantes, pesquisadores e gestores interessados em políticas públicas de energia e sustentabilidade.  

---

# Diagrama de Contexto
```mermaid
flowchart TD
  U["Usuário / Analista de Dados"] -->|Executa o script| P["Projeto de Análise Energética"]
  D[("Base de Dados ANEEL")] -->|Fornece dados CSV| P
  P --> R["Relatórios e Visualizações"]
  P --> E["Insights sobre Consumo e Sustentabilidade"]
  R --> U
  E --> U
