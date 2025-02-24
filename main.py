from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class JogoDaVelha(App):
    def build(self):
        self.jogo_em_andamento = True
        self.jogador_atual = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]

        # Layout principal
        self.layout = BoxLayout(orientation='vertical')

        # Label para exibir o status
        self.status_label = Label(text=f"Jogador {self.jogador_atual}'s vez")
        self.layout.add_widget(self.status_label)

        # Layout para os botões do jogo
        self.grid = GridLayout(cols=3)
        for i in range(3):
            for j in range(3):
                button = Button(font_size=40, on_press=self.fazer_jogada)
                button.pos = (i, j)
                self.grid.add_widget(button)

        self.layout.add_widget(self.grid)

        return self.layout

    def fazer_jogada(self, button):
        i, j = button.pos
        i, j = int(i), int(j)
        if self.tabuleiro[i][j] == '' and self.jogo_em_andamento:
            self.tabuleiro[i][j] = self.jogador_atual
            button.text = self.jogador_atual
            if self.checar_vitoria():
                self.status_label.text = f"Jogador {self.jogador_atual} venceu!"
                self.jogo_em_andamento = False
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                self.status_label.text = f"Jogador {self.jogador_atual}'s vez"

    def checar_vitoria(self):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] != '':
                return True

        # Verificar colunas
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] and self.tabuleiro[0][col] != '':
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] != '':
            return True

        return False

if __name__ == "__main__":
    JogoDaVelha().run()
