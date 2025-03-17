from microbit import *
import radio

class Volante:
    
    ARROW_NW = Image("99000:" "90000:" "00000:" "00000:" "00000")
    ARROW_N = Image("00900:" "09090:" "00000:" "00000:" "00000")
    ARROW_NE = Image("00099:" "00009:" "00000:" "00000:" "00000")   

    MOVE_NW_0 = Image("00000:" "09990:" "09000:" "09000:" "00000")
    MOVE_NW_1 = Image("99900:" "90000:" "90000:" "00000:" "00000")
    MOVE_NW = [MOVE_NW_0, MOVE_NW_1]

    MOVE_N_0 = Image("00000:" "00900:" "09090:" "90009:" "00000")
    MOVE_N_1 = Image("00900:" "09090:" "90009:" "00000:" "00000")
    MOVE_N = [MOVE_N_0, MOVE_N_1]

    MOVE_NE_0 = Image("00000:" "09990:" "00090:" "00090:" "00000")
    MOVE_NE_1 = Image("00999:" "00009:" "00009:" "00000:" "00000")
    MOVE_NE = [MOVE_NE_0, MOVE_NE_1]    

    ARROWS = [ARROW_NW, ARROW_N, ARROW_NE]
    MOVES = [MOVE_NW, MOVE_N, MOVE_NE]
    
    def __init__(self):
        self.flechas = []
        for flecha in Volante.ARROWS:
            self.flechas.append(flecha)
        self.moves = []
        for move in Volante.MOVES:
            self.moves.append(move)
        self.actual = 1
        self.caminar = False

    def display(self):
        if self.caminar:
            display.show(self.moves[self.actual], delay=50)
        else:
            display.show(self.flechas[self.actual])

class Buscador(Volante):
    def __init(self):
        super().__init__()

    def capturar_sennal_de_radio(self):
        mensaje = radio.receive()
        if mensaje:
            self.actual = int(mensaje[0])
            if mensaje[1] == '1':
                self.caminar = True
            else:
                self.caminar = False

class Receptora:
    def __init__(self):
        radio.on()
        radio.config(channel = 0, group = 0, power = 7)
        self.volante = Buscador()

    def run(self):
        while True:
            self.volante.capturar_sennal_de_radio()
            self.volante.display()
            sleep(100)    

def main():
    Receptora().run()

if __name__ == "__main__":
    main()