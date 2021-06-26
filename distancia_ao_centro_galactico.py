import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt
import os
import statistics as estat
from scipy.stats import norm

os.makedirs('histograma')
os.makedirs('histograma_gaussiana')
os.makedirs('metalicidade')

def leitura(nomearquivo):
  arquivo = pd.read_csv(nomearquivo)

  df_test = pd.DataFrame(arquivo)

  df_test.head()

  return df_test

#Primeiramente vamos fazer 3 gráficos latitude galáctica x metalicidade;
#Os grupos serão classificados da seguinte forma:
#grupo 1: todos os aglomerados
#grupo 2: aglomerados com metalicidade menor ou igual a -1,2 
#grupo 3: aglomerados com metalicidade maior que -1,2

planilha1 = leitura('Todos_os_valores.csv')

#aplicamos a equação 1; 2 e 3 e adicionamos os valores encontrados ao Dataframe
rad = np.pi/180

planilha1['dx'] = np.cos((planilha1['B'])*rad)*planilha1['R_Sun']*np.cos((planilha1['L'])*rad)
planilha1['dy'] = np.cos((planilha1['B'])*rad)*planilha1['R_Sun']*np.sin((planilha1['L'])*rad)
planilha1['dz'] = np.sin((planilha1['B'])*rad)*planilha1['R_Sun']

#criamos um filtro para selecionar os grupos 1; 2 e 3
filtro_grupo1 = planilha1
filtro_grupo2 = planilha1[planilha1['[Fe/H]'] <= -1.2]
filtro_grupo3 = planilha1[planilha1['[Fe/H]'] > -1.2]

def fazer_grafico(x,y,titulo,nomeeixox,nomeeixoy,nome):
  plt.scatter(x,y) #plotar o gráfico 
  plt.title (titulo) #título
  plt.xlabel(nomeeixox) #título do eixo x
  plt.ylabel(nomeeixoy) #título do eixo y
  plt.savefig(nome,format='png')
  plt.show()

#fazer o gráfico

eixo_x_grupo1 = filtro_grupo1['dz']
eixo_y_grupo1 = filtro_grupo1['[Fe/H]']

grupo1 = fazer_grafico(eixo_x_grupo1, eixo_y_grupo1,
                       'módulo de B X metalicidade\n grupo 1', 'dz',
                       'metalicidade [Fe/H]', 'grafico_grupo1.png')

#fazer o gráfico

eixo_x_grupo2 = filtro_grupo2['dz']
eixo_y_grupo2 = filtro_grupo2['[Fe/H]']

grupo2 = fazer_grafico(eixo_x_grupo2, eixo_y_grupo2,
                       'módulo de B X metalicidade\n grupo 2', 'dz',
                       'metalicidade [Fe/H]', 'grafico_grupo2.png')

#fazer o gráfico

eixo_x_grupo3 = filtro_grupo3['dz']
eixo_y_grupo3 = filtro_grupo3['[Fe/H]']

grupo3 = fazer_grafico(eixo_x_grupo3, eixo_y_grupo3,
                       'módulo de B X metalicidade\n grupo3', 'dz',
                       'metalicidade [Fe/H]', 'grafico_grupo3.png')

#Aplicamos as equações 4, 5 e 6 do roteiro de atividades para determinar
#o valor médio das componentes do vetor distância para o grupo 1.

ro1x = filtro_grupo1['dx'].mean()
ro1y = filtro_grupo1['dy'].mean()
ro1z = filtro_grupo1['dz'].mean()

#Estimamos a a distância do Sol ao CG com a equação 7.
ro1 = (ro1x**2 + ro1y**2 + ro1z**2)**(1/2)
print('A componente x é {0:.2f}.\n'.format(ro1x),
      'A componente y é {0:.2f}.\n'.format(ro1y),
      'A componente z é {0:.2f}.\n'.format(ro1z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro1))

#Aplicamos as equações 4, 5 e 6 do roteiro de atividades para determinar
#o valor médio das componentes do vetor distância para o grupo 2.

ro2x = filtro_grupo2['dx'].mean()
ro2y = filtro_grupo2['dy'].mean()
ro2z = filtro_grupo2['dz'].mean()

#Estimamos a a distância do Sol ao CG com a equação 7.
ro2 = (ro2x**2 + ro2y**2 + ro2z**2)**(1/2)
print('A componente x é {0:.2f} kpc.\n'.format(ro2x),
      'A componente y é {0:.2f} kpc.\n'.format(ro2y),
      'A componente z é {0:.2f} kpc.\n'.format(ro2z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro2))

#Aplicamos as equações 4, 5 e 6 do roteiro de atividades para determinar
#o valor médio das componentes do vetor distância para o grupo 3.

ro3x = filtro_grupo3['dx'].mean()
ro3y = filtro_grupo3['dy'].mean()
ro3z = filtro_grupo3['dz'].mean()

#Estimamos a a distância do Sol ao CG com a equação 7.
ro3 = (ro3x**2 + ro3y**2 + ro3z**2)**(1/2)
print('A componente x é {0:.2f} kpc.\n'.format(ro3x),
      'A componente y é {0:.2f} kpc.\n'.format(ro3y),
      'A componente z é {0:.2f} kpc.\n'.format(ro3z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro3))

def fazer_histograma(eixox, min, max, titulo, nomeeixox, nomegrafico):
  plt.hist(eixox, bins=range(min,max,2))
  plt.title(titulo)
  plt.xlabel(nomeeixox)
  plt.ylabel('Aglomerados')
  plt.savefig('histograma/'+nomegrafico)

def fazer_gaussiana(eixox, min, max, titulo, nomeeixox, nomegrafico):
  plt.hist(eixox, bins=range(min,max,2), density = True)
  plt.title(titulo)
  plt.xlabel(nomeeixox)
  plt.ylabel('Aglomerados')
  media = estat.mean(eixox)
  desvio = estat.pstdev(eixox)
  xmim, xmax = plt.xlim()
  eixo = np.linspace(xmim,xmax,1000)
  eixoy = norm.pdf(eixo,media,desvio)
  plt.plot(eixo,eixoy)
  plt.savefig('histograma_gaussiana/'+nomegrafico)

#Fizemos um histograma para cada direção de cada grupo e também um histograma
#com aplicação de uma gaussiana.

hist_grupo1x = fazer_histograma(filtro_grupo1['dx'], -100, 100,
                                'Histograma grupo1', 'dx', 'hist_grupo1_dx.png')

#histograma com gaussiana grupo 1 dx
histgaus_grupo1x = fazer_gaussiana(filtro_grupo1['dx'], -100, 100,
                                'Histograma grupo1', 'dx', 'gaus_grupo1_dx.png')

#histograma grupo 1 dy
hist_grupo1y = fazer_histograma(filtro_grupo1['dy'], -100, 100,
                                'Histograma grupo1', 'dy', 'hist_grupo1_dy.png')

#histograma com gaussiana grupo 1 dy
histgaus_grupo1y = fazer_gaussiana(filtro_grupo1['dy'], -100, 100,
                                'Histograma grupo1', 'dy', 'gaus_grupo1_dy.png')

#histograma grupo 1 dz
hist_grupo1z = fazer_histograma(filtro_grupo1['dz'], -100, 100,
                                'Histograma grupo1', 'dz', 'hist_grupo1_dz.png')

#histograma com gaussiana grupo 1 dz
histgaus_grupo1z = fazer_gaussiana(filtro_grupo1['dz'], -100, 100,
                                'Histograma grupo1', 'dz', 'gaus_grupo1_dz.png')

#histograma grupo 2 dx
hist_grupo2x = fazer_histograma(filtro_grupo2['dx'], -100, 100,
                                'Histograma grupo2', 'dx', 'hist_grupo2_dx.png')

#histograma com gaussiana grupo 2 dx
histgaus_grupo2x = fazer_gaussiana(filtro_grupo2['dx'], -100, 100,
                                'Histograma grupo2', 'dx', 'gaus_grupo2_dx.png')

#histograma grupo 2 dy
hist_grupo2y = fazer_histograma(filtro_grupo2['dy'], -100, 100,
                                'Histograma grupo2', 'dy', 'hist_grupo2_dy.png')

#histograma com gaussiana grupo 2 dy
histgaus_grupo2y = fazer_gaussiana(filtro_grupo2['dy'], -100, 100,
                                'Histograma grupo2', 'dy', 'gaus_grupo2_dy.png')

#histograma grupo 2 dz
hist_grupo2z = fazer_histograma(filtro_grupo2['dz'], -100, 100,
                                'Histograma grupo2', 'dz', 'hist_grupo2_dz.png')


#histograma com gaussiana grupo 2 dz
histgaus_grupo2z = fazer_gaussiana(filtro_grupo2['dz'], -100, 100,
                                'Histograma grupo2', 'dz', 'gaus_grupo2_dz.png')

#histograma grupo 3 dx
hist_grupo3x = fazer_histograma(filtro_grupo3['dx'], -30, 30,
                                'Histograma grupo3', 'dx', 'hist_grupo3_dx.png')

#histograma com gaussiana grupo 3 dx
histgaus_grupo3x = fazer_gaussiana(filtro_grupo3['dx'], -30, 30,
                                'Histograma grupo3', 'dx', 'gaus_grupo3_dx.png')

#histograma grupo 3 dy
hist_grupo3y = fazer_histograma(filtro_grupo3['dy'], -30, 30,
                                'Histograma grupo3', 'dy', 'hist_grupo3_dy.png')

#histograma com gaussiana grupo 3 dy
histgaus_grupo3y = fazer_gaussiana(filtro_grupo3['dy'], -30, 30,
                                'Histograma grupo3', 'dy', 'gaus_grupo3_dy.png')

#histograma grupo 3 dz
hist_grupo3z = fazer_histograma(filtro_grupo3['dz'], -30, 30,
                                'Histograma grupo3', 'dz', 'hist_grupo3_dz.png')

#histograma com gaussiana grupo 3 dz
histgaus_grupo3z = fazer_gaussiana(filtro_grupo3['dz'], -30, 30,
                                'Histograma grupo3', 'dz', 'gaus_grupo3_dz.png')

def distanciaCG(r_o, d, b, l):
  R = (d**2 + r_o**2 + 2*r_o*d*np.cos(b)*np.cos(l))**0.5
  return R

#Aplicamos a equação 8 do trabalho e adicionamos uma nova coluna ao
#dataframe que contém a nova informação que é a distância do AG ao CG

filtro_grupo1['R'] = distanciaCG(ro1, filtro_grupo1['R_Sun'],
                                filtro_grupo1['B'], filtro_grupo1['L'])
filtro_grupo2['R'] = distanciaCG(ro2, filtro_grupo2['R_Sun'],
                                 filtro_grupo2['B'], filtro_grupo2['L'])
filtro_grupo3['R'] = distanciaCG(ro3, filtro_grupo3['R_Sun'],
                                 filtro_grupo3['B'], filtro_grupo3['L'])

#fazer o gráfico de metalicidade por R

metalicidade_grupo1 = fazer_grafico(filtro_grupo1['R'], filtro_grupo1['[Fe/H]'],
                                    'Gráfico metalicidade x distância AGCG\ngrupo 1',
                                    'Metalicidade [Fe/H]', 'distância R',
                                    'metalicidade/grafico_metalicidade_grupo1.png')

metalicidade_grupo2 = fazer_grafico(filtro_grupo2['R'], filtro_grupo2['[Fe/H]'],
                                    'Gráfico metalicidade x distância AGCG\ngrupo 2',
                                    'Metalicidade [Fe/H]', 'distância R',
                                    'metalicidade/grafico_metalicidade_grupo2.png')

metalicidade_grupo3 = fazer_grafico(filtro_grupo3['R'], filtro_grupo3['[Fe/H]'],
                                    'Gráfico metalicidade x distância AGCG\ngrupo 3',
                                    'Metalicidade [Fe/H]', 'distância R',
                                    'metalicidade/grafico_metalicidade_grupo3.png')
