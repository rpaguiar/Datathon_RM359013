Datathon - Fase 5 - Postech FIAP

Aplicação de Inteligência Artificial em processos de recrutamento e seleção, utilizando como base o estudo de caso da empresa Decision

IA aplicada ao Recrutamento – Painel com Random Forest
Objetivo
Este projeto utiliza técnicas de Machine Learning para auxiliar na priorização de candidatos em processos seletivos. A proposta é aplicar inteligência artificial para gerar scores preditivos de contratação com transparência e interpretabilidade, apoiando decisões gerenciais de forma mais ágil e consistente.

Abordagem técnica
- Algoritmo: Random Forest Classifier
- Foco do modelo: Maximizar o recall para evitar falso-negativos (bons candidatos sendo ignorados)
- Tratamento de variáveis: Codificação via LabelEncoder e estrutura de base com dados normalizados
- Interpretação: Cálculo da importância das variáveis via .feature_importances_

Funcionalidades do Dashboard
- Estatísticas gerais da base de candidatos
- Filtros por score mínimo, título da vaga e perfis prioritários
- Distribuição dos scores em gráfico interativo
- Visualização da importância das variáveis no modelo
- Tabela de candidatos filtrados e botão de exportação para CSV
A interface foi desenvolvida em Streamlit e permite tomada de decisão visual, simples e direta para gestores de recrutamento.

Link da aplicação (Streamlit)
Deploy disponível em: https://datathon-rm359013.streamlit.app/

Estrutura do projeto
projeto-ia-recrutamento/
│
├── app.py                    → Código do dashboard Streamlit
├── modelo_rf_v3.pkl          → Modelo Random Forest treinado e salvo
├── scores_contratacao_v3.csv → Base com scores de candidatos
├── requirements.txt          → Lista de dependências do projeto
└── README.md                 → Documentação geral

Tecnologias utilizadas
- Python 3.10+
- Streamlit
- scikit-learn
- pandas
- plotly
- joblib
