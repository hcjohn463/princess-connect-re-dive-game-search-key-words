import bs4,requests,pickle
def rename_keys(d, keys):
    return dict([(keys.get(k), v) for k, v in d.items()])
url = 'https://hanshino.nctu.me/online/KyaruMiniGame'
htmlfile = requests.get(url)
soup = bs4.BeautifulSoup(htmlfile.text,'lxml')

tbody = soup.find('tbody')

words = {'ㄓ':[],'ㄕ':[],'ㄖ':[],'ㄗ':[],'ㄙ':[],'ㄚ':[],'ㄛ':[],'ㄜ':[]
,'ㄞ':[],'ㄟ':[],'ㄠ':[],'ㄡ':[],'ㄢ':[],'ㄣ':[],'ㄤ':[],'ㄥ':[],'ㄦ':[],
'ㄧ':[],'ㄧㄚ':[],'ㄧㄝ':[],'ㄧㄠ':[],'ㄧㄡ':[],'ㄧㄢ':[],'ㄧㄣ':[],
'ㄧㄤ':[],'ㄧㄥ':[],'ㄨ':[],'ㄨㄚ':[],'ㄨㄛ':[],'ㄨㄟ':[],'ㄨㄢ':[],
'ㄨㄣ':[],'ㄨㄤ':[],'ㄨㄥ':[],'ㄩ':[],'ㄩㄝ':[],'ㄩㄢ':[],'ㄩㄣ':[]}

tr_all = tbody.find_all('tr')
for tr in tr_all:
	head = tr.find('td',class_='head').text
	normal = tr.find('td',class_='normal')
	great = tr.find('td',class_='great')
	puricone = tr.find('td',class_='puricone')
	if normal:
	 	words[head].append(normal.text)
	if great:
	 	words[head].append(great.text)
	if puricone:
		words[head].append(puricone.text)



translations = {'ㄓ':'5 ','ㄕ':'g ','ㄖ':'b ','ㄗ':'y ','ㄙ':'n ','ㄚ':'8 ','ㄛ':'i ','ㄜ':'k '
,'ㄞ':'9 ','ㄟ':'o ','ㄠ':'l ','ㄡ':'. ','ㄢ':'0 ','ㄣ':'p ','ㄤ':'; ','ㄥ':'/ ','ㄦ':'- ',
'ㄧ':'u ','ㄧㄚ':'u8 ','ㄧㄝ':'u, ','ㄧㄠ':'ul ','ㄧㄡ':'u. ','ㄧㄢ':'u0 ','ㄧㄣ':'up ',
'ㄧㄤ':'u; ','ㄧㄥ':'u/ ','ㄨ':'j ','ㄨㄚ':'j8 ','ㄨㄛ':'ji ','ㄨㄟ':'jo ','ㄨㄢ':'j0 ',
'ㄨㄣ':'jp ','ㄨㄤ':'j; ','ㄨㄥ':'j/ ','ㄩ':'m ','ㄩㄝ':'m, ','ㄩㄢ':'m0 ','ㄩㄣ':'mp '}


finals = rename_keys(words,translations)

while True:
	head = input('輸入head(英文):')
	print(finals[head])