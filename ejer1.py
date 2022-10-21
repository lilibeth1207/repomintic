chavo = int (input())
quico = (chavo*2) + 4
nono = (chavo + quico) // 5

print(chavo, " ",quico, " ",nono, " ")

if nono > 80:
  print ("cuatro")
elif nono >= 41 and nono <= 80:
  print ("tres")
elif nono >= 21 and nono <= 40:
  print ("dos")
else: print ("uno")