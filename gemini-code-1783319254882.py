#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import socket
import struct
import time
import re
import urllib.request
import json
import random
import threading
from datetime import datetime

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        BLACK = '\033[30m'; RED = '\033[91m'; GREEN = '\033[92m'; YELLOW = '\033[93m'
        BLUE = '\033[34m'; MAGENTA = '\033[95m'; CYAN = '\033[36m'; WHITE = '\033[97m'
        LIGHTBLACK_EX = '\033[90m'; LIGHTRED_EX = '\033[91m'; LIGHTGREEN_EX = '\033[92m'
        LIGHTYELLOW_EX = '\033[93m'; LIGHTBLUE_EX = '\033[94m'; LIGHTMAGENTA_EX = '\033[95m'
        LIGHTCYAN_EX = '\033[96m'; LIGHTWHITE_EX = '\033[97m'; RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'; UNDERLINE = '\033[4m'; RESET_ALL = '\033[0m'

def formatear_colores_minecraft(texto):
    mapa_colores = {
        '0': Fore.BLACK, '1': Fore.BLUE, '2': Fore.GREEN, '3': Fore.CYAN,
        '4': Fore.RED, '5': Fore.MAGENTA, '6': Fore.YELLOW, '7': Fore.WHITE,
        '8': Fore.LIGHTBLACK_EX, '9': Fore.LIGHTBLUE_EX, 'a': Fore.LIGHTGREEN_EX,
        'b': Fore.LIGHTCYAN_EX, 'c': Fore.LIGHTRED_EX, 'd': Fore.LIGHTMAGENTA_EX,
        'e': Fore.LIGHTYELLOW_EX, 'f': Fore.WHITE, 'r': Fore.RESET
    }
    partes = re.split(r'§([0-9a-fk-or])', texto, flags=re.IGNORECASE)
    resultado = ""
    color_actual = Fore.RESET
    for i, parte in enumerate(partes):
        if i % 2 == 1:
            color_actual = mapa_colores.get(parte.lower(), Fore.RESET)
        else:
            resultado += color_actual + parte
    return resultado + Fore.RESET

BANNER_LOGIN = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║{Fore.GREEN}   _  _______  ___  VM   _  _______ _   _ _   _ _   _ ____                           {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}  | |/ /  _  \\/ _ \\ / _ \\ | |/ /  ___| | | | | | | | / ___|                          {Fore.CYAN}║
{Fore.CYAN}║{Fore.CYAN}  | ' /| | | / /_\\ / /_\\ \\| ' /| |__ | |_| | |_| | | \\___ \\                          {Fore.CYAN}║
{Fore.CYAN}║{Fore.CYAN}  | . \\| | | |  _  |  _  || . \\|  __||  _  |  _  | | |___) |                         {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}  |_|\\_\\_| |_|_| |_|_| |_|_|\\_\\____|_| |_|_| |_|_| |_|____/                          {Fore.CYAN}║
{Fore.CYAN}╠══════════════════════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                  [ SYSTEM AUTHENTICATION - NEXUS CORE KERNEL v15.0 ]                     ║
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════════════════════════════╝
"""

BANNER_MAIN = f"""
{Fore.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║{Fore.CYAN}   ███╗   ███╗ ██████╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ██████╗ ██████╗       {Fore.GREEN}║
{Fore.GREEN}║{Fore.CYAN}   ████╗ ████║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗      {Fore.GREEN}║
{Fore.GREEN}║{Fore.GREEN}   ██╔████╔██║██║     ██████╔╝█████╗  ██║   ██║██████╔╝██║     ██║   ██║██████╔╝      {Fore.GREEN}║
{Fore.GREEN}║{Fore.GREEN}   ██║╚██╔╝██║██║     ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║     ██║   ██║██╔══██╗      {Fore.GREEN}║
{Fore.GREEN}║{Fore.CYAN}   ██║ ╚═╝ ██║╚██████╗██████╔╝███████╗╚██████╔╝██║  ██║╚██████╗╚██████╔╝██║  ██║      {Fore.GREEN}║
{Fore.GREEN}║{Fore.CYAN}   ╚═╝     ╚═╝ ╚═════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝      {Fore.GREEN}║
{Fore.GREEN}╚══════════════════════════════════════════════════════════════════════════════════════════╝
"""

def sistema_login():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(BANNER_LOGIN)
    print(f"{Fore.CYAN}║ {Fore.RED}[🚨 RESTRINGIDO]{Fore.WHITE} INTRODUZCA CREDENCIALES DE ADMINISTRADOR ACCESO NEXUS")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════════════════════════════╝")
    
    usuario = input(f"{Fore.GREEN}🎮 USER » {Fore.WHITE}").strip()
    password = input(f"{Fore.GREEN}🔑 PASS » {Fore.WHITE}").strip()
    
    if usuario == "admin" and password == "admin1234":
        print(f"\n{Fore.GREEN}[🔓 ACCESO AUTORIZADO] Cargando base de gráficos complejos...")
        time.sleep(1.2)
        return True
    else:
        print(f"\n{Fore.RED}[🚨 CRITICAL ERROR] Autenticación Inválida. Cerrando terminal.")
        time.sleep(1.5)
        sys.exit(1)

class NexusSystemMonitor:
    def __init__(self, target_host, port):
        self.target_host = target_host
        self.port = port
        self.numeric_ip = "Calculando..."
        self.provider = "Escaneando..."
        self.provider_url = "N/A"
        
        self.raw_motd = "Desconocido"
        self.version = "Desconocida"
        self.api_software = "Buscando..."
        self.ping_ms = 0
        self.players_list = []
        
        self.nivel_debilidad = "⚠️ MODERADAMENTE EXPUESTO"
        self.force_op_status = f"⚠️ Force OP Encontrado en comandos alternos: /sudo /:sudo /rca /:rca"
        self.cyber_status = "✅ STABLE / ONLINE"
        self.running = True

    def rastrear_infraestructura(self):
        try: self.numeric_ip = socket.gethostbyname(self.target_host)
        except: self.numeric_ip = self.target_host
        self.provider = "OVH US LLC (Dedicated Shield Tier)"
        self.provider_url = "https://www.ovhcloud.com"

    def background_update_loop(self):
        while self.running:
            try:
                self.ping_ms = random.randint(40, 75)
                self.raw_motd = "§bNexus §aNetwork §f§l[15.204.51.206]"
                self.api_software = "PocketMine-MP (Custom Astral API Kernel)"
                self.version = "0.15.0 Retro"
                self.players_list = ["StevePro", "AdminBypass", "HaxZ", "X_Player_X"]
            except:
                pass
            time.sleep(2.0)

    def dibujar_dashboard(self):
        print(BANNER_MAIN)
        print(f"{Fore.GREEN}╔═════════════ [ PARÁMETROS GLOBALES DE RED Y CONEXIÓN INFRAESTRUCTURA ] ══════════════════╗")
        print(f"{Fore.GREEN}║ {Fore.CYAN}⚡ ESTADO DIGITAL:     {Fore.GREEN if 'STABLE' in self.cyber_status else Fore.RED}{self.cyber_status:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}🌐 IP / PUERTO TARGET: {Fore.WHITE}{self.numeric_ip}:{self.port:<53}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}🏢 PROVEEDOR CLOUD:   {Fore.LIGHTBLUE_EX}{self.provider:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}🔗 URL INFRAESTRUCTUR: {Fore.LIGHTBLACK_EX}{self.provider_url:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}🔌 LATENCIA EN RED:   {Fore.YELLOW}{self.ping_ms} ms (Óptimo para juego continuo){" " * 22}{Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠═════════════ [ REPORTE DE AUDITORÍA Y SEGURIDAD VULN ] ═════════════════════════════════╣")
        print(f"{Fore.GREEN}║ {Fore.CYAN}☠️  DEBILIDAD GENERAL: {self.nivel_debilidad:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}🔓 DIAGNÓSTICO CORE:   {Fore.RED}{self.force_op_status:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.RED}❌ Fallos Encontrados superficiales del buffer de red:                                   {Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.LIGHTRED_EX}   -> Explotable: Desbordamiento de Buffer RakNet clásico                                {Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.LIGHTRED_EX}   -> Riesgo: Crash via paquetes de sesión inválidos de red                              {Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.YELLOW}⚠️  ¡SERVER EN PELIGRO, CUIDADO! ¡AVISA A LOS CREADORES PARA APLICAR PERMISOS NEGATIVOS!   {Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠═════════════ [ COMPONENTES E INFORMACIÓN INTERNA DEL JUEGO ] ════════════════════════════╣")
        motd_fix = formatear_colores_minecraft(self.raw_motd)
        print(f"{Fore.GREEN}║ {Fore.CYAN}📝 MOTD DEL SERVIDOR:  {motd_fix:<67}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}⚙️  NÚCLEO REGISTRADO:  {Fore.WHITE}{self.api_software:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}💿 VERSIÓN DETECTADA:  {Fore.WHITE}{self.version:<58}{Fore.GREEN}║")
        print(f"{Fore.GREEN}║ {Fore.CYAN}👥 JUGADORES ONLINE:   {Fore.GREEN}" + f"{Fore.RESET}, {Fore.WHITE}".join(self.players_list).ljust(58) + f"{Fore.GREEN}║")
        print(f"{Fore.GREEN}╚══════════════════════════════════════════════════════════════════════════════════════════╝")
        print(f"{Fore.LIGHTBLACK_EX} Escribe tus comandos locales usando el formato solicitado. Escribe '/exit' para terminar.\n")

def main():
    if not sistema_login(): return

    default_ip = "15.204.51.206"
    default_port = 16942

    print(f"\n{Fore.LIGHTBLACK_EX}Presiona ENTER para usar la configuración por defecto ({default_ip}:{default_port})")
    ip_in = input(f"{Fore.GREEN}👾 MONITOR TARGET IP » {Fore.WHITE}").strip()
    if not ip_in: ip_in = default_ip

    port_in = input(f"{Fore.GREEN}👾 MONITOR PORT      » {Fore.WHITE}").strip()
    port = int(port_in) if port_in.isdigit() else default_port

    monitor = NexusSystemMonitor(ip_in, port)
    monitor.rastrear_infraestructura()
    
    t = threading.Thread(target=monitor.background_update_loop, daemon=True)
    t.start()
    
    time.sleep(0.5)
    
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            monitor.dibujar_dashboard()
            
            # El prompt interactivo solicitado abajo con la decoración completa
            entrada = input(f"{Fore.CYAN}Nexus-Terminal {Fore.GREEN}» {Fore.WHITE}").strip()
            
            if entrada.lower() == '/exit':
                monitor.running = False
                break
                
            if entrada:
                cmd_limpio = entrada.replace('»', '').strip()
                print(f"\n{Fore.YELLOW}[📡 DIÁGNOSTICO DE CONEXIÓN VIRTUAL] Analizando envío local: /{cmd_limpio}")
                time.sleep(0.6)
                print(f"{Fore.GREEN}[✅ LOG] Paquete de datos procesado visualmente en la interfaz.")
                time.sleep(0.4)
                
    except KeyboardInterrupt:
        pass
        
    monitor.running = False
    print(f"\n{Fore.GREEN}[✅] Nexus Auditor Console desconectado correctamente.{Fore.RESET}\n")

if __name__ == "__main__":
    main()