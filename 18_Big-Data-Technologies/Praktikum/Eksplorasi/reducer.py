#!/usr/bin/env python3
import sys

class PalindromeCheckerReducer:
    
    @staticmethod
    def process_input(line):
        # Memisahkan baris input menjadi bagian-bagian
        line_parts = line.strip().split('\t')
        
        # Memeriksa apakah baris memiliki format yang diharapkan
        if len(line_parts) == 2:
            word, is_palindrome = line_parts
            print(f"{word}\t{is_palindrome}")
        else:
            # Mencetak pesan kesalahan ke stderr
            print("Format input tidak valid:", line.strip(), file=sys.stderr)

if __name__ == "__main__":
    # Membaca input dari standar input dan memprosesnya dengan reducer
    for line in sys.stdin:
        PalindromeCheckerReducer.process_input(line)