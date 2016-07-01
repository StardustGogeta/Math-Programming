def a(address): # Finds the correct memory location based on address.
    if address < 0x100:
        return 'zeroPage[address]'
    elif address < 0x200:
        return stack[address-0x100]
    elif address < 0x800:
        return RAM[address-0x200]
    elif address < 0x2000:
        return a(address % 0x800)
    elif address < 0x4000:
        return PPU[(address-0x2000) % 0x8]
    elif address < 0x4020:
        return 'DMA['+str(address)+'-0x4000]'
    elif address < 0x6000:
        return EROM[address-0x4020]
    elif address < 0x8000:
        return SRAM[address-0x6000]
    else:
        return 'prgROM[('+str(address)+'-0x8000) % len(prgROM)]'

def memory_reset(prgROM_length):
    global zeroPage, stack, RAM, PPU, DMA, EROM, SRAM, prgROM, reg
    zeroPage = [0]*256
    stack = [0]*256
    RAM = [0]*1536
    PPU = [0]*8
    DMA = [0]*32
    EROM = [0]*8160
    SRAM = [0]*8192
    prgROM = [0]*16384*prgROM_length
    reg = {'A':0,'X':0,'Y':0,'PC':0xfffc}

def runOpcode(a):
    x = ord(a)
    if x == 0x0: # BRK
        print('BRK')
        pass
    elif x == 0x1: # ORA
        print('ORA')
        pass
    elif x == 0x5: # ORA
        print('ORA')
        pass
    elif x == 0x6: # ASL
        print('ASL')
        pass
    elif x == 0x8: # PHP
        print('PHP')
        pass
    elif x == 0x9: # ORA
        print('ORA')
        pass
    elif x == 0xa: # ASL
        print('ASL')
        pass
    elif x == 0xd: # ORA
        print('ORA')
        pass
    elif x == 0xe: # ASL
        print('ASL')
        pass
    elif x == 0x10: # BPL
        print('BPL')
        pass
    elif x == 0x11: # ORA
        print('ORA')
        pass
    elif x == 0x15: # ORA
        print('ORA')
        pass
    elif x == 0x16: # ASL
        print('ASL')
        pass
    elif x == 0x18: # CLC
        print('CLC')
        pass
    elif x == 0x19: # ORA
        print('ORA')
        pass
    elif x == 0x1d: # ORA
        print('ORA')
        pass
    elif x == 0x1e: # ASL
        print('ASL')
        pass
    elif x == 0x20: # JSR
        print('JSR')
        pass
    elif x == 0x21: # AND
        print('AND')
        pass
    elif x == 0x24: # BIT
        print('BIT')
        pass
    elif x == 0x25: # AND
        print('AND')
        pass
    elif x == 0x26: # ROL
        print('ROL')
        pass
    elif x == 0x28: # PLP
        print('PLP')
        pass
    elif x == 0x29: # AND
        print('AND')
        pass
    elif x == 0x2a: # ROL
        print('ROL')
        pass
    elif x == 0x2c: # BIT
        print('BIT')
        pass
    else: # Not implemented / Error
        print('Unrecognized code:',hex(x))
        pass

