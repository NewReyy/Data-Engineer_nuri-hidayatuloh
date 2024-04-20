#!/usr/bin/env python3
import sys

class PalindromeCheckerMapper:
    
    @staticmethod
    def is_palindrome(word):
        # Fungsi untuk mengecek apakah kata merupakan palindrom atau tidak
        return word == word[::-1]
    
    @staticmethod
    def process_input(line):
        # Menghapus karakter newline dan mendapatkan kata dari baris input
        word = line.strip()
        
        # Mengecek apakah kata merupakan palindrom atau tidak
        is_palindrome = PalindromeCheckerMapper.is_palindrome(word)
        
        # Outputkan kata dan hasil pengecekan palindrom sebagai pasangan (kunci, nilai)
        print(f"{word}\t{is_palindrome}")

if __name__ == "__main__":
    # Membaca input dari standar input dan memprosesnya dengan mapper
    for line in sys.stdin:
        PalindromeCheckerMapper.process_input(line)