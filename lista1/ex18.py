mb = float(input("Digite quantos MBs são o arquivo"))
velocidadeMbps = float(input("Digite em Mbps a velocidade do download"))
tempoDownload = (mb*8)/velocidadeMbps

tempoMinutos = tempoDownload/60
print("Demoraria em minutos: ", tempoMinutos, "minutos")
