from spaceInvadersGUI import *

score = 0
go_to_the_game = False
k_space_is_down = False
while True:
    if not go_to_the_game:
        show_opening_screen()
        go_to_the_game = True

    clock.tick(FPS)
    win.fill(BLACK)

    win.blit(background, (0, 0))
    win.blit(trophy, (240, 15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                k_space_is_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                k_space_is_down = False
        if play_stop_bg_music.is_clicked():
            stop_play_button()
    if k_space_is_down:
        now = pygame.time.get_ticks()
        if now - my_player.last_shot > 200:
            my_player.last_shot = now
            my_player.shoot()
    all_sprites.draw(win)
    all_sprites.update()
    user_score.draw(win)
    my_shieldBar.draw(my_shieldBar.shield_pct)
    play_stop_bg_music.draw(win)
    pygame.display.update()

    bullet_and_meteor_collide = pygame.sprite.groupcollide(meteors, my_player.bullets, True, True)
    for collision in bullet_and_meteor_collide:
        score += 1
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'large')
        if my_shieldBar.shield_pct < 90:
            my_shieldBar.shield_pct += 10

    player_and_meteors_collide = pygame.sprite.spritecollide(my_player, meteors, True)
    for collision in player_and_meteors_collide:
        my_shieldBar.shield_pct -= 45
        score -= 2
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'small')

        if my_shieldBar.shield_pct <= 0:
            if score > 50:
                message = "You won the game!"
            else:
                message = "You lost in this game, but you can try again"
            show_game_over_screen(message)
            if not show_game_over_screen(message):
                score = 0
                user_score.set_text(str(score))
                my_shieldBar.shield_pct = 90
                go_to_the_game = False
    # player_and_meteor_collide = pygame.sprite.spritecollideany(my_player, meteors)
    # if player_and_meteor_collide is not None:
        # my_player.change_color()
