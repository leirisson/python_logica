import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Criando o Dataset
data = {'Número': list(range(1, 21)), 'Próximo': list(range(2, 22))}
df = pd.DataFrame(data)

# 2. Preparando os Dados
X = df[['Número']]
y = df['Próximo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Treinando o Modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Validando o Modelo
score = model.score(X_test, y_test)
print(f"Acurácia do modelo: {score:.2f}")

# 5. Entrada Interativa
while True:
    try:
        numero_usuario = float(input("Digite um número (ou 'sair' para encerrar): "))
        proximo_numero = model.predict([[numero_usuario]])
        print(f"O próximo número previsto para {numero_usuario} é {proximo_numero[0]:.2f}\n")
    except ValueError:
        print("Encerrando...")
        break
