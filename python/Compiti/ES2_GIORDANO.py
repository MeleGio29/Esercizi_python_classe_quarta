class IPAddress():
    def __init__(self, ip):
        self.ip = ip

    def dec2bin(numero,nbit):
        numeroBin = bin(numero)[2:]
        n = "0" * (nbit-len(numeroBin))+numeroBin
        return n

    def IP_dec2bin(self):
        pezzi,finale = self.ip.split(".")," "
        for cella in pezzi:
            finale += str(self.ip.dec2bin(int(cella), 8))
        return finale

    def controllo(self):
        pezzi, ok = self.ip.split(","), True
        for cella in pezzi:
            if (int(cella)) > 255:
                ok = False
                break
        return ok

    def isSubnet(self):
        ok = False
        for k in range(32):
            if '1' * k + '0' * (32 - k) == self.IP_dec2bin():
                ok = True
                break
        return ok

def main():
    ip = IPAddress(input("Inserisci un indirizzo IP: "))
    if ip.controllo(): print("Corretto")
    else: print("Errato")
    if ip.isSubnet(): print("E' una subnet")
    else: print("NON è una subnet")

if __name__ == "__main__":
    main()