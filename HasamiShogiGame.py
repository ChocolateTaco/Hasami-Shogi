# Steven Tran
# 2021-12-02
# CS-162 Final Project: Hasami Shogi (Variant 1)
# Description: In the Japanese Board Game of Hasami Shogi, players take turns
# moving their piece (either red or black). Pieces move like rooks in the
# game of chess, horizontally or vertically. The goal is to at capture least 8
# of the 9 opponents pieces. To capture a piece, the opposing player's piece
# must be "sandwiched" between two of the active player's pieces.

class GamePiece():
    """Initial game pieces (either RED or BLACK). Still TBD if want to use."""
    def __init__(self):
        pass

class HasamiShogiGame():
    """Initializes a game of Hasami Shogi (Japanese Rook-Like Capture Game).
    The board will be stored in this init of _game_board where it is first
    initalized with 'RED' and 'BLACK' pieces at the applicable starting
    postiions."""
    def __init__(self):
        """Initializes the _game_board.
        Moves will be tracked using the _move_tracker which will increment by
        one based on successful moves. This may also be used later at the end
        to determine how many moves it took for the game to complete.
        _game_state: will be used with a while loop to determine the current
        state of the game. After each move, determines if the game is still
        in progress. This will be achieved by calling get_num_captured_pieces
        function to determine if either RED or BLACK has captured at least 8
        pieces. If so, the _game_state flag will result with the winner.
        Otherwise it will remain in the 'IN PROGRESS' state. """
        self._rows = 9          # NOT USED
        self._columns = 9       # NOT USED
        # self._top_label = "    [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ][ 8 ][ 9 ]"
        self._top_label = "    1 2 3 4 5 6 7 8 9"
        self._side_label = ['a','b','c','d','e','f','g','h','i']
        self._game_board = [["R", "R", "R", "R", "R", "R", "R", "R", "R"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["B", "B", "B", "B", "B", "B", "B", "B", "B"]]
        self._move_tracker = 1      # Tracks the number of moves performed in the game
        self._game_state = "UNFINISHED"     # Will be used for while loop to
        self._red_caps = 0
        self._black_caps = 0
        # determine if the game is still on-going.

    def __repr__(self) -> str:
        """Printable Format of the Board Game State"""
        for i in self._side_label:
            print(self._side_label)

    def display_game(self):
        """Displays the current state of the game. """
        print(self._top_label)
#        print("=======================")
        for i in range(0, len(self._side_label)):
            print(self._side_label[i], "|" , *(self._game_board[i]))

    def set_red(self, space):
        """Sets a red piece in a specified location."""
        row = int(space[0])
        col = int(space[1])
        self._game_board[row][col] = "R"

    def set_black(self, space):
        """Sets a black piece in a specified location."""
        row = int(space[0])
        col = int(space[1])
        self._game_board[row][col] = "B"

    def cap_red(self):
        """Increases the number of RED pieces captured by one."""
        self._red_caps += 1

    def cap_black(self):
        """Increases the number of BLACK pieces captured by one."""
        self._black_caps += 1

    def set_empty(self, space):
        """Sets a space to empty in a specified location (typically starting
        location of a move)."""
        row = int(space[0])
        col = int(space[1])
        self._game_board[row][col] = "_"

    def get_game_state(self):
        """Function determines the current progress of the game. If there's a
        current winner or if its still "UNFINISHED"".

        Returns:
            UNFINISHED (str): when red/black captures < 8
            RED_WON (str): when black captures >= 8
            BLACK_WON (str): when red captures >= 8
        """
        if self._game_state is None:
            return "UNFINISHED"
        elif self._game_state == "RED_WON":
            return "RED_WON"
        else:
            return "BLACK_WON"

    def get_active_player(self):
        """Determines the active player of the game init based on
        number of turns partaken.

        Returns:
            BLACK (str): if move_tracker is odd
            RED (str): if move_tracker is even
        """
        if self._move_tracker % 2 == 1:            
            return "BLACK"
        else:
            return "RED"

    def get_num_captured_pieces(self, color = None):
        """Returns the number of captured pieces for the specified color.
        Used to determine if there's a winner after each move."""
        if color.upper() == "RED":
            print(f"\nRED pieces captured: {self._red_caps}")
            return self._red_caps
        if color.upper() == "BLACK":
            # Returns the number of red pieces captured
            print(f"\nBLACK pieces captured: {self._black_caps}")
            return self._black_caps
        else:
            # Raises some Error for inputting a correct color value.
            pass

    # This might work as a wrapper. Converts to human friendly tiles (a-i)(1-9)
    def move_to_index(self, move):
        """Converts the move to an index for the _game_board's list parameters
        allowing for spaces of a-i and 1-9.
        Returns:
            index (str): move to make is horizontal
            VERTICAL: move to make is vertical
            None:   Illegal move request (i.e. diagonal, non-existent space)
        """
        allowed = ['a','b','c','d','e','f','g','h','i']
        index = ''
        if len(move) != 2:
            print("INVALID SQUARE, outside of limits")
            return False
        if int(move[1]) not in range(1, 10):
            print("INVALID SQUARE, outside of limits")
            return False
        if move[0].lower() not in allowed:
            print("INVALID SQUARE, outside of limits")
            return False
        for i in range(len(allowed)):
            if allowed[i] == move[0].lower():
                # print(i+1, move[1])
                index = str(i) + str(int(move[1]) - 1)
                # print(f"The converted index is now: {index}")
                return index
        print("Reached end where its false")
        return False

    def index_to_move(self, index):
        """Converts the index to a move for the _game_board's list parameters
        allowing for spaces of a-i and 1-9.
        
        Returns:
            move (str): the game board space as a string
        """
        allowed = ['a','b','c','d','e','f','g','h','i']
        row = int(index[0])
        row = allowed[row]
        column = int(index[1]) + 1
        print(f"the row is {row}, and the column is {column}")
        move = row + str(column)
        print(move)
        return move

    def get_square_occupant(self, square = ""):
        """Determines if the square is occupied or not.

        Returns:
            "RED":   if square is occupied by a "R" piece
            "BLACK": if square is occupied by a "B" piece
            "NONE":  if square is empty; occupied by a "_"
        """
        print(f"Square being checked for occupant: {square}")
#       print(f"Checking for square occupant in space {square}")
        row = int(square[0])
        column = int(square[1])
        if self._game_board[row][column] == "B":
            print(f"Black occupies {square}")
            return "BLACK"
        elif self._game_board[row][column] == "R":
            print(f"Red occupies {square}")
            return "RED"
        elif self._game_board[row][column] == "_":
            print(f"...its empty...")
            return "NONE"
        else:
            print("Something is wrong in get_square_occupant")

    # Move Verification Functions
    def move_type(self, start_loc, end_loc):
        """After checking the start and end locations are valid, this function
        determines what kind of movement direction is being requested.

        Args:
            start_loc (str): a location with an active piece
            end_loc (str): a valid location to move an active piece

        Returns:
            HORIZONTAL: move to make is horizontal
            VERTICAL: move to make is vertical
            None:   Illegal move request (i.e. diagonal, non-existent space)
        """
        # print(f"Starting row: {start_loc[0]}, {end_loc[0]}")
        # print(f"Starting col: {start_loc[1]}, {end_loc[1]}")

        if (start_loc[0] == end_loc[0]) and (start_loc[1] != end_loc[1]):
            # print("Horizontal move requested")
            return "HORIZONTAL"
        elif (start_loc[0] != end_loc[0]) and (start_loc[1] == end_loc[1]):
            # print("Vertical move requested")
            return "VERTICAL"
        else:
#            print("An illegal move type is requested. Please try again.")
            return None
                
    def horizontal_move(self, start_loc, end_loc, pos = None):
        """Checks to see if there are any pieces between the start_loc to the
        end_loc. If the start location's column is less than the end location's
        column, then the movement is right (i.e. d1 to d7). If the start
        location's column is greater than the end location's row, then the
        movement is left (i.e. d7 to d1).

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: move is valid; sets the move.
            False: move is not valid (something obstructs)
        """
        if pos is None:
            start_col = int(start_loc[1])
            end_col = int(end_loc[1])
            if start_col > end_col:
                pos = -1 # going left
            else:
                pos = 1 # going right
        if pos < 0:
            direction = -1 # going left
        elif pos > 0:
            direction = 1 # going right
        start_col = int(start_loc[1]) + pos
        end_col = int(end_loc[1])
        index =  start_loc[0] + str(start_col)
        print(f"position is now {pos}")
        print(f"{start_col} trying to reach {end_col}")
        if self.get_square_occupant(end_loc) != "NONE":
            print("Cannot move to a non-empty space.")
            return False
        if start_col == end_col:
            # set the start location to the active player's piece
            if self.get_active_player() == "RED":
                print(f"Red moved to {end_loc}")
                self.set_red(end_loc)
                return True
            else:
                print(f"Black moved to {end_loc}")
                self.set_black(end_loc)
                return True
            self.set_empty(start_loc)
        elif self.get_square_occupant(index) == "NONE":
            print(f"checking occupant for index {index}")
            return self.horizontal_move(start_loc, end_loc, pos + direction)
        else:
            print("Invalid Move on Horizontal")
            return False
    
    #  Trying Recursive Move
    def vertical_move(self, start_loc, end_loc, pos = None):
        """Checks to see if there are any pieces between the start_loc to the
        end_loc. If the start location's row is less than the end location's
        row, then the movement is up (i.e. i1 to h1). If the start location's
        row is greater than the end location's row, then the movement is down
        (i.e. a1 to f1).

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: move is valid; sets the move.
            False: move is not valid (something obstructs)
        """
        if pos is None:
            start_row = int(start_loc[0])
            end_row = int(end_loc[0])
            if start_row > end_row:
                pos = -1 # going up
            else:
                pos = 1 # going down
        if pos < 0:
            direction = -1 # move up
        elif pos > 0:
            direction = 1 # move down
        start_row = int(start_loc[0]) + pos
        end_row = int(end_loc[0])
        index = str(start_row) + start_loc[1]
        print(f"position is now {pos}")
        print(f"{start_row} trying to reach {end_row}")
        if self.get_square_occupant(end_loc) != "NONE":
            print("Cannot move to a non-empty space.")
            return False
        if start_row == end_row:
            # set the start location to the active player's piece
            if self.get_active_player() == "RED":
                print(f"Red moved to {end_loc}")
                self.set_red(end_loc)
                return True
            else:
                print(f"Black moved to {end_loc}")
                self.set_black(end_loc)
                return True
            self.set_empty(start_loc)
        elif self.get_square_occupant(index) == "NONE":
            print(f"checking occupant for index {index}")
            return self.vertical_move(start_loc, end_loc, pos + direction)
        else:
            print("Invalid Move Vertically")
            return False
    
    def corner_capture(self, start_loc, end_loc):
        """If the current move is nearby an opponent's corner piece, check to see if
        another active player's piece resides on the nearby corner.
        Note: Corner capturesho can only occur if the active player moves to one
        of 8 tiles (a2, b1, a8, b9, h1, i2, i8, h9). A piece of the opposite
        would need to be in the respective corner (a1, a9, i0, i9)

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the corner piece. Updates the active player, and move_tracker
            False: if corner capture condition is not met
        """
        pass

    def horizontal_capture(self, start_loc, end_loc):
        """After a valid move check, determines if the current move is
        horizontal to an opponent's piece. If so check to see if another
        active player's piece is on the opposite side.

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the opponent's piece piece. Updates number of captured pieces, and move_tracker
            False: if horizontal capture condition is not met
        """
        pass

    def check_top(self, space):
        """Checks if theres at least 2 spaces available above to score a capture"""
        if int(space) - 20 < 0:
            return False
        else:
            return True

    def vertical_capture(self, start_loc, maybe_caps = None, pos = None):
        """After a valid move check, determines if the current move is vertical to an opponent's piece. If so check to see if another active player's piece is on the opposite side.

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the opponent's piece piece. Updates number of captured pieces, and move_tracker
            False: if vertical capture condition is not met
        """
        # check_top
        if pos is None:
            pos = -10
        if self.check_top(start_loc):
            space_above = str(int(start_loc) + pos)
            # Scenario for an opponent piece above, but no matching active
            if maybe_caps is not None:
                if self.get_square_occupant(space_above) == "NONE":
                    return False
                # Scenario for a sandwich/capture
                elif self.get_square_occupant(space_above) == self.get_active_player():
                    for captures in maybe_caps:
                        self.set_empty(captures)
                        if self.get_active_player() == "RED":
                            self.cap_black()
                        else:
                            self.cap_red()
            print(f"\nVertical_Capture: the space above is {space_above}")
            if self.get_square_occupant(space_above) == "NONE":
                print("No need to check above, the space is empty")
                return False
            elif self.get_square_occupant(space_above) != self.get_active_player():
                print("Found an opponent piece adjacent above.")
                if maybe_caps is None:
                    maybe_caps = []
                maybe_caps.append(space_above)
                print(maybe_caps)
                return self.vertical_capture(start_loc, maybe_caps, pos - 10)

        # check space above end location
        # if empty: return False
        # if space != active player and not empty:
        # save that spot to the list
        # if space = active player and list of opposing pieces > 0:
        # capture_pieces
        # check next space above recursively
        # check_top(scanned, pos, maybe_caps=None)
        # if maybe_caps is None: 
        # maybe_caps = []
        # maybe_caps.append(space)

    
    def next_turn(self):
        """Increases the move tracker after a successful turn."""
        self._move_tracker += 1
        
    def make_move(self, start_loc, end_loc):
        """Moves a piece from the start_loc to the end_loc as long as it is a
        valid move.

        Checks for:
            * Valid Turn (if its RED or BLACK's turn)
            * Valid Move (if the start_loc can actually reach end_loc without any obstructions)
            * Type of Move (horizontal versus vertical)
            * Capturing conditions:
                - Horizontal Captures
                - Vertical Captures
                - Corner Captures

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: updated location with the piece. Also updates start_loc to an
                empty location again. Updates the active player, and move_tracker
            False: if the current move is blocked by any pieces
        """
        start = self.move_to_index(start_loc)
        end = self.move_to_index(end_loc)
        # Checks if the starting square belongs to the active player's turn
        move = False
        if start and end:
            if self.get_square_occupant(start) == self.get_active_player():
                # Check if move is possible
                print(f"Moving from {start} to {end}")
                moving = self.move_type(start, end)
                if moving == "VERTICAL":
                    print("\nmake_move: Confirmed for vertical path")
                    move = self.vertical_move(start, end)
                elif moving == "HORIZONTAL":
                    print("\nmake_move: Confirmed for Horizontal path")
                    move = self.horizontal_move(start, end)
                else:
                    print("Invalid move. Please try again.")
                    return False
                print(f"Your turn: {self.get_active_player()}")
            else:
                print(f"Invalid Turn\nCurrent Player: {self.get_active_player()}")
        # After any successful move, scan the areas for possible captures.
        if move:
            self.vertical_capture(end)
            self.next_turn()



def main():
    game = HasamiShogiGame()
    game.display_game()
    print(game.get_active_player())
    game.make_move("i1", "g1")
    game.display_game()

if __name__ == "__main__":
    main()