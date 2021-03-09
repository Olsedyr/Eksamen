import base64
import io
import os
import platform
import sys
import json

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

def main_menu_setup():
    show_mouse()
    SCREEN.fill(WHITE)
    text_surf, text_rect = text_objects('Jungle Climb', MENU_TEXT)
    text_rect.center = (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 4))
    SCREEN.blit(text_surf, text_rect)
    text_surf, text_rect = text_objects(f'v{VERSION}', SMALL_TEXT)
    text_rect.center = (int(SCREEN_WIDTH * 0.98), int(SCREEN_HEIGHT * 0.98))
    SCREEN.blit(text_surf, text_rect)
    text_surf, text_rect = text_objects('Created by Elijah Lopez', LARGE_TEXT)
    text_rect.center = (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 0.84))
    SCREEN.blit(text_surf, text_rect)
    pygame.display.update()


def main_menu():
    global ticks
    main_menu_setup()
    start_game = view_hs = False
    while True:
        click = False
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4
                      and (pressed_keys[K_LALT] or pressed_keys[K_RALT])
                      or event.key == K_q or event.key == K_ESCAPE))
            if event.type == QUIT or alt_f4: sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE: start_game = True
            elif event.type == KEYDOWN and (event.key == K_v or event.key == K_h): view_hs = True
            elif event.type == MOUSEBUTTONDOWN: click = True

        if button('S T A R T  G A M E', *button_layout_4[0], click): start_game = True
        elif button('V I E W  H I G H S C O R E S', *button_layout_4[1], click) or view_hs:
            view_high_scores()
            view_hs = False
            main_menu_setup()
        elif button('S E T T I N G S', *button_layout_4[2], click):
            settings_menu()
            main_menu_setup()
        elif button('Q U I T  G A M E', *button_layout_4[3], click): sys.exit()
        if start_game:
            while start_game: start_game = game() == 'Restart'
            main_menu_setup()
        pygame.display.update(button_layout_4)
        clock.tick(60)


def settings_menu():
    SCREEN.fill(WHITE)
    text_surf, text_rect = text_objects('Settings', MENU_TEXT)
    text_rect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 4))
    SCREEN.blit(text_surf, text_rect)
    pygame.display.update()
    first_run = draw_bg_toggle = draw_jump_toggle = draw_show_fps = True
    while True:
        click = False
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and (event.key == K_F4 and (pressed_keys[K_LALT] or pressed_keys[K_RALT])
                      or event.key == K_q))
            if event.type == QUIT or alt_f4: sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE: return
            elif event.type == MOUSEBUTTONDOWN: click = True
        if toggle_btn('Background Music', *button_layout_4[0], click, enabled=config['background_music'],
                      draw_toggle=draw_bg_toggle, blit_text=first_run):
            config['background_music'] = not config['background_music']
            save_config()
            draw_bg_toggle = True
        elif toggle_btn('Jump Sound', *button_layout_4[1], click, enabled=config['jump_sound'],
                        draw_toggle=draw_jump_toggle, blit_text=first_run):
            config['jump_sound'] = not config['jump_sound']
            save_config()
            draw_jump_toggle = True
        elif toggle_btn('Show FPS', *button_layout_4[2], click, enabled=config['show_fps'],
                        draw_toggle=draw_show_fps, blit_text=first_run):
            config['show_fps'] = not config['show_fps']
            save_config()
            draw_show_fps = True
        elif button('B A C K', *button_layout_4[3], click): return
        else: draw_bg_toggle = draw_jump_toggle = draw_show_fps = False
        first_run = False
        pygame.display.update(button_layout_4)
        clock.tick(60)
