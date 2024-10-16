import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')


df_xadrez = pd.read_csv('C:/Users/deivid/OneDrive - grupotorino.com.br/Documentos/Pythons/Xadrez/games/games.csv')

xadrez= pd.DataFrame(df_xadrez.drop(columns=['rated','created_at','last_move_at','increment_code','white_id','black_id','opening_ply'], inplace=False))

partidas= xadrez['winner'].value_counts()
total_partidas = partidas.sum()

porc_white = 100*(partidas["white"] /total_partidas)
porc_black =100*(partidas["black"] /total_partidas)
porc_draw =100*(partidas["draw"] /total_partidas)

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len([partidas['white'],partidas["draw"],partidas["black"] ])))

fig, ax = plt.subplots()
ax.pie([partidas['white'],partidas["draw"],partidas["black"] ], colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))


#print(total_partidas)
#print(porc_black,porc_draw,porc_white)

aberturas_jogadas=xadrez['opening_name'].value_counts()

partida_abertura = xadrez[['winner','opening_name']].value_counts().sort_values(ascending=False)

partida_black = xadrez[xadrez['winner']=='black']
partida_black =partida_black.drop(columns=['id','moves','opening_eco'], inplace=False).sort_values(by=['black_rating'],ascending=False)
partida_black_geral = partida_black.drop(columns=['turns','victory_status','white_rating','black_rating']).value_counts()
status_black=partida_black['victory_status'].value_counts()
#print(status_black)


partida_white = xadrez[xadrez['winner']=='white']
partida_white =partida_white.drop(columns=['id','moves','opening_eco'], inplace=False).sort_values(by=['white_rating'],ascending=False)
partida_white_geral = partida_white.drop(columns=['turns','victory_status','white_rating','black_rating']).value_counts()
status_white=partida_white['victory_status'].value_counts()

partida_draw = xadrez[xadrez['winner']=='draw']
partida_draw =partida_draw.drop(columns=['id','moves','opening_eco'], inplace=False).sort_values(by=['white_rating','black_rating'],ascending=False)
partida_draw_geral = partida_draw.drop(columns=['turns','victory_status','white_rating','black_rating']).value_counts()



arquivoExcel = pd.ExcelWriter(f'AnaliseXadrez.xlsx',engine="xlsxwriter")
partida_draw_geral.to_excel(arquivoExcel,sheet_name='Partidas_Gerais_Draw',index=True)
partida_draw.to_excel(arquivoExcel,sheet_name='Partidas_Draw',index=True)
partida_white_geral.to_excel(arquivoExcel,sheet_name='Partidas_Gerais_White',index=True)
partida_white.to_excel(arquivoExcel,sheet_name='Partidas_White',index=True)
partida_black_geral.to_excel(arquivoExcel,sheet_name='Partidas_Gerais_Black',index=True)
partida_black.to_excel(arquivoExcel,sheet_name='Partidas_Black',index=True)
partidas.to_excel(arquivoExcel,sheet_name='Partidas',index=True)
partida_abertura.to_excel(arquivoExcel,sheet_name='Partidas_Abertura',index=True)
arquivoExcel.close()

plt.show()
