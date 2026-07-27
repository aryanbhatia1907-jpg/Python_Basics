with open('myfile.txt','r') as f:
    print(type(f))

    f.seek(10)          # seek mein jitne character dalenge utne character [ including spaces] ko skip karke agle ko print karega
    print(f.tell())     # Tell batata hai ki humne kitne character/bytes seek kare or kahan prr hai abhi hum
    data=f.read(10)     # isme 10 ka matlb hai ki agle 10 character ko print kardo
    print(data)
