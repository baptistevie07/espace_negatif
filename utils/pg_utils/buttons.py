import pygame

pygame.font.init()

class Button:
    def __init__(self, rect, text, font, on_color, off_color, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(rect) if not isinstance(rect, pygame.Rect) else rect
        self.text = text
        self.font = font
        self.on_color = on_color
        self.off_color = off_color
        self.text_color = text_color
        self.active = False  # État ON/OFF

    def draw(self, screen):
        color = self.on_color if self.active else self.off_color
        pygame.draw.rect(screen, color, self.rect)
        txt_surface = self.font.render(self.text, True, self.text_color)
        txt_rect = txt_surface.get_rect(center=self.rect.center)
        screen.blit(txt_surface, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active  # On/Off toggle
                return True
        return False
    
class Parametres():
    def __init__(self):
        self.buttons = {}
    def add_button(self, label,text,width):
        i = len(self.buttons)
        button = Button(
            rect=(width + 25, 10 + i * 60,100, 50),  # Position et taille par défaut
            text=text,
            font=pygame.font.Font(None, 24),
            on_color=(0, 255, 0),
            off_color=(255, 0, 0)
        )
        self.buttons[label] = button
    def draw_params(self, screen):
        for button in (self.buttons.values()):
            button.draw(screen)  # Positionnement vertical des boutons
    def handle_event(self, event):
        for btn in self.buttons.values():
            result = btn.handle_event(event)
           

