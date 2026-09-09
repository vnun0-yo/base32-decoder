#!/usr/bin/env python3
"""
Base64 Tool - A simple tool to encode and decode text using Base64
Using optparse instead of argparse
"""


banner = """
██╗   ██╗███████╗███╗   ██╗
╚██╗ ██╔╝██╔════╝████╗  ██║
 ╚████╔╝ █████╗  ██╔██╗ ██║
  ╚██╔╝  ██╔══╝  ██║╚██╗██║
   ██║   ███████╗██║ ╚████║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝
"""
print(banner)


import base64
import sys
import re
from optparse import OptionParser


RED = "\033[1;31m"
GREEN = "\033[1;32m"



def encode_text(text):
   
    try:
        encoded_bytes = base64.b32encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"{RED}Encoding error: {e}"

def decode_text(text):

    try:
        decoded_bytes = base64.b32decode(text)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"{RED}Decoding error: {e}"

def main():
    
    parser = OptionParser(
        usage="Usage: %prog [options]",
        description="Base32 Encoder/Decoder Tool",
        epilog="Example: %prog -e 'Hello World'"
    )
    
    
    parser.add_option(
        "-e", "--encode", 
        dest="encode", 
        type="string", 
        help="Encode text to Base32",
        metavar="Text"
    )
    
    parser.add_option(
        "-d", "--decode", 
        dest="decode", 
        type="string", 
        help="Decode text from Base32",
        metavar="Text"
    )
    
    parser.add_option(
        "-o", "--output", 
        dest="output", 
        type="string", 
        help="Write result to file instead of stdout",
        metavar="File"
    )
    
    
    (options, args) = parser.parse_args()
    
    
    if not options.encode and not options.decode:
        parser.print_help()
        print(f"\n{RED}Error: You must specify -e or -d")
        sys.exit(1)
    
    
    result = None
    operation = None
    
    if options.encode:
        operation = "encode"
        result = encode_text(options.encode)
    
    elif options.decode:
        operation = "decode"
        result = decode_text(options.decode)
    
    
    if result:
        
        if result.startswith("Encoding error") or result.startswith("Decoding error"):
            print(f"{RED}{result}")
            sys.exit(1)
        
        
        if options.output:
            try:
                with open(options.output, 'w') as f:
                    f.write(result)
                print(f"{GREEN}Result written to {options.output}")
                print(f"{GREEN}{operation.capitalize()} result: {result[:50]}..." if len(result) > 50 else f"[+] {operation.capitalize()} result: {result}")
            except Exception as e:
                print(f"{RED}Error writing to file: {e}")
                print(f"{GREEN}{operation.capitalize()} result: {result}")
        else:
            print(f"{GREEN}{operation.capitalize()} result: {result}")
    else:
        print(f"{RED}No result generated")
        sys.exit(1)

if __name__ == "__main__":
    main()
