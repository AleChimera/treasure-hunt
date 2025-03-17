from microbit import *
import radio

class Volante:
    
    FLECHA_NW = Image("99000:" "90000:" "00000:" "00000:" "00000")
    FLECHA_N = Image("00900:" "09090:" "00000:" "00000:" "00000")
    FLECHA_NE = Image("00099:" "00009:" "00000:" "00000:" "00000")   

    MOVE_NW_0 = Image("00000:" "09990:" "09000:" "09000:" "00000")
    MOVE_NW_1 = Image("99900:" "90000:" "90000:" "00000:" "00000")
    MOVE_NW = [MOVE_NW_0, MOVE_NW_1]

    MOVE_N_0 = Image("00000:" "00900:" "09090:" "90009:" "00000")
    MOVE_N_1 = Image("00900:" "09090:" "90009:" "00000:" "00000")
    MOVE_N = [MOVE_N_0, MOVE_N_1]

    MOVE_NE_0 = Image("00000:" "09990:" "00090:" "00090:" "00000")
    MOVE_NE_1 = Image("00999:" "00009:" "00009:" "00000:" "00000")
    MOVE_NE = [MOVE_NE_0, MOVE_NE_1]    

    FLECHAS = [FLECHA_NW, FLECHA_N, FLECHA_NE]
    MOVES = [MOVE_NW, MOVE_N, MOVE_NE]
    
    def __init__(self):
        self.flechas = []
        for flecha in Volante.FLECHAS:
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

class Guia(Volante):
    def __init__(self):
        super().__init__()

    def __switch_caminar(self):
        self.caminar = not self.caminar

    def capturar_sennales(self):
        if (button_a.was_pressed() and button_b.was_pressed() or button_b.was_pressed() and button_a.was_pressed()):
            self.__switch_caminar()
        elif button_a.is_pressed() and not button_b.is_pressed():
            self.actual = 0
        elif button_b.is_pressed() and not button_a.is_pressed():
            self.actual = 2
        else:
            self.actual = 1

    def transmitir(self):
        mensaje = ''
        mensaje += str(self.actual)
        if self.caminar:
            mensaje += "1"
        else:
            mensaje += "0"
        radio.send(mensaje)

class Emisora:
    def __init__(self):
        radio.on()
        radio.config(channel = 0, group = 0, power = 7)
        self.volante = Guia()

    def run(self):
        while True:
            self.volante.capturar_sennales()
            self.volante.transmitir()
            self.volante.display()
            sleep(100)

def main():
    Emisora().run()

if __name__ == "__main__":
    main()
