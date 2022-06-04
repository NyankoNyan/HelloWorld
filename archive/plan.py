# Терминология
# Парадигмы
# Декомпозиция

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilyagromov', 'masha.yashkina']
          }

sort_govna = []
for key, value in emails.items():
    for i in value:
        i = i.replace('.', '')
        x = (i + '@' + key)
        sort_govna.append(x)

sort_govna.sort()

#for govn in sort_govna:
#    print(govn)
#print(str(sort_govna).replace(' ', '\n'))

def govn_to_str(val):
    result = ""
    for sub in val:
        result += str(sub) + '\n'
    return result

print(govn_to_str(sort_govna))
