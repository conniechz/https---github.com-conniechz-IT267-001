import measure_convert as my

if __name__ == '__main__':
    print(f'{my.cm_inch(10):.2f}')
    print(f'{my.inch_cm(10):.2f}')

from measure_convert import inch_cm,cm_inch

if __name__ == '__main__':
    print(f'{cm_inch(100)}')
    print(f'{inch_cm(12.5)}')