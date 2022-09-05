import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Title and Subheader
st.title("Student Performance EDA App")
st.subheader("EDA Web App com Streamlit ")

class DataFrame_Loader():

    def __init__(self):
        
        print("Loadind DataFrame")
        
    def read_csv(self,data):
        self.df = pd.read_csv(data)
        
    
class EDA_Dataframe_Analysis():

    
    def __init__(self):
        
        print("General_EDA object created")

    def describe(self,data):
        return data.describe()
    
    def colunas(self,data):
        return data.columns
    
    def aprovados(self,data):
        return data['verdict'].value_counts(normalize=True)
    
    def scatter(self,data,x):
        return sns.scatterplot(y='G_mean',x=x,data=data)
    
    def boxplot(self,data,x):
        return sns.boxplot(x=x,y="G_mean",data=data)
    
    def barplot(self,data,x):
        return sns.barplot(x=x,y="G_mean",data=data)
        
    def count(self,data,x):
        return sns.countplot(x=x, data = data, palette='rocket', saturation=0.9)
    
    def heat(self,data):
        numData = data._get_numeric_data()
        var_num_corr = numData.corr()
        f,ax = plt.subplots(figsize=(15, 15))
        return sns.heatmap(var_num_corr, ax=ax, annot=True)

def main():
    
    st.title("Análise exploratória de dados")
    
    if st.checkbox("Começar"):
        st.text("5 primeiras linhas do dataset")
        
        df = pd.read_csv(r'Student.csv')
  
        st.dataframe(df.head())
        st.success("Data Frame Loaded successfully")
        
        st.markdown('A coluna G_mean representa a média das 3 notas e a coluna verdict nos mostra se o aluno passou ou não de ano, se a média for (maior que 10 -- 1: Passou),  (menor que 10 -- 0: Reprovou)')
        if st.checkbox("Resumo estatístico"):
            st.write(dataframe.describe(df))

        if st.checkbox("Exibir todas as colunas"):
            st.write(dataframe.colunas(df))

        if st.checkbox(r"% de aprovados"):
            st.write(dataframe.aprovados(df))
            
        
        #! Tabulação
        st.subheader('Tabulação Cruzada') 
        all_columns_names = dataframe.colunas(df)
        all_columns_names1 = dataframe.colunas(df)        
        selected_columns_names = st.selectbox("Selecione a coluna 1 para tabulação cruzada",all_columns_names)
        selected_columns_names1 = st.selectbox("Selecione a coluna 2 para tabulação cruzada",all_columns_names1)
        
        if st.button("Gerar tabulação cruzada"):
            st.dataframe(pd.crosstab(df[selected_columns_names],df[selected_columns_names1]))
        st.subheader('Vamos criar gráficos comparativos com a média dos alunos')
        #! Disperção    
        st.subheader('Disperção')            
        occupation = st.selectbox("Selecione a coluna que fara o gráfico de disperção com a média das notas",dataframe.colunas(df))                        
        if st.button("Gerar Gráfico de Disperçao"):
            st.write(dataframe.scatter(data = df, x = occupation))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            
        #! Boxplot    
        st.subheader('Boxplot')      
        occupation = st.selectbox("Selecione a coluna que fara o gráfico Boxplot com a média das notas",dataframe.colunas(df))                
        if st.checkbox("Gerar Gráfico BoxPlot"):
            st.write(dataframe.boxplot(df, occupation))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        
        
        #! Barplot    
        st.subheader('Barplot')      
        occupation = st.selectbox("Selecione a coluna que fara o gráfico Barplot com a média das notas",dataframe.colunas(df))               
        if st.checkbox("Gerar Gráfico BarPlot"):
            st.write(dataframe.barplot(df, occupation))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            
            
        #! Contagem    
        st.subheader('Contagem')      
        occupation = st.selectbox("Selecione a coluna que fara o gráfico de contagem com a média das notas",dataframe.colunas(df))            
        if st.checkbox("Gerar Gráfico De Contagem"):
            st.write(dataframe.count(df, occupation))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        
        #! Gráfico de calor    
        st.subheader('Gráfico de calor')              
        if st.checkbox("Gerar Gráfico De Calor"):
            st.write(dataframe.heat(df))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()


                

load = DataFrame_Loader()
 
dataframe = EDA_Dataframe_Analysis()
 
main()
    