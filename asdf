import pandas as pd
import numpy as np
import math as math
import matplotlib.pyplot as plt
import os

os.makedirs('histograma')

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

def fazer_grafico(x,y,titulo,eixox,eixoy,nome):
  plt.scatter(x,y) #plotar o gráfico 
  plt.title (titulo) #título
  plt.xlabel(eixox) #título do eixo x
  plt.ylabel(eixoy) #título do eixo y
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

ro1x = (filtro_grupo1['dx'].mean()**2)
ro1y = (filtro_grupo1['dy'].mean()**2)
ro1z = (filtro_grupo1['dz'].mean()**2)

#Estimamos a a distância do Sol ao CG com a equação 7.
ro1 = (ro1x + ro1y + ro1z)**(1/2)
print('A componente x é {0:.2f}.\n'.format(ro1x),
      'A componente y é {0:.2f}.\n'.format(ro1y),
      'A componente z é {0:.2f}.\n'.format(ro1z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro1))

#Aplicamos as equações 4, 5 e 6 do roteiro de atividades para determinar
#o valor médio das componentes do vetor distância para o grupo 2.

ro2x = (filtro_grupo2['dx'].mean()**2)
ro2y = (filtro_grupo2['dy'].mean()**2)
ro2z = (filtro_grupo2['dz'].mean()**2)

#Estimamos a a distância do Sol ao CG com a equação 7.
ro2 = (ro2x + ro2y + ro2z)**(1/2)
print('A componente x é {0:.2f} kpc.\n'.format(ro2x),
      'A componente y é {0:.2f} kpc.\n'.format(ro2y),
      'A componente z é {0:.2f} kpc.\n'.format(ro2z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro2))

#Aplicamos as equações 4, 5 e 6 do roteiro de atividades para determinar
#o valor médio das componentes do vetor distância para o grupo 3.

ro3x = (filtro_grupo3['dx'].mean()**2)
ro3y = (filtro_grupo3['dy'].mean()**2)
ro3z = (filtro_grupo3['dz'].mean()**2)

#Estimamos a a distância do Sol ao CG com a equação 7.
ro3 = (ro3x + ro3y + ro3z)**(1/2)
print('A componente x é {0:.2f} kpc.\n'.format(ro3x),
      'A componente y é {0:.2f} kpc.\n'.format(ro3y),
      'A componente z é {0:.2f} kpc.\n'.format(ro3z),
    'A distância do Sol ao CG é {0:.2f} kpc.'.format(ro3))

def fazer_histograma(eixox, titulo, nomeeixox, nomegrafico):
  plt.hist(eixox, bins=range(-100,100,2))
  plt.title(titulo)
  plt.xlabel(nomeeixox)
  plt.ylabel('Aglomerados')
  plt.savefig('histograma/'+nomegrafico)

histogramadx1 = fazer_histograma(filtro_grupo1['dx'], 'histograma grupo 1', 'dx', 'hist_grupo1_dx.png')

histogramady1 = fazer_histograma(filtro_grupo1['dy'], 'histograma grupo 1', 'dy', 'hist_grupo1_dy.png')

histogramadz1 = fazer_histograma(filtro_grupo1['dz'], 'histograma grupo 1', 'dz', 'hist_grupo1_dz.png')

histogramadx2 = fazer_histograma(filtro_grupo2['dx'], 'histograma grupo 2', 'dx', 'hist_grupo2_dx.png')

histogramady2 = fazer_histograma(filtro_grupo2['dy'], 'histograma grupo 2', 'dy', 'hist_grupo2_dy.png')

histogramadz2 = fazer_histograma(filtro_grupo2['dz'], 'histograma grupo 2', 'dz', 'hist_grupo2_dz.png')

histogramadx3 = fazer_histograma(filtro_grupo3['dx'], 'histograma grupo 3', 'dx', 'hist_grupo3_dx.png')

histogramady3 = fazer_histograma(filtro_grupo3['dy'], 'histograma grupo 3', 'dy', 'hist_grupo3_dy.png')

histogramadz3 = fazer_histograma(filtro_grupo3['dz'], 'histograma grupo 3', 'dz', 'hist_grupo3_dz.png')
