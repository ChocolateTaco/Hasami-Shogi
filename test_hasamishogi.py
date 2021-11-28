import unittest
from HasamiShogiGame import *

class HasamiTests(unittest.TestCase):
    """List of tests used during the development of Library.py its functions"""
    # def test01_vertical_move(self):
    #     """This test ensures that the turns alternate after a successful move."""
    #     game = HasamiShogiGame()
    #     player = game.get_active_player()
    #     self.assertEqual(player, "BLACK")
    #     game.make_move("i1", "f1")
    #     move2 = game.get_active_player()
    #     self.assertEqual(move2, "RED")
    #     game.display_game()
    #     game.make_move("a1", "e1")
    #     move3 = game.get_active_player()
    #     game.display_game()
    #     self.assertEqual(move3, "BLACK")

    
    # def test02_horizontal_move(self):
    #     "This test checks that the pieces can move up without obstructions."""
    #     game = HasamiShogiGame()
    #     game.make_move("i1", "f1")
    #     game.make_move("a1", "e1")
    #     # print(f"SHOULD BE: {game.get_active_player()}")
    #     # checks to move right
    #     game.make_move("f1", "f5")
    #     game.make_move("e1", "e5")
    #     game.display_game()
    #     # checks to move left
    #     game.make_move("f5", "f1")
    #     game.make_move("e5", "e1")
    #     # checks to move right but out of bounds
    #     game.make_move("f1", "w2")
    #     # checks to move left but out of bounds
    #     game.make_move("f5", "f9")
    #     game.make_move("i2", "e2")
    #     game.display_game()

    # def test03_vertical_up_obstructed(self):
    #     "This test checks that the pieces can down without obstructions."""
    #     game = HasamiShogiGame()
    #     not_allowed = game.make_move("i1", "a1")
    #     self.assertFalse(not_allowed)
    #     # game.make_move("a1", "i1")
    #     filled_space = game.get_square_occupant(game.move_to_index("i1"))
    #     game.display_game()
    #     self.assertEqual(filled_space, "BLACK")
    
    # def test04_move_to_index(self):
    #     """This test checks and determines if the square is converted correctly to an index."""
    #     game = HasamiShogiGame()
    #     square = game.move_to_index("a1")
    #     self.assertEqual(square, "00")
    #     square = game.move_to_index("z0")
    #     self.assertFalse(square)
    #     square = game.move_to_index("i9")
    #     self.assertEqual(square, "88")

    # def test05_index_to_move(self):
    #     """This converts an index to a move parameter."""
    #     game = HasamiShogiGame()
    #     square = game.index_to_move("00")
    #     self.assertEqual(square, "a1")
    #     square = game.index_to_move("76")
    #     self.assertEqual(square, "h7")


    def test_05_vertical_capture(self):
        """This test checks the potential for a potential capture vertically above."""
        game = HasamiShogiGame()
        game.make_move('i2','b2')
        game.make_move('a3','c3')
        game.make_move('b2','b3')
        game.make_move('a9','b9')
        game.make_move('i3','d3')
        game.display_game()
        game.get_num_captured_pieces("RED")
    
    def test_06_vertical_capture_double(self):
        """This test checks the potential for a potential capture vertically above."""
        game = HasamiShogiGame()
        game.make_move('i5','e5')
        game.make_move('a5','d5')
        game.make_move('i4','f4')
        game.make_move('a9','g9')
        game.make_move('f4','f5') # Black
        print(game.get_active_player())
        # game.make_move('g9','g5')
        game.display_game()
        game.get_num_captured_pieces("RED")


    

if __name__ == '__main__':
    unittest.main()
