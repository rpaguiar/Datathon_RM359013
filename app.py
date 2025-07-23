import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Configuração da página
st.set_page_config(page_title="Dashboard de Contratação", layout="wide")
st.title("Dashboard de Contratação")

# Carregamento dos dados
df = pd.read_csv("scores_contratacao_v3.csv")
modelo_rf = joblib.load("modelo_rf_v3.pkl")

# Estatísticas
st.subheader("Estatísticas gerais")

col1, col2, col3 = st.columns(3)
col1.metric("Total de candidatos", len(df))
col2.metric("Score mínimo", round(df['score_contratacao_v3'].min(), 2))
col3.metric("Score máximo", round(df['score_contratacao_v3'].max(), 2))

# Nomes das variáveis usadas
nome_variaveis = ['formacao_e_idiomas.nivel_ingles', 'formacao_e_idiomas.nivel_espanhol', 'formacao_e_idiomas.nivel_academico', 'informacoes_profissionais.nivel_profissional',
'informacoes_profissionais.area_atuacao','perfil_vaga.estado']

importancias = modelo_rf.feature_importances_

# Importância das variáveis – gráfico
st.subheader("Importância das variáveis no modelo")

df_importancias = pd.DataFrame({"Variável": nome_variaveis, "Importância": importancias}).sort_values(by="Importância", ascending=True)

fig_imp = px.bar(df_importancias, x="Importância", y="Variável", orientation="h", title="Importância das variáveis – Random Forest V3", color="Importância", color_continuous_scale="Blues"
)
st.plotly_chart(fig_imp, use_container_width=True)

# Filtros
st.sidebar.header("Filtros")

score_min = st.sidebar.slider("Score mínimo", 0.0, 1.0, 0.5, 0.01)
vaga_selecionada = st.sidebar.selectbox("Título da vaga", ["Todas"] + sorted(df['titulo_vaga'].dropna().unique()))
prioritarios = st.sidebar.checkbox("Mostrar apenas prioritários (score ≥ 0.8)")

# Aplicação dos filtros
df_filtrado = df[df['score_contratacao_v3'] >= score_min]

if vaga_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['titulo_vaga'] == vaga_selecionada]

if prioritarios:
    df_filtrado = df_filtrado[df_filtrado['score_contratacao_v3'] >= 0.8]

# Gráfico de distribuição dos scores
st.subheader("Distribuição dos scores")

fig_score = px.histogram(df, x="score_contratacao_v3", nbins=25, title="Distribuição dos scores na base", labels={"score_contratacao_v3": "Score de contratação"}, color_discrete_sequence=["royalblue"])
fig_score.update_layout(bargap=0.15)
st.plotly_chart(fig_score, use_container_width=True)

# Tabela de candidatos
st.subheader("Candidatos filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Botão de exportação
st.subheader("Exportar CSV filtrado")
st.download_button(label="Exportar para CSV", data=df_filtrado.to_csv(index=False).encode("utf-8"), file_name="candidatos_filtrados.csv", mime="text/csv")