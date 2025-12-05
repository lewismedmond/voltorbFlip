
import pygame
from sys import exit
from boardGenerator import Board
from tile import Tile
from agents.random_agent import RandomPlayer

from boardRender import draw_keys
import time
import csv


def play_one_game(GAME_SIZE, games_played, agent = None, render = False,  score_log = []):
    
    agent.set_score(0)
    board = Board(GAME_SIZE)

    if render:
        pygame.init()
        pygame.display.set_caption("Voltorb Flip")
        clock = pygame.time.Clock() # Initialize clock for controlling frame rate
        game_font = pygame.font.SysFont("Pixel Emulator", 16)
        screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50))
        screen.fill((100,255,100))

        all_sprites = pygame.sprite.Group()
        for i in range(GAME_SIZE**2):
            all_sprites.add(Tile((i % GAME_SIZE), (i // GAME_SIZE), board.board[i % GAME_SIZE][i // GAME_SIZE]))  # Creating all tiles and fitting them to grid
        
        draw_keys(board.col_keys, board.row_keys, GAME_SIZE, game_font, screen)

    if agent == None:
        pass
        #play_human_game(GAME_SIZE, render)
    else:
        game_over = False
        if board.total_score_tiles == 0:
            game_over = True
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            game_over, action = play_one_move(agent, board)

            if render:
                #pygame.draw.rect(screen, (100, 255, 100), pygame.Rect(GAME_SIZE * 47,GAME_SIZE * 47, 50, 50))
                #screen.blit(game_font.render(str(rl_player.score), True, (0, 0, 0)), (GAME_SIZE * 47 + 15,GAME_SIZE * 47 + 15))  # render player score
                
                for tile in all_sprites:
                    if tile.col == action[0] and tile.row == action[1]:  # reveal chosen tile
                        tile.reveal_tile()
                        if tile.value == -1:  # if the tile selected is a voltorb, end the game
                            game_over = True
                
                all_sprites.draw(screen) # Sprite rendering
                clock.tick(30)  # Limit frame rate to 30 FPS
                pygame.display.update()  # update screen
        
        score_log.append((board.score_tiles_remaining - board.total_score_tiles)/board.total_score_tiles if board.total_score_tiles > 0 else -1)
        games_played += 1
        if games_played % 1000 == 0:
            agent.save_q_table("voltorbFlip/q_table.pkl")
            
            print(score_log[-10:])
            print(games_played, "games played")
            
            with open("voltorbflip/scores.csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerows([score_log])
                score_log = []
            

            
            
    
def play_one_move(agent, board, all_sprites = None):
        time.sleep(1)
        
        available_moves = board.available_moves
        if(len(available_moves) == 0):
            return True, None
        
        current_state = board.state.copy()
        action = agent.select_action(current_state, available_moves)
        
        #agent.score += board.board[action] if board.board[action] > 0 else 0  # update agent score if a point tile is selected
        
        reward = board.play(action)
        new_state = board.state
        agent.step(current_state, action, reward, new_state, board.available_moves)
        

        return False, action


#GAME_SIZE = 2  # set row/column count
#rl_player = RLPlayer(GAME_SIZE)  # initialise rl agent


#score_log = []

#for i in range(10000):
#
   

    





   
     # draw the column and row keys

#    while True and not game_over:
#        
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #    pos = pygame.mouse.get_pos()
            #    for tile in all_sprites:
            #        if tile.rect.collidepoint(pos) and not tile.revealed:
            #            tile.reveal_tile()
#        if not game_over:
            
#            next_move = rl_player.select_move()  # player selects next move 

 #           if next_move == None:
 #               game_over = True
 #               rl_player.update_weights()
 #               score_log.append([rl_player.score])
 #               break

 #           if current_board[next_move[0]][next_move[1]] == -1: # check if bomb has been flipped
 #               rl_player.set_score(-1)
 #               game_over = True
 #               rl_player.update_weights()
 #               score_log.append([rl_player.score])
                
                


#            rl_player.play_move(next_move, current_board, all_sprites)  # player updates their board with new information
#            if rl_player.score == AVAILABLE_SCORE:
#                game_over = True
#                rl_player.update_weights()
#                score_log.append([rl_player.score])



        

