from scanner.library import ScanningService

# Boilerplate code, need to finish this up


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    localhost = ScanningService(target='127.0.0.1', ports='22,23,24,25,100')
    localhost.scan()


