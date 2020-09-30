import ssd1306
import framebuf
from machine import I2C, Pin
i2c = I2C(-1, Pin(12), Pin(14))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
buffer = bytearray(b'\x00\x00\x18\x28\x48\x88\xF8\x88\x48\x28\x18\x00\x00\x00\x80\x00\xC0\x00\x00\x00\x20\x40\xF8\x88\x50\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x08\xC0\x20\x10\x90\x90\xA0\x08\x18\x00\x00\xE0\x20\xF8\x08\xE8\xE8\xE8\x08\xE8\xE8\xE8\x08\xE8\xE8\xE8\x08\xF8\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x00\x0C\x00\x0E\x00\x0F\x00\x0F\x00\x0F\x00\x00\x00\x02\x01\x0F\x08\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0C\x08\x01\x02\x04\x04\x04\x03\x08\x0C\x00\x00\x03\x02\x0F\x08\x0B\x0B\x0B\x08\x0B\x0B\x0B\x08\x0B\x0B\x0B\x08\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFE\x42\x42\x42\x42\x42\x02\x02\x00\xFE\x06\x18\x60\x80\x00\x80\x60\x18\x06\xFE\x00\x00\x08\x08\xFE\x00\x00\x00\x00\x00\xF8\x04\x02\x02\x02\x02\x04\xF8\x00\x00\x00\x08\x08\xFE\x00\x00\x00\x00\x00\x00\x00\x02\x02\x02\x02\x82\x62\x1A\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1F\x00\x00\x00\x00\x00\x00\x00\x00\x1F\x00\x00\x00\x01\x06\x01\x00\x00\x00\x1F\x00\x00\x10\x10\x1F\x10\x10\x00\x00\x00\x07\x08\x10\x10\x10\x10\x08\x07\x00\x00\x00\x10\x10\x1F\x10\x10\x00\x00\x00\x18\x00\x00\x00\x18\x06\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x44\x44\x24\x98\x00\xFC\x04\x04\x04\xFC\x00\x00\x08\xFC\x00\x00\x00\x8C\x04\x24\x24\xDC\x00\x80\x00\xFC\x24\x24\x24\xFC\x00\x80\x00\x88\x44\x44\x24\x98\x00\x88\x44\x44\x24\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x00\x01\x01\x01\x01\x01\x00\x00\x01\x01\x01\x00\x00\x01\x01\x01\x81\x81\x80\x81\x80\x81\x81\x81\x01\x01\x00\x01\x00\x01\x01\x01\x01\x01\x00\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x03\x0C\x30\x0C\x03\x7F\x00\x38\x54\x54\x58\x00\x7C\x04\x04\x78\x00\x3C\x40\x40\x7C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xAA\xAA\xA8\x28\x08\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x03\x0C\x30\x0C\x03\x7F\x00\x00\x26\x49\x49\x49\x32\x00\x00\x7F\x02\x04\x08\x10\x7F\x00')
fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MVLSB)
display.fill(0)
display.framebuf.blit(fb, 0, 0)
display.show()