# Author: Muhammad Fiqri
# Date: 2023-09-1
# Description: Convert binary to decimal
# GitHub: https://github.com/Muhammad-Fiqri

def main():
    binary = input_binary()
    print("inputed binary: ",binary)

    decimal = convert_binary(binary)
    print("converted binary into decimal : ",decimal)

def input_binary():
    binary = input("Enter a binary number: ")
    if len(binary) > 8:
        print("Error: binary number too long")
        print()
        binary = ""
        input_binary()
    return binary

def convert_binary(binary):
    result = 0 # to store decimal result
    index = 0 # index of binary number
    dec_chunks = 0 # to store converted binary chunks of each index

    # start at last list, and work backwards
    # set dec_chunks to binary * 2^index
    # add index + 1 for next binary loop
    # add dec_chunks to result
    for i in reversed(binary):
        print("index: ",index,", binary: ",i)
        dec_chunks = int(i) * 2**index
        index += 1
        print("dec_chunks: ",dec_chunks)
        result += dec_chunks
        print("result: ",result)
        print()
    
    return result

main()