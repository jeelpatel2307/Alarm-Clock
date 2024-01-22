# Alarm Clock

Welcome to the Alarm Clock! This Python program allows you to set an alarm for a specific time, displaying a message and playing an alarm sound when the time arrives.

## How to Use

1. Run the script.
2. Enter the desired alarm time in 24-hour format when prompted.
3. The program will display a message and play an alarm sound when the specified time arrives.

## Features

### `play_alarm_sound()` Function

- Plays the alarm sound when the alarm goes off.
- Uses the `playsound` library to play the sound file.

### `set_alarm(hour, minute)` Function

- Sets an alarm for a specific hour and minute.
- Calculates the time difference until the alarm and sleeps until that time.
- Displays a message and plays the alarm sound when the alarm goes off.

### `alarm_clock()` Function

- Main function that runs the Alarm Clock.
- Takes user input for the alarm time.
- Validates the input and sets the alarm using the `set_alarm` function.

## Usage

```bash
python alarm_clock.py
```

Follow the on-screen instructions to set and experience the alarm.

## Requirements

- [playsound](https://pypi.org/project/playsound/): Library for playing sound files.

## Author

Jeel patel
