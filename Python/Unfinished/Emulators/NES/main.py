import cartridge, cpu

# Pieces:
# 1: CPU
# 2: PPU
# 3: pAPU
# 4: RAM
# 5: Game ROM and Mappers
# 6: Controller Interface
# 7: Accessories, etc.


# Inputting a cartridge.
path = 'Starwars.nes' # input("What is the ROM filepath?")
prgROM_length = cartridge.romCheck(path)

print(prgROM_length)
cpu.memory_reset(prgROM_length)
print(cpu.prgROM[0x7ff0:0x8000])
cpu.prgROM[(65532-0x8000) % len(cpu.prgROM)] = 3
print(cpu.prgROM[0x7ff0:0x8000])
cpu.memory_reset(prgROM_length)
print(cpu.prgROM[0x7ff0:0x8000])

cartridge.loadROM(path)

print(cpu.prgROM[:6])
for x in cpu.prgROM[:100]:
    cpu.runOpcode(x)
