from getting_coordinates import  generate_city
import random
import pygame
import os

city = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань',
             'Нижний Новгород', 'Челябинск', 'Самара', 'Омск','Ростов-на-Дону',
             'Уфа', 'Красноярск', 'Воронеж', 'Пермь', 'Волгоград', 'Краснодар',
             'Саратов', 'Тюмень', 'Тольятти', 'Ижевск']


name_city = random.choice(city)
response = generate_city(name_city)
pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True

if response:
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    os.remove(map_file)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            name_city = random.choice(city)
            response = generate_city(name_city)
            if response:
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
                os.remove(map_file)
pygame.quit()