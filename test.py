from chessboard import display
import platform

if platform.system() == "Linux":

    position = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'

    while True:
        display.start(position)