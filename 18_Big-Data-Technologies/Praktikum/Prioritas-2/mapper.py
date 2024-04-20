import sys

class MeanCalculatorMapper:
    
    @staticmethod
    def process_input(line):
        # Memisahkan baris input menjadi nilai-nilai yang dipisahkan oleh koma
        values = line.strip().split(',')
        
        # Menghitung total nilai dan jumlah elemen
        total = sum(map(float, values))
        count = len(values)
        
        # Outputkan total nilai dan jumlah elemen sebagai pasangan (kunci, nilai)
        print(f"{total}\t{count}")

if __name__ == "__main__":
    # Membaca input dari standar input dan memprosesnya dengan mapper
    for line in sys.stdin:
        MeanCalculatorMapper.process_input(line)