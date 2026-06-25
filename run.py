import sys

try:
    import dvkrfb_3
except ImportError:
    print("\033[1;31m [!] Error: dvkrfb_3.so file not found or incompatible python version!\033[0m")
    sys.exit()
