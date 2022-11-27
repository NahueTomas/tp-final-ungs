#! /usr/bin/env python
import os

import pygame
from pygame.locals import *

from config.configuracion import ANCHO, ALTO
from funciones.games.normalMode import normalMode
from funciones.menu.menuInicio import menuInicio


# Programa Principal ejecuta Main
if __name__ == "__main__":
    menuInicio(ANCHO, ALTO, normalMode)
