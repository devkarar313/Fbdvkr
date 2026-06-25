import sys

try:
    import devkarar_fb
except ImportError:
    print("\033[1;31m [!] Error: devkarar_fb.so file not found or incompatible python version!\033[0m")
    sys.exit()
