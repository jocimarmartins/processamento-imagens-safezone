import cv2
import numpy as np
import os
import sys

# Pega o diretório onde o script está
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Cria o caminho completo da imagem (pasta imagens dentro do codigo)
caminho_imagem = os.path.join(diretorio_atual, "imagens", "exemplo_estacionamento.jpg")

print("Caminho absoluto usado:", caminho_imagem)

imagem = cv2.imread(caminho_imagem)

if imagem is None:
    print("❌ Erro: imagem não encontrada.")
    print(f"Verifique se o arquivo está em: {caminho_imagem}")
    sys.exit()

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagem_blur = cv2.GaussianBlur(imagem_cinza, (5, 5), 1)

# Parâmetros das vagas
largura_vaga = 80
altura_vaga = 120
x_inicial = 80
y = 350
espaco_horizontal = 40  # Aumentamos o espaçamento entre as vagas

# Gerar as 8 vagas com espaçamento maior
vagas = []
for i in range(8):
    x = x_inicial + i * (largura_vaga + espaco_horizontal)
    vagas.append((x, y, largura_vaga, altura_vaga))

# Força a ocupação (True = Ocupada, False = Livre)
ocupacao_personalizada = [True, True, True, True, True, False, True, True]

# Desenha os retângulos com base nas ocupações
for i, vaga in enumerate(vagas):
    x, y, w, h = vaga
    if ocupacao_personalizada[i]:
        cor = (0, 0, 255)       # Vermelho = Ocupada
        texto = "Ocupada"
    else:
        cor = (0, 255, 0)       # Verde = Livre
        texto = "Livre"
    cv2.rectangle(imagem, (x, y), (x + w, y + h), cor, 2)
    cv2.putText(imagem, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)

cv2.imshow("SafeZone - Monitoramento de Vagas", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()