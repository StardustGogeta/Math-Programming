import cpu

mappers = {0:'NROM',1:'MMC1',2:'UNROM',3:'CNROM',4:'MMC3',5:'MMC5'}

def romCheck(path):
    with open(path,encoding='ascii',errors='replace') as ROM:
        ROM = ROM.read()
        if ROM[:4] != 'NES\x1a':
            print('The cartridge is not of the iNES format.')
        else:
            print('The cartridge is of the correct iNES format.')
            
            print(repr(ROM[:16]))
            prgROM_length = ord(ROM[4])
            print('The PRG ROM size is',prgROM_length,'16-KB blocks.')
            print('The CHR ROM size is',ord(ROM[5]),'8-KB blocks.')
            f6 = ord(ROM[6])
            print('The flag 6 is',bin(f6)[2:])
            mirroring = 'vertical' if f6 % 2 else 'horizontal'
            prgRAM = f6 % 4 > 1
            trainer = f6 % 8 > 3
            fourScreen = f6 % 16 > 7
            print(mirroring,prgRAM,trainer,fourScreen)
            print('The flag 7 is',bin(ord(ROM[7]))[2:])
            print('The PRG RAM size is',ord(ROM[8]) if ord(ROM[8])>0 else 1,'8-KB blocks.')
            mapper = f6>>4|ord(ROM[7])>>4<<4
            print('The mapper number is',mapper)
            print('This mapper is known as',mappers.get(mapper,'(not implemented)'))
            # TODO: Implement proper mapper support.
            
            #for x in ROM[int('fffc',16)-32768:int('fffe',16)-32768]: print(hex(ord(x)))
            #print(repr(ROM[int('fffc',16)-32768:int('fffe',16)-32768]))
            return prgROM_length

def loadROM(path):
    with open(path,encoding='ascii',errors='replace') as ROM:
        ROM = ROM.read()
        for x in range(len(cpu.prgROM)):
            cpu.prgROM[x] = ROM[x+16]
            

        
#>>> bytearray.fromhex('4e45531a')
#   bytearray(b'NES\x1a')
