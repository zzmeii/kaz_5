import pandas as pd

k = 2
f = 16

data = [bin(i).replace('0b', "").zfill(4) for i in range(2 ** 4)]
data = [list(i) for i in data]
[i.insert(0, '1') for i in data]
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

dataf = pd.DataFrame(data)
dataf = dataf.rename(columns={0: 'x0', 1: 'x1', 2: 'x2', 3: 'x3', 4: 'x4'})
dataf['x1*x2'] = dataf['x1'] * dataf['x2']
dataf['x3*x4'] = dataf['x3'] * dataf['x4']
