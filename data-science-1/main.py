#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[24]:


from IPython import get_ipython

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[3]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# In[4]:


# Sua análise da parte 1 começa aqui.
# verificando as informações do dataset
dataframe.info()


# In[5]:


# Verificando as primeiras linhas do dataset
dataframe.head()


# In[6]:


# Verificando se há dados nulos no dataset
dataframe.isna().sum()


# In[7]:


# Distribuição Gaussiana (normal)
normal = sct.norm.rvs(20, 4, size=10000) 
sns.distplot(normal);


# In[8]:


# Média e variância (normal)
(normal.mean(), normal.var())


# In[9]:


# Desvio Padrão (normal)
normal.std()


# In[10]:


# Distribuição Binomial
binomial = sct.binom.rvs(100, 0.2, size=10000)
plt.hist(binomial, density = True, bins = 50)
plt.show()


# In[11]:


# Média e a variância (binomial)
(binomial.mean(), binomial.var())


# In[12]:


# Verificando o desvio padrão (binominal)
binomial.std()


# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[13]:


def q1():
    # Retorne aqui o resultado da questão 1.
    normal = np.percentile(dataframe.normal, [25, 50, 75])
    binomial = np.percentile(dataframe.binomial, [25, 50, 75])
    return (round(normal[0]-binomial[0], 3),round(normal[1]-binomial[1], 3),round(normal[2]-binomial[2], 3))
q1()


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[14]:


def q2():
    #Distribuição acumulada empírica
    dist_empirica = ECDF(dataframe.normal)
    
    #Calculando a média
    media = dataframe.normal.mean()
    
    # Calculando o desvio padrão
    desvio_padrao = dataframe.normal.std()
    
    # Calculando os limites da fórmula
    limite_superior = dist_empirica(media + desvio_padrao)
    limite_inferior = dist_empirica(media - desvio_padrao)
    
    return float(np.round(limite_superior - limite_inferior, 3))

q2()


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[15]:


def q3():  
    # Calculando parâmetros para distribuição normal
    media_normal = dataframe.normal.mean()
    variancia_normal = dataframe.normal.var()
    
    # Calculando parâmetros para distribuição binomial
    media_binomial = dataframe.binomial.mean()
    variancia_binomial = dataframe.binomial.var()
    
    # Diferenças entre as médias
    dif_media = media_binomial - media_normal
    
    # Diferença entre as variâncias
    dif_variancia = variancia_binomial - variancia_normal
    
    resultado = (round( dif_media, 3), round(dif_variancia, 3))
    
    return tuple(resultado)

q3()


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[17]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[18]:


# Sua análise da parte 2 começa aqui.
#Verificando informações sobre o dataset
stars.info()


# In[19]:


# Visualizando as primeiras linhas do dataset
stars.head()


# In[20]:


# Verificando dados faltantes
stars.isna().sum()


# In[21]:


# Estatística descritiva do dataset
stars.describe()


# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[22]:


def q4():
    # Filtrando os dados
    nova_variavel = stars[stars['target'] == 0]['mean_profile']
    
    # Padronizando os dados para normal padrão
    false_pulsar_mean_profile_standardized = (nova_variavel - nova_variavel.mean())/nova_variavel.std()

    # Calculando a distribuição empirica
    dist_empirica = ECDF(false_pulsar_mean_profile_standardized)
    
    # Quantis na distribuicao normal
    quantis = sct.norm.ppf([.8, .9, .95])
    
    # Calculo de propabilidade
    return tuple(np.round(dist_empirica(quantis),3))
q4()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[23]:


def q5():
    # Quantis = 25, 50 e 75
    quantis = [.25, .5, .75]
    
    # Filtrando os dados
    nova_variavel = stars[stars['target'] == 0]['mean_profile']
    
    # Padronizando os dados para normal padrão
    false_pulsar_mean_profile_standardized = (nova_variavel - nova_variavel.mean())/nova_variavel.std()
    
    # Quantis da distribuição
    quantis_empiricos = false_pulsar_mean_profile_standardized.quantile(quantis)
    
    # Quantis teoricos
    quantis_teoricos = sct.norm.ppf(quantis)
    
    return tuple(np.round(quantis_empiricos - quantis_teoricos, 3))
    
q5()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.
