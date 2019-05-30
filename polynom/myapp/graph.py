import plotly
from plotly.graph_objs import Scatter, Layout
from bs4 import BeautifulSoup
val = open("htmltext.txt", "w+")

sis = "5x^6 + 3x^5 + 7x^4 + 11x^3 - 9x^2 - 50"
nullkohad = [-1.678,1.236]

astmed = [pos for pos, char in enumerate(sis) if char == "^"]

sismod = sis

for i in range(len(astmed)):
    sismod = (sismod[:(astmed[i]-1)] + "*" + sismod[(astmed[i]-1):])
    
    if(i < len(astmed)-1):
        for j in range(len(astmed)):
            astmed[j] += 1

polnm = sismod.replace("^","**")

xlist = []
y = []

nullkohad.sort()
if(len(nullkohad) > 1):
    vahemik = (nullkohad[1]-nullkohad[0])*1.05 + 0.5
   
else:
    vahemik = 4

vahe = vahemik/1000
alg = -vahemik/2

for i in range(int((vahemik/vahe) + 1)):
    x = float(alg + vahe)
    xlist.append(x)
    alg = x
    y.append(eval(polnm))

plotly.offline.plot({
 
"data":
[ Scatter(x = xlist,y = y)],

"layout":
Layout(title= sis)

}, filename='templates/graafik.html', auto_open = False
)


html = open("templates/graafik.html").read()
soup = BeautifulSoup(html)
val.write(soup.get_text())
val.close()
