import spidev
import time

class MyPanel:
    def __init__(self, bus=1, device=0):
        self.spi_delay = 100000
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.mode = 0x3  # CPOL=1, CPHA=1 as specified in datasheet
        self.spi.max_speed_hz = 10000  # 100KHz max as per spec but we use 10K for testing

        # Initialize display
        time.sleep(0.2)  # 100ms startup delay required
        self._send_command(0xFE, 0x41)  # Display on

    def _send_command(self, prefix, cmd):
        self.spi.xfer2([prefix], self.spi.max_speed_hz, self.spi_delay)
        self.spi.xfer2([cmd], self.spi.max_speed_hz, self.spi_delay)
        time.sleep(0.002)  # Minimum 200µs delay between commands

    def _send_command_with_parameter(self, prefix, cmd, parameter):
        self.spi.xfer2([prefix], self.spi.max_speed_hz, self.spi_delay)
        self.spi.xfer2([cmd], self.spi.max_speed_hz, self.spi_delay)
        self.spi.xfer2([parameter], self.spi.max_speed_hz, self.spi_delay)
        time.sleep(0.002)  # Minimum 200µs delay between commands

    def write_text(self, text):
        for char in text:
            self.spi.xfer2([ord(char)], self.spi.max_speed_hz, self.spi_delay)
            time.sleep(0.002)  # 100µs execution time

    def set_cursor(self, position):
        self._send_command_with_parameter(0xFE, 0x45, position)
        time.sleep(0.002)

    def set_backlight(self, brightness):
        self._send_command_with_parameter(0xFE, 0x53, brightness)

    def clear_screen(self):
        self._send_command(0xFE, 0x51)
        time.sleep(0.002)

    def turn_on_underline_cursor(self):
        self._send_command(0xFE, 0x47)
        time.sleep(0.2)

    def turn_off_underline_cursor(self):
        self._send_command(0xFE, 0x48)
        time.sleep(0.2)