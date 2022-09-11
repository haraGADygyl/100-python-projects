import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.BLACK+Back.YELLOW+'some sting')
print(Fore.RED+Back.RESET+'some sting')
print(Fore.GREEN+Back.RESET+'some sting')
print(Fore.MAGENTA+Back.RESET+'some sting')
print(Fore.BLACK+Back.CYAN+'some sting')
