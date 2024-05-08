import networkx as nx
from operator import itemgetter, attrgetter
G = nx.Graph()
G.add_node("Aguinaldo Silva")
G.add_node("Gloria Perez")
G.add_node("João Emanuel Carneiro")
G.add_node("Chay Suede")
G.add_node("Alexandre Nero")
G.add_node("Adriana Biroli")
G.add_node("Lilia Cabral")
G.add_node("Caio Blat")
G.add_node("Elizangela")
G.add_node("Nanda Costa")
G.add_node("José Mayer")
G.add_node("Malvino Salvador")
G.add_node("Gabriel Pelícia")
G.add_node("Caio Castro")
G.add_node("Sophie Charlotte")
G.add_node("Totia Meireles")
G.add_node("Renata Sorrah")
G.add_node("Eva Wilma")
G.add_node("Dira Paes")
G.add_node("Dalton Vigh")
G.add_node("Carolina Dieckmann")
G.add_node("Rodrigo Lombardi")
G.add_node("Nanda Costa")
G.add_node("Claudia Raia")
G.add_node("Vera Fischer")
G.add_node("André Gonçalves")
G.add_node("Letícia Spiller")
G.add_node("Stênio Garcia")
G.add_node("Juliana Paes")
G.add_node("Emilio Dantas")
G.add_node("Gabriel Almeida Bravo")
G.add_node("Paolla Oliveira")
G.add_node("Débora Falabella")
G.add_node("Adriana Esteves")
G.add_node("Murilo Benício")
G.add_node("Cauã Reymond")
G.add_node("Alexandre Borges")
G.add_node("Débora Bloch")
G.add_node("Juca de Oliveira")
G.add_node("Tony Ramos")
G.add_edges_from([("Aguinaldo Silva", "Chay Suede"),("Aguinaldo Silva", "Alexandre Nero"),("Aguinaldo Silva", "Adriana Biroli"),("Aguinaldo Silva", "Lilia Cabral"),("Aguinaldo Silva", "Caio Blat"),("Aguinaldo Silva", "Elizangela"),("Aguinaldo Silva", "Nanda Costa"),("Aguinaldo Silva", "José Mayer"),("Aguinaldo Silva", "Malvino Salvador"),("Aguinaldo Silva","Gabriel Pelícia"), ("Aguinaldo Silva","Caio Castro"), ("Aguinaldo Silva","Sophie Charlotte"), ("Aguinaldo Silva","Totia Meireles"), ("Aguinaldo Silva","Renata Sorrah"), ("Aguinaldo Silva","Eva Wilma"), ("Aguinaldo Silva","Dira Paes"), ("Aguinaldo Silva","Dalton Vigh"), ("Aguinaldo Silva","Carolina Dieckmann"),("CHAY SUEDE","ALEXANDRE NERO"),
("CHAY SUEDE","ADRIANA BIROLI"),
("CHAY SUEDE","LILIA CABRAL"),
("CHAY SUEDE","CAIO BLAT"),
("CHAY SUEDE","ELIZANGELA"),
("CHAY SUEDE","NANDA COSTA"),
("CHAY SUEDE","JOSÉ MAYER"),
("ALEXANDRE NERO","ADRIANA BIROLI"),
("ALEXANDRE NERO","LILIA CABRAL"),
("ALEXANDRE NERO","CAIO BLAT"),
("ALEXANDRE NERO","ELIZANGELA"),
("ALEXANDRE NERO","NANDA COSTA"),
("ALEXANDRE NERO","JOSÉ MAYER"),
("ADRIANA BIROLI","LILIA CABRAL"),
("ADRIANA BIROLI","CAIO BLAT"),
("ADRIANA BIROLI","ELIZANGELA"),
("ADRIANA BIROLI","NANDA COSTA"),
("ADRIANA BIROLI","JOSÉ MAYER"),("LILIA CABRAL","MALVINO SALVADOR"),
("LILIA CABRAL","GABRIEL PELÍCIA"),
("LILIA CABRAL","CAIO CASTRO"),
("LILIA CABRAL","SOPHIE CHARLOTTE"),
("LILIA CABRAL","TOTIA MEIRELES"),
("LILIA CABRAL","RENATA SORRAH"),
("LILIA CABRAL","JOSÉ MAYER"),
("LILIA CABRAL","EVA WILMA"),
("LILIA CABRAL","DIRA PAES"),
("LILIA CABRAL","DALTON VIGH"),
("LILIA CABRAL","CAROLINA DIECKMANN"),
("LILIA CABRAL","ALEXANDRE NERO"),
("MALVINO SALVADOR","GABRIEL PELÍCIA"),
("MALVINO SALVADOR","CAIO CASTRO"),
("MALVINO SALVADOR","SOPHIE CHARLOTTE"),
("MALVINO SALVADOR","TOTIA MEIRELES"),
("MALVINO SALVADOR","RENATA SORRAH"),
("MALVINO SALVADOR","JOSÉ MAYER"),
("MALVINO SALVADOR","EVA WILMA"),
("MALVINO SALVADOR","DIRA PAES"),
("MALVINO SALVADOR","DALTON VIGH"),
("MALVINO SALVADOR","CAROLINA DIECKMANN"),
("MALVINO SALVADOR","ALEXANDRE NERO"),
("GABRIEL PELÍCIA","CAIO CASTRO"),
("GABRIEL PELÍCIA","SOPHIE CHARLOTTE"),
("GABRIEL PELÍCIA","TOTIA MEIRELES"),
("GABRIEL PELÍCIA","RENATA SORRAH"),
("GABRIEL PELÍCIA","JOSÉ MAYER"),
("GABRIEL PELÍCIA","EVA WILMA"),
("GABRIEL PELÍCIA","DIRA PAES"),
("GABRIEL PELÍCIA","DALTON VIGH"),
("GABRIEL PELÍCIA","CAROLINA DIECKMANN"),
("GABRIEL PELÍCIA","ALEXANDRE NERO"),
("CAIO CASTRO","SOPHIE CHARLOTTE"),
("CAIO CASTRO","TOTIA MEIRELES"),
("CAIO CASTRO","RENATA SORRAH"),
("CAIO CASTRO","JOSÉ MAYER"),
("CAIO CASTRO","EVA WILMA"),
("CAIO CASTRO","DIRA PAES"),
("CAIO CASTRO","DALTON VIGH"),
("CAIO CASTRO","CAROLINA DIECKMANN"),
("CAIO CASTRO","ALEXANDRE NERO"),
("SOPHIE CHARLOTTE","TOTIA MEIRELES"),
("SOPHIE CHARLOTTE","RENATA SORRAH"),
("SOPHIE CHARLOTTE","JOSÉ MAYER"),
("SOPHIE CHARLOTTE","EVA WILMA"),
("SOPHIE CHARLOTTE","DIRA PAES"),
("SOPHIE CHARLOTTE","DALTON VIGH"),
("SOPHIE CHARLOTTE","CAROLINA DIECKMANN"),
("SOPHIE CHARLOTTE","ALEXANDRE NERO"),
("TOTIA MEIRELES","RENATA SORRAH"),
("TOTIA MEIRELES","JOSÉ MAYER"),
("TOTIA MEIRELES","EVA WILMA"),
("TOTIA MEIRELES","DIRA PAES"),
("TOTIA MEIRELES","DALTON VIGH"),
("TOTIA MEIRELES","CAROLINA DIECKMANN"),
("TOTIA MEIRELES","ALEXANDRE NERO"),
("RENATA SORRAH","JOSÉ MAYER"),
("RENATA SORRAH","EVA WILMA"),
("RENATA SORRAH","DIRA PAES"),
("RENATA SORRAH","DALTON VIGH"),
("RENATA SORRAH","CAROLINA DIECKMANN"),
("RENATA SORRAH","ALEXANDRE NERO"),
("JOSÉ MAYER","EVA WILMA"),
("JOSÉ MAYER","DIRA PAES"),
("JOSÉ MAYER","DALTON VIGH"),
("JOSÉ MAYER","CAROLINA DIECKMANN"),
("JOSÉ MAYER","ALEXANDRE NERO"),
("EVA WILMA","DIRA PAES"),
("EVA WILMA","DALTON VIGH"),
("EVA WILMA","CAROLINA DIECKMANN"),
("EVA WILMA","ALEXANDRE NERO"),
("DIRA PAES","DALTON VIGH"),
("DIRA PAES","CAROLINA DIECKMANN"),
("DIRA PAES","ALEXANDRE NERO"),
("DALTON VIGH","CAROLINA DIECKMANN"),
("DALTON VIGH","ALEXANDRE NERO"),
("CAROLINA DIECKMANN","ALEXANDRE NERO")])
G.add_edges_from([("Gloria Perez", "Rodrigo Lombardi"), ("Gloria Perez","Nanda Costa"), ("Gloria Perez","Dira Paes"), ("Gloria Perez","Totia Meireles"), ("Gloria Perez","Claudia Raia"), ("Gloria Perez","Vera Fischer"), ("Gloria Perez","André Gonçalves"), ("Gloria Perez","Letícia Spiller"), ("Gloria Perez","Elizangela"), ("Gloria Perez","Stênio Garcia"), ("Gloria Perez","Carolina Dieckmann"), ("Gloria Perez","Dalton Vigh"), ("Gloria Perez","Juliana Paes"), ("Gloria Perez","Emilio Dantas"), ("Gloria Perez","Gabriel Almeida Bravo"), ("Gloria Perez","Paolla Oliveira"), ("Gloria Perez","Lilia Cabral"), ("Gloria Perez","Débora Falabella"),("RODRIGO LOMBARDI","NANDA COSTA"),
("RODRIGO LOMBARDI","DIRA PAES"),
("RODRIGO LOMBARDI","TOTIA MEIRELES"),
("RODRIGO LOMBARDI","CLAUDIA RAIA"),
("RODRIGO LOMBARDI","VERA FISCHER"),
("RODRIGO LOMBARDI","ANDRÉ GONÇALVES"),
("RODRIGO LOMBARDI","LETÍCIA SPILLER"),
("RODRIGO LOMBARDI","ELIZANGELA"),
("RODRIGO LOMBARDI","STÊNIO GARCIA"),
("RODRIGO LOMBARDI","CAROLINA DIECKMANN"),
("RODRIGO LOMBARDI","DALTON VIGH"),
("NANDA COSTA","DIRA PAES"),
("NANDA COSTA","TOTIA MEIRELES"),
("NANDA COSTA","CLAUDIA RAIA"),
("NANDA COSTA","VERA FISCHER"),
("NANDA COSTA","ANDRÉ GONÇALVES"),
("NANDA COSTA","LETÍCIA SPILLER"),
("NANDA COSTA","ELIZANGELA"),
("NANDA COSTA","STÊNIO GARCIA"),
("NANDA COSTA","CAROLINA DIECKMANN"),
("NANDA COSTA","DALTON VIGH"),
("DIRA PAES","TOTIA MEIRELES"),
("DIRA PAES","CLAUDIA RAIA"),
("DIRA PAES","VERA FISCHER"),
("DIRA PAES","ANDRÉ GONÇALVES"),
("DIRA PAES","LETÍCIA SPILLER"),
("DIRA PAES","ELIZANGELA"),
("DIRA PAES","STÊNIO GARCIA"),
("DIRA PAES","CAROLINA DIECKMANN"),
("DIRA PAES","DALTON VIGH"),
("TOTIA MEIRELES","CLAUDIA RAIA"),
("TOTIA MEIRELES","VERA FISCHER"),
("TOTIA MEIRELES","ANDRÉ GONÇALVES"),
("TOTIA MEIRELES","LETÍCIA SPILLER"),
("TOTIA MEIRELES","ELIZANGELA"),
("TOTIA MEIRELES","STÊNIO GARCIA"),
("TOTIA MEIRELES","CAROLINA DIECKMANN"),
("TOTIA MEIRELES","DALTON VIGH"),
("CLAUDIA RAIA","VERA FISCHER"),
("CLAUDIA RAIA","ANDRÉ GONÇALVES"),
("CLAUDIA RAIA","LETÍCIA SPILLER"),
("CLAUDIA RAIA","ELIZANGELA"),
("CLAUDIA RAIA","STÊNIO GARCIA"),
("CLAUDIA RAIA","CAROLINA DIECKMANN"),
("CLAUDIA RAIA","DALTON VIGH"),
("VERA FISCHER","ANDRÉ GONÇALVES"),
("VERA FISCHER","LETÍCIA SPILLER"),
("VERA FISCHER","ELIZANGELA"),
("VERA FISCHER","STÊNIO GARCIA"),
("VERA FISCHER","CAROLINA DIECKMANN"),
("VERA FISCHER","DALTON VIGH"),
("ANDRÉ GONÇALVES","LETÍCIA SPILLER"),
("ANDRÉ GONÇALVES","ELIZANGELA"),
("ANDRÉ GONÇALVES","STÊNIO GARCIA"),
("ANDRÉ GONÇALVES","CAROLINA DIECKMANN"),
("ANDRÉ GONÇALVES","DALTON VIGH"),
("LETÍCIA SPILLER","ELIZANGELA"),
("LETÍCIA SPILLER","STÊNIO GARCIA"),
("LETÍCIA SPILLER","CAROLINA DIECKMANN"),
("LETÍCIA SPILLER","DALTON VIGH"),
("ELIZANGELA","STÊNIO GARCIA"),
("ELIZANGELA","CAROLINA DIECKMANN"),
("ELIZANGELA","DALTON VIGH"),
("STÊNIO GARCIA","CAROLINA DIECKMANN"),
("STÊNIO GARCIA","DALTON VIGH"),
("CAROLINA DIECKMANN","DALTON VIGH"),("JULIANA PAES","RODRIGO LOMBARDI "),
("JULIANA PAES","EMILIO DANTAS "),
("JULIANA PAES","GABRIEL ALMEIDA BRAVO"),
("JULIANA PAES","PAOLLA OLIVEIRA"),
("JULIANA PAES","TOTIA MEIRELES"),
("JULIANA PAES","LILIA CABRAL"),
("JULIANA PAES","ELIZANGELA"),
("JULIANA PAES","DÉBORA FALABELLA"),
("RODRIGO LOMBARDI ","EMILIO DANTAS "),
("RODRIGO LOMBARDI ","GABRIEL ALMEIDA BRAVO"),
("RODRIGO LOMBARDI ","PAOLLA OLIVEIRA"),
("RODRIGO LOMBARDI ","TOTIA MEIRELES"),
("RODRIGO LOMBARDI ","LILIA CABRAL"),
("RODRIGO LOMBARDI ","ELIZANGELA"),
("RODRIGO LOMBARDI ","DÉBORA FALABELLA"),
("EMILIO DANTAS ","GABRIEL ALMEIDA BRAVO"),
("EMILIO DANTAS ","PAOLLA OLIVEIRA"),
("EMILIO DANTAS ","TOTIA MEIRELES"),
("EMILIO DANTAS ","LILIA CABRAL"),
("EMILIO DANTAS ","ELIZANGELA"),
("EMILIO DANTAS ","DÉBORA FALABELLA"),
("GABRIEL ALMEIDA BRAVO","PAOLLA OLIVEIRA"),
("GABRIEL ALMEIDA BRAVO","TOTIA MEIRELES"),
("GABRIEL ALMEIDA BRAVO","LILIA CABRAL"),
("GABRIEL ALMEIDA BRAVO","ELIZANGELA"),
("GABRIEL ALMEIDA BRAVO","DÉBORA FALABELLA"),
("PAOLLA OLIVEIRA","TOTIA MEIRELES"),
("PAOLLA OLIVEIRA","LILIA CABRAL"),
("PAOLLA OLIVEIRA","ELIZANGELA"),
("PAOLLA OLIVEIRA","DÉBORA FALABELLA"),
("TOTIA MEIRELES","LILIA CABRAL"),
("TOTIA MEIRELES","ELIZANGELA"),
("TOTIA MEIRELES","DÉBORA FALABELLA"),
("LILIA CABRAL","ELIZANGELA"),
("LILIA CABRAL","DÉBORA FALABELLA"),
("ELIZANGELA","DÉBORA FALABELLA")])
G.add_edges_from([("João Emanuel Carneiro","Débora Falabella"), ("João Emanuel Carneiro","Adriana Esteves"), ("João Emanuel Carneiro","Murilo Benício"), ("João Emanuel Carneiro","Cauã Reymond"), ("João Emanuel Carneiro","Alexandre Borges"), ("João Emanuel Carneiro","Débora Bloch"), ("João Emanuel Carneiro","Tony Ramos"), ("João Emanuel Carneiro","Juca de Oliveira"),("DÉBORA FALABELLA","ADRIANA ESTEVES"),
("DÉBORA FALABELLA","MURILO BENÍCIO"),
("DÉBORA FALABELLA","CAUÃ REYMOND"),
("DÉBORA FALABELLA","ALEXANDRE BORGES"),
("DÉBORA FALABELLA","DÉBORA BLOCH"),
("DÉBORA FALABELLA","MURILO BENÍCIO"),
("DÉBORA FALABELLA","TONY RAMOS"),
("DÉBORA FALABELLA","JUCA DE OLIVEIRA"),
("ADRIANA ESTEVES","MURILO BENÍCIO"),
("ADRIANA ESTEVES","CAUÃ REYMOND"),
("ADRIANA ESTEVES","ALEXANDRE BORGES"),
("ADRIANA ESTEVES","DÉBORA BLOCH"),
("ADRIANA ESTEVES","MURILO BENÍCIO"),
("ADRIANA ESTEVES","TONY RAMOS"),
("ADRIANA ESTEVES","JUCA DE OLIVEIRA"),
("MURILO BENÍCIO","CAUÃ REYMOND"),
("MURILO BENÍCIO","ALEXANDRE BORGES"),
("MURILO BENÍCIO","DÉBORA BLOCH"),
("MURILO BENÍCIO","MURILO BENÍCIO"),
("MURILO BENÍCIO","TONY RAMOS"),
("MURILO BENÍCIO","JUCA DE OLIVEIRA"),
("CAUÃ REYMOND","ALEXANDRE BORGES"),
("CAUÃ REYMOND","DÉBORA BLOCH"),
("CAUÃ REYMOND","MURILO BENÍCIO"),
("CAUÃ REYMOND","TONY RAMOS"),
("CAUÃ REYMOND","JUCA DE OLIVEIRA"),
("ALEXANDRE BORGES","DÉBORA BLOCH"),
("ALEXANDRE BORGES","MURILO BENÍCIO"),
("ALEXANDRE BORGES","TONY RAMOS"),
("ALEXANDRE BORGES","JUCA DE OLIVEIRA"),
("DÉBORA BLOCH","MURILO BENÍCIO"),
("DÉBORA BLOCH","TONY RAMOS"),
("DÉBORA BLOCH","JUCA DE OLIVEIRA"),
("MURILO BENÍCIO","TONY RAMOS"),
("MURILO BENÍCIO","JUCA DE OLIVEIRA"),
("TONY RAMOS","JUCA DE OLIVEIRA")])
import matplotlib.pyplot as plt
plt.figure(1)
nx.draw(G, with_labels=True)
centralidade_grau = nx.degree_centrality(G)
nx.set_node_attributes(G, centralidade_grau, 'betweenness')
Classificação = sorted(centralidade_grau.items(), key=itemgetter(1), reverse=True)
print("Centralidade de Grau Top 10:")
for b in Classificação[:10]:
    print(b,'\n')
Proximidade = nx.closeness_centrality(G)
nx.set_node_attributes(G, Proximidade, 'proximidade')
Classificação = sorted(Proximidade.items(), key=itemgetter(1), reverse=True)
print("Centralidade de Proximidade Top 10:")
for b in Classificação[:10]:
    print(b,'\n')
Betweenness = nx.betweenness_centrality(G)
nx.set_node_attributes(G, Betweenness, 'betweenness')
Classificação = sorted(Betweenness.items(), key=itemgetter(1), reverse=True)
print("Centralidade de Betweenness Top 10:")
for b in Classificação[:10]:
    print(b,'\n')
Autovetor = nx.eigenvector_centrality(G)
nx.set_node_attributes(G, Autovetor, 'Autovetor')
Classificação = sorted(Autovetor.items(), key=itemgetter(1), reverse=True)
print("Centralidade de Auto Vetor Top 10:")
for b in Classificação[:10]:
    print(b,'\n')
print("Assortavidade: ", nx.degree_assortativity_coefficient(G),'\n')
transitividade = nx.transitivity(G)
print("Coeficiente de Agrupamento: ", transitividade,'\n')
clusterização = nx.clustering(G)
print("clusterização: ", clusterização,'\n')