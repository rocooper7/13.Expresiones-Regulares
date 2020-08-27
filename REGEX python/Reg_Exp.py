import re
no_partidos = 0
pattern = re.compile(r'^[\d]{2,2}/[\d]{2,2}/([\d]{4,4}),(.+),(.+),([\d]+),([\d]+),.*$')
f_csv = None
def read_csv():
    global no_partidos
    with open('results.csv', mode= 'r',encoding='utf-8') as f:
        f_csv = [line for line in f]

        for line in f_csv:
            res = re.match(pattern, line)
            if res:
                total = int(res.group(4)) + int(res.group(5)) 
                if total > 10:
                    print(f'Total:{total}, Año:{res.group(1)}, Home:{res.group(2)}, Away:{res.group(3)}, No.:{no_partidos}')
                    no_partidos +=1 
        print(f'Total de partidos:{int(no_partidos)}')

if __name__ == '__main__':
    read_csv()