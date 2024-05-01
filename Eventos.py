def manejar_eventos_teclado(equipo_actual, equipos, artillero, portero, switch1, switch2):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not switch1:
                    equipo_actual = (equipo_actual - 1) % len(equipos)
                elif switch1 == True:
                    portero = ...
                elif switch1 and switch2:
                    # Lógica para seleccionar el artillero a la izquierda
                    artillero = ...
            elif event.key == pygame.K_RIGHT:
                if not switch1:
                    equipo_actual = (equipo_actual + 1) % len(equipos)
                elif switch1 and switch2:
                    # Lógica para seleccionar el artillero a la derecha
                    artillero = ...
            elif event.key == pygame.K_e:  # Tecla "E" para alternar el segundo interruptor
                switch2 = not switch2  # Cambiar el estado del segundo interruptor
                switch1 = False  # Desactivar el primer interruptor al activar el segundo
            elif event.key == pygame.K_e and not switch2:  # Tecla "E" para alternar el primer interruptor
                switch1 = not switch1  # Cambiar el estado del primer interruptor
    return equipo_actual, artillero, portero, switch1, switch2