import datetime
import time
import os
import platform
import playsound

def play_alarm_sound():
    """
    Play the alarm sound when the alarm goes off.
    """
    # The sound file path (replace with your own sound file)
    sound_file = "alarm_sound.mp3"

    try:
        # Use the playsound library to play the sound
        playsound.playsound(sound_file)
    except Exception as e:
        print(f"Error playing alarm sound: {e}")

def set_alarm(hour, minute):
    """
    Set an alarm for a specific hour and minute.

    Args:
    - hour (int): The hour of the alarm (24-hour format).
    - minute (int): The minute of the alarm.
    """
    # Get the current date and time
    now = datetime.datetime.now()

    # Set the alarm time for the next occurrence of the specified hour and minute
    alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute)

    # Calculate the time difference until the alarm
    time_difference = (alarm_time - now).total_seconds()

    # Sleep until the alarm time
    time.sleep(time_difference)

    # Display a message when the alarm goes off
    print("\nAlarm Time! Wake up!")

    # Play the alarm sound
    play_alarm_sound()

def alarm_clock():
    print("Welcome to the Alarm Clock!")

    # Get the user input for the alarm time
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))

    # Validate the input
    if not (0 <= hour < 24 and 0 <= minute < 60):
        print("Invalid input. Please enter a valid time.")
        return

    print(f"Alarm set for {hour:02d}:{minute:02d}")

    # Set the alarm
    set_alarm(hour, minute)

if __name__ == "__main__":
    # Run the Alarm Clock
    alarm_clock()
