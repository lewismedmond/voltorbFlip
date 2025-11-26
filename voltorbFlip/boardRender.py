def draw_keys(col_keys, row_keys, GAME_SIZE, font, screen):
    for i,(voltorb, score) in enumerate(col_keys):
        voltorbCount = font.render(str(voltorb), True, (0,0,0))
        pointTotal = font.render(str(score).zfill(2), True, (0,0,0))
        screen.blit(voltorbCount, (i * 47 + 34, (GAME_SIZE) * 47 + 26))  # Positioning key in the right place
        screen.blit(pointTotal, (i * 47 + 22, (GAME_SIZE) * 47 + 6))

    for i,(voltorb, score) in enumerate(row_keys):
        voltorbCount = font.render(str(voltorb), True, (0,0,0))
        pointTotal = font.render(str(score).zfill(2), True, (0,0,0))
        screen.blit(voltorbCount, ((GAME_SIZE) * 47 + 30, i*47 + 27))  # Positioning key in the right place
        screen.blit(pointTotal, ((GAME_SIZE) * 47 + 20, i*47+7))