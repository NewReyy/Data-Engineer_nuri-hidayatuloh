import sys

class MeanCalculatorReducer:
    
    def __init__(self):
        # Inisialisasi total jumlah nilai dan total jumlah elemen
        self.total_sum = 0
        self.total_count = 0
    
    def process_input(self, line):
        # Mendapatkan total nilai dan jumlah elemen dari baris input
        total, count = map(float, line.strip().split('\t'))
        
        # Menambahkan total nilai dan jumlah elemen ke variabel total
        self.total_sum += total
        self.total_count += count
    
    def calculate_mean(self):
        # Menghitung rata-rata dari total nilai dan total jumlah elemen
        return self.total_sum / self.total_count

if __name__ == "__main__":
    # Membuat objek reducer
    mean_calculator = MeanCalculatorReducer()
    
    # Membaca input dari standar input dan memprosesnya dengan reducer
    for line in sys.stdin:
        mean_calculator.process_input(line)
    
    # Menghitung rata-rata dan mengeluarkannya sebagai output
    mean = mean_calculator.calculate_mean()
    print("Rata-rata:", mean)