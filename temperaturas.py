temperaturas = [[20, 19.5], [20, 19.7], [20, 22.2], [20, 20.1], [21, 19.9], [21, 20.7], [21, 21.2], [21, 21.5], [25, 25.5], [25, 24.7], [25, 25.2], [25, 24.1]]

somatorio_sp = 0
somatorio_sv = 0
total = 0

for temperatura in temperaturas:
    somatorio_sp += temperatura[0]
    somatorio_sv += temperatura[1]
    total += 1

media_sp = somatorio_sp / total
media_pv = somatorio_sv / total

somatorio_desvio_sp = 0
somatorio_desvio_pv = 0

for temperatura in temperaturas:
    somatorio_desvio_sp += (temperatura[0] - media_sp) ** 2
    somatorio_desvio_pv += (temperatura[1] - media_pv) ** 2

desvio_padrao_sp = (somatorio_desvio_sp / total) ** 0.5
desvio_padrao_pv = (somatorio_desvio_pv / total) ** 0.5

print('Média SP = ', media_sp)
print('Desvio Padrão SP = ', desvio_padrao_sp)
print('Média PV = ', media_pv)
print('Desvio Padrão PV = ', desvio_padrao_pv)

