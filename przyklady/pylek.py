from rich.console import Console
from rich.table import Table

class ChessPiece:
    """
    Klasa Pyłka reprezentująca wspólne dane figur szachowych.
    """
    def __init__(self, name, color):
        self.name = name  # Nazwa figury (np. Pawn, Rook)
        self.color = color  # Kolor figury (White, Black)

    def display(self, position):
        print(f"{self.color} {self.name} at {position}")


class ChessPieceFactory:
    """
    Fabryka Pyłków zarządza współdzielonymi obiektami figur szachowych.
    """
    _pieces = {}

    @staticmethod
    def get_piece(name, color):
        key = f"{name}-{color}"
        if key not in ChessPieceFactory._pieces:
            ChessPieceFactory._pieces[key] = ChessPiece(name, color)
            print(f"Created new piece: {name} ({color})")
        else:
            print(f"Reusing existing piece: {name} ({color})")
        return ChessPieceFactory._pieces[key]


class ChessBoard:
    """
    Klient przechowujący dane specyficzne dla każdej figury (pozycja).
    """
    def __init__(self):
        self.pieces = []

    def place_piece(self, name, color, position):
        piece = ChessPieceFactory.get_piece(name, color)
        self.pieces.append((piece, position))

    def display_board(self):
        for piece, position in self.pieces:
            piece.display(position)





class ChessBoardRenderer:
    """
    Klasa odpowiedzialna za rysowanie planszy szachowej w interfejsie tekstowym z kolorami.
    """
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.board = [[" " for _ in range(8)] for _ in range(8)]  # Plansza 8x8

    def prepare_board(self):
        """
        Przygotowuje planszę do renderowania na podstawie ustawionych figur.
        """
        for piece, position in self.chess_board.pieces:
            row = 8 - int(position[1])  # Konwersja wiersza
            col = ord(position[0].upper()) - ord('A')  # Konwersja kolumny
            symbol = piece.name[0].upper()  # Skrót nazwy figury (np. P dla Pawn)
            if piece.color == "White":
                self.board[row][col] = f"[bold white]{symbol}[/bold white]"
            else:
                self.board[row][col] = f"[bold red]{symbol.lower()}[/bold red]"

    def render(self):
        """
        Rysuje planszę szachową w terminalu z kolorami.
        """
        self.prepare_board()
        console = Console()
        table = Table(show_header=False, box=None, padding=(0, 1))

        # Dodanie nagłówka kolumn (A-H)
        col_header = [" "] + [f"[bold]{chr(c)}[/bold]" for c in range(ord("A"), ord("H") + 1)]
        table.add_row(*col_header)

        # Dodanie wierszy planszy
        for row_num, row in enumerate(self.board):
            row_label = f"[bold]{8 - row_num}[/bold]"  # Numer wiersza
            table.add_row(row_label, *row)

        console.print(table)



# Użycie
board = ChessBoard()

# Dodanie figur do planszy
board.place_piece("Pawn", "White", "A2")
board.place_piece("Pawn", "White", "B2")
board.place_piece("Rook", "White", "A1")
board.place_piece("Pawn", "Black", "A7")
board.place_piece("Rook", "Black", "A8")
board.place_piece("Pawn", "White", "C2")  # Reusing White Pawn

# Wyświetlenie stanu planszy
board.display_board()


renderer = ChessBoardRenderer(board)
renderer.render()