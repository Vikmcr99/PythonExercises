tabela = ('Fluminense', 'Vasco', 'Flamengo', 'Botafogo','Santos','Sao Paulo', 'Corinthians', 'Palmeiras', 'Galo',
          'Cruzeiro','Red Bull', 'Bahia', 'Chape','Inter','Gremio','Fortaleza','CAP','Juventude','Goianiense','Vitoria')
print(tabela[:6])
print(tabela[-4:])
print(f'Em ordem alfabetica é {sorted(tabela)}')
print(f'a Chapecoense ta em {tabela.index("Chape")+1} lugar')