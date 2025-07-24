import mraa
import time

# Konfiguration
digital_out_phase1 = [1, 2, 3, 4, 5, 6]     # D1–D6
analog_inputs      = [0, 1, 2, 3, 4, 5]     # A0–A5
digital_outputs    = [7, 8, 9, 10, 11, 12]  # D7–D12 (zugeordnet zu A0–A5)

analog_threshold = 0.5  # Schwelle für analog HIGH (z. B. 2.5V bei 5V)

# === Phase 1: D1–D6 nacheinander HIGH setzen ===
print("Phase 1: D1–D6 nacheinander auf HIGH setzen")
for pin_num in digital_out_phase1:
    try:
        pin = mraa.Gpio(pin_num)
        pin.dir(mraa.DIR_OUT)
        pin.write(1)
        print(f"D{pin_num} -> HIGH")
        time.sleep(0.2)
    except Exception as e:
        print(f"Fehler bei D{pin_num}: {e}")

# === Phase 2: A0–A5 lesen und zugehörige D7–D12 setzen ===
print("Phase 2: A0–A5 lesen und direkt zugeordnete D7–D12 setzen")
max_adc = 1023  # Maximalwert des ADC (abhängig vom Board)

# Merken, welche digitalen Pins gesetzt wurden
used_digital_outputs = []

for i in range(len(analog_inputs)):
    aio_pin = analog_inputs[i]
    d_pin   = digital_outputs[i]
    try:
        aio = mraa.Aio(aio_pin)
        raw = aio.read()
        voltage_ratio = raw / max_adc
        print(f"A{aio_pin} = {voltage_ratio:.2f} (Rohwert: {raw})")
        time.sleep(0.2)
        if voltage_ratio >= analog_threshold:
            pin = mraa.Gpio(d_pin)
            pin.dir(mraa.DIR_OUT)
            pin.write(1)
            used_digital_outputs.append(d_pin)
            print(f"A{aio_pin} HIGH erkannt -> D{d_pin} -> HIGH")
        else:
            print(f"A{aio_pin} unterhalb der Schwelle – D{d_pin} bleibt LOW")
    except Exception as e:
        print(f"Fehler bei A{aio_pin}/D{d_pin}: {e}")

# === Warten ===
time.sleep(5)

# === Alle verwendeten digitalen Pins rückwärts auf LOW setzen ===
all_pins = digital_out_phase1 + used_digital_outputs
all_pins = list(set(all_pins))  # doppelte vermeiden
all_pins.sort(reverse=True)    # absteigend sortieren

print("Alle verwendeten digitalen Ausgänge rückwärts auf LOW setzen...")
for pin_num in all_pins:
    try:
        pin = mraa.Gpio(pin_num)
        pin.dir(mraa.DIR_OUT)
        pin.write(0)
        print(f"D{pin_num} -> LOW")
        time.sleep(0.2)
    except Exception as e:
        print(f"Fehler beim Zurücksetzen von D{pin_num}: {e}")

