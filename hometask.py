from urllib.request import urlopen
from json import loads
from itertools import groupby


#Задание 1
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
info = data['query']['pages']['183903']['revisions']
dates = []
for date, counts in groupby(info, lambda x: x['timestamp'].split('T')[0]):
    dates.append([date, len(list(counts))])
dates.sort(key=lambda x: x[1], reverse=True)
for date in dates:
    print(' '.join([str(counts) for counts in date]))

print('')

#Задание 2
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
info = data['query']['pages']['192203']['revisions']
dates = []
for date, counts in groupby(info, lambda x: x['timestamp'].split('T')[0]):
    dates.append([date, len(list(counts))])
dates.sort(key=lambda x: x[1], reverse=True)
print(dates[0][0], "- Дата смерти")

