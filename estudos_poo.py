
class TV:

    def __init__(self) -> None:
        self.cor = 'Preta'
        self.ligado = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 50

    def ligar_tv(self):
        pass


tv_sala = TV()
tv_quarto = TV()

tv_sala.cor = 'Branca'

print(tv_quarto.cor)
print(tv_sala.cor)

