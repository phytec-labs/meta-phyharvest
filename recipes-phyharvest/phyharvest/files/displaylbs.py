import time
import subprocess  # For running shell scripts
import os
import random
from my_panel import MyPanel

# Functions to control LEDs
def led_on(led):
    with open(f'/sys/class/leds/{led}/brightness', 'w') as f:
        f.write('1')  # Turn the LED on

def led_off(led):
    with open(f'/sys/class/leds/{led}/brightness', 'w') as f:
        f.write('0')  # Turn the LED off

def flash_leds_opposite(led1, led2, duration, interval=0.5):
    """Flash LEDs alternately (on/off at opposite times) for the specified duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        # Turn LED1 on and LED2 off
        led_on(led1)
        led_off(led2)
        time.sleep(interval)

        # Turn LED1 off and LED2 on
        led_off(led1)
        led_on(led2)
        time.sleep(interval)

# Function to get weight from the shell script
def get_weight():
    """
    Executes the shell script to retrieve the weight and returns it as an integer.
    """
    try:
        result = subprocess.check_output(['/usr/bin/readlbs.sh'], text=True).strip()
        return int(result)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run readlbs.sh: {e}")
        return None
    except ValueError:
        print("Error converting script output to integer.")
        return None

# Function to play a specific .wav file
def play_specific_wav(wav_file):
    """
    Plays a specific .wav file using aplay.
    """
    try:
        if os.path.exists(wav_file):
            print(f"Playing sound: {wav_file}")
            subprocess.run(["aplay", wav_file])
        else:
            print(f"Wav file not found: {wav_file}")
    except Exception as e:
        print(f"Error playing wav file: {e}")

# Function to play a random .wav file
def play_random_wav(wav_folder):
    """
    Plays a random .wav file from the specified folder using aplay.
    """
    try:
        wav_files = [f for f in os.listdir(wav_folder) if f.endswith(".wav")]
        if not wav_files:
            print("No .wav files found in the folder.")
            return

        selected_wav = random.choice(wav_files)
        print(f"Playing sound: {selected_wav}")
        subprocess.run(["aplay", os.path.join(wav_folder, selected_wav)])
    except Exception as e:
        print(f"Error playing wav file: {e}")

# Function to play specific goal-reached audio files
def play_goal_reached_audio():
    """Play the specific goal-reached audio files."""
    try:
        goal_audio_files = ["/usr/bin/wav/special/goal-reached1.wav", "/usr/bin/wav/special/goal-reached2.wav"]
        for audio_file in goal_audio_files:
            if os.path.exists(audio_file):
                print(f"Playing goal-reached audio: {audio_file}")
                subprocess.run(["aplay", audio_file])
            else:
                print(f"Goal-reached audio file not found: {audio_file}")
    except Exception as e:
        print(f"Error playing goal-reached audio files: {e}")

# Main function
def main():
    try:
        # Initialize the display
        lcd = MyPanel(bus=1, device=0)  # Using SPI0, device 0

        # Clear the display
        lcd.clear_screen()
        time.sleep(0.0015)  # Clear screen needs 1.5ms
        lcd.set_backlight(0x28)

        wav_folder = "/usr/bin/wav"  # Path to .wav files
        special_wav_folder = "/usr/bin/wav/special"  # Path to milestone and goal-reached .wav files
        last_weight = None  # Store the last weight value
        goal_reached = False  # Track if the goal has been reached
        milestones = {75: "quarter.wav", 150: "halfway.wav", 225: "almost.wav", 250: "final-countdown.wav"}  # Milestone sounds
        milestones_played = set()  # Track played milestones

        while True:
            # Get the current weight
            current_weight = get_weight()

            if current_weight is not None:
                print(f"Current weight: {current_weight}")

                # Play sound only if the weight has increased
                if last_weight is not None and current_weight > last_weight:
                    print("Weight has increased!")
                    play_random_wav(wav_folder)

                # Play milestone sounds when weight crosses milestones
                for milestone, wav_file in milestones.items():
                    if milestone not in milestones_played and current_weight >= milestone:
                        print(f"Milestone reached: {milestone} lbs")
                        play_specific_wav(f"{special_wav_folder}/{wav_file}")
                        milestones_played.add(milestone)

                # Check for the "Goal Reached!" condition
                if current_weight >= 301 and not goal_reached:
                    print("Goal reached!")
                    lcd.clear_screen()
                    lcd.set_cursor(0x00)
                    lcd.write_text("Goal Reached!")
                    flash_leds_opposite('led-1', 'led-2', duration=10)  # Flash LEDs alternately for 10 seconds
                    play_goal_reached_audio()
                    goal_reached = True  # Ensure goal-reached actions are only performed once

                # Update the display with the current weight
                if not goal_reached:
                    lcd.clear_screen()
                    lcd.set_cursor(0x00)
                    lcd.write_text(f"Weight: {current_weight} lbs")

                # Update the last_weight to the current weight
                last_weight = current_weight
            else:
                # Display an error if weight retrieval fails
                lcd.clear_screen()
                lcd.set_cursor(0x00)
                lcd.write_text("Weight: Error")

            # Check for changes every second
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'lcd' in locals():
            lcd.spi.close()
        # Ensure LEDs are turned off when the script ends
        led_off('led-1')
        led_off('led-2')

if __name__ == "__main__":
    main()

