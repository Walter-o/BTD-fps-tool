from struct import pack, unpack


class Converter:
    title = "--- Walter's Bloons TD fps tool ---"

    defaultFPS = "111111111111913F"  # 60 fps

    @staticmethod
    # Converts a double-precision floating point number to a hex value
    # Credit to Jonathon https://stackoverflow.com/questions/23624212
    def doubleToHex(f):
        # Made an edit here to reverse endianness for BTD
        #                             v
        return hex(unpack('<Q', pack('>d', f))[0])

    # Returns a nice representation of the hex edit you need to do
    def getHexEdit(self, desiredFps):
        hexEdit = str(self.doubleToHex(1 / desiredFps))[2:].upper().rjust(16, "1")
        return f"{self.defaultFPS} => {hexEdit}\n"

    # Wait for next command
    def awaitCommand(self):
        print(self.title)
        while True:
            command = input("Type desired fps number or 'exit': ")
            if command.isdigit():
                print(self.getHexEdit(desiredFps=int(command)))
            elif command == "exit":
                exit(0)