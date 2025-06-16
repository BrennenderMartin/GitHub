from playsound import playsound
import subprocess
import os

def play_media_file(filepath):
    if not os.path.isfile(filepath):
        print(f"File does not exist: {filepath}")
        return

    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == ".mp3":
        try:
            proc = subprocess.Popen(filepath)
        except Exception as e:
            print(f"Error playing mp3: {e}")
    elif ext == ".mp4":
        try:
            # Platform-specific: this one is for Windows, adjust if needed
            if os.name == 'nt':  # Windows
                os.startfile(filepath)
            elif os.name == 'posix':  # Unix/Linux/Mac
                subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", filepath])
        except Exception as e:
            print(f"Error playing mp4: {e}")
    else:
        print(f"Unsupported file type: {ext}")

# Example usage (will not actually run media playback in this environment)
example_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds", "test2", "01_rülps.mp3")
play_media_file(example_path)

