import ossaudiodev

def main():
    print("hello world")
    print(ossaudiodev.get_device_info())
    print(ossaudiodev.get_default_input_device_info())
    print(ossaudiodev.get_default_output_device_info())
    print(ossaudiodev.get_device_info_by_name("default"))
    