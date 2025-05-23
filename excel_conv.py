import pandas as pd

# Данные в виде списка списков
data = [[ 0.        , -0.21593291, -0.12159329,  0.24528302],
       [ 0.        , -0.04893907,  0.57085162,  0.07944784],
       [ 0.        ,  0.10488285, -0.08411749, -0.30480596],
       [ 0.        , -0.05372785,  0.10830797,  0.1762441 ]]

# Создание DataFrame
df = pd.DataFrame(data, columns=["x_k", "Y_k (предыдущая итерация)", "Y_k (последняя итерация)", "Разность"])

# Сохранение в Excel
df.to_excel("B.xlsx", index=False)