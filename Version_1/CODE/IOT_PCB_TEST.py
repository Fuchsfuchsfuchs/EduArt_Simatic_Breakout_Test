import mraa
import time

# Konfiguration
digital_out_phase1 = [1, 2, 3, 4, 5, 6]     # D1–D6
analog_inputs      = [0, 1, 2, 3, 4, 5]     # A0–A5
digital_out_phase2 = [7, 8, 9, 10, 11, 12]  # D7–D12

analog_threshold = 0.5  # Wert von 0.0–1.0 (z. B. ~2.5V bei 5V Referenz)

# === Phase 1: D1–D6 nacheinander HIGH schalten ===
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

# === Phase 2: Analoge Eingänge prüfen ===
print("Phase 2: A0–A5 auf HIGH prüfen (analog > threshold)")
any_high = False
for aio_pin in analog_inputs:
    try:
        aio = mraa.Aio(aio_pin)
        raw = aio.read()  # z. B. 0–1023 bei 10-bit ADC
        max_adc = 1023     # Setze passend zu deinem Board
        voltage_ratio = raw / max_adc
        print(f"A{aio_pin} = {voltage_ratio:.2f} (Rohwert: {raw})")
        if voltage_ratio >= analog_threshold:
            any_high = True
    except Exception as e:
        print(f"Fehler beim Lesen von A{aio_pin}: {e}")

# === Phase 3: Falls HIGH anliegt, D7–D12 HIGH setzen ===
if any_high:
    print("HIGH erkannt an A0–A5 – D7–D12 auf HIGH setzen")
    for pin_num in digital_out_phase2:
        try:
            pin = mraa.Gpio(pin_num)
            pin.dir(mraa.DIR_OUT)
            pin.write(1)
            print(f"D{pin_num} -> HIGH")
            time.sleep(0.2)
        except Exception as e:
            print(f"Fehler bei D{pin_num}: {e}")
else:
    print("Kein HIGH an A0–A5 erkannt – D7–D12 bleiben LOW")


# === Phase 3: bisschen warten jaja

time.sleep(5)

# === Abschließend: Alle verwendeten digitalen Pins rückwärts auf LOW setzen ===

all_pins = digital_out_phase1 + digital_out_phase2
all_pins.reverse()  # Reihenfolge umdrehen

print("Alle digitalen Ausgänge rückwärts zurück auf LOW setzen...")
for pin_num in all_pins:
    try:
        pin = mraa.Gpio(pin_num)
        pin.dir(mraa.DIR_OUT)
        pin.write(0)
        print(f"D{pin_num} -> LOW")
        time.sleep(0.2)
    except Exception as e:
        print(f"Fehler beim Zurücksetzen von D{pin_num}: {e}")

