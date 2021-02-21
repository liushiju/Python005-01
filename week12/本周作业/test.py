from collections import Counter
urls = ['https://maoyan.com/films/1299372', 'https://maoyan.com/films/1299372', 'https://maoyan.com/films/553231', 'https://maoyan.com/films/553231', 'https://maoyan.com/films/1218142', 'https://maoyan.com/films/1218142', 'https://maoyan.com/films/1334342', 'https://maoyan.com/films/1334342', 'https://maoyan.com/films/25348', 'https://maoyan.com/films/25348', 'https://maoyan.com/films/1300936', 'https://maoyan.com/films/1300936', 'https://maoyan.com/films/1244901', 'https://maoyan.com/films/1244901', 'https://maoyan.com/films/1298938', 'https://maoyan.com/films/1298938', 'https://maoyan.com/films/1217023', 'https://maoyan.com/films/1217023', 'https://maoyan.com/films/1332663', 'https://maoyan.com/films/1332663']

url = Counter(urls)
# print(url)
res= sorted(url)
print(res)