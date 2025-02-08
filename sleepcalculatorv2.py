from datetime import datetime, timedelta

extraSleepTime = 0

def get_wakeup_time():
    while True:
        user_input = input("Enter your desired wake-up time (e.g., '07:30 AM' or '19:30'): ")
        # Try parsing with multiple possible formats
        for fmt in ("%I:%M %p", "%H:%M"):
            try:
                parsed_time = datetime.strptime(user_input, fmt)
                now = datetime.now()
                wakeup_datetime = now.replace(hour=parsed_time.hour, minute=parsed_time.minute,
                                              second=0, microsecond=0)
                if wakeup_datetime <= now:
                    wakeup_datetime += timedelta(days=1)
                return wakeup_datetime
            except ValueError:
                continue  # Try the next format
        print("Invalid format. Please try again.")

while True:
    # Refreshes current time after every loop restart
    current_time = datetime.now()
    print("\n\n\n====================================")
    print("CURRENT TIME:", current_time.strftime("%I:%M %p"))
    print("====================================")
    if extraSleepTime > 0:
        print("Extra Fall-Asleep Time: ", extraSleepTime, "minutes")
    
    print("MAIN MENU:")
    print("1: Calculate wake up time (if you go to sleep now)")
    print("2: Calculate sleep times (if you have a desired wake-up time)")
    print("3: Settings")
    print("0: Exit")
    
    try:
        Choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your choice.\n")
        continue

    if Choice == 1:
        print("\nCalculating wake up times...\n")
        # Calculate wake-up times based on the current time
        wakeupTime1 = current_time + timedelta(hours=9.25) + timedelta(minutes=extraSleepTime)  # 9 hours 15 minutes
        wakeupTime2 = current_time + timedelta(hours=7.75) + timedelta(minutes=extraSleepTime)  # 7 hours 45 minutes
        wakeupTime3 = current_time + timedelta(hours=6.25) + timedelta(minutes=extraSleepTime)  # 6 hours 15 minutes
        wakeupTime4 = current_time + timedelta(hours=4.75) + timedelta(minutes=extraSleepTime)  # 4 hours 45 minutes
        wakeupTime5 = current_time + timedelta(hours=3.25) + timedelta(minutes=extraSleepTime)  # 3 hours 15 minutes
        wakeupTime6 = current_time + timedelta(hours=1.75) + timedelta(minutes=extraSleepTime)  # 1 hour 45 minutes

        print("The average human takes 15 minutes to fall asleep. This time is automatically added on.")
        print("If you were to fall asleep now, the best times to wake up would be:\n")
        print("Best wake-up time:", wakeupTime1.strftime("%I:%M %p"))
        print("Good wake-up time:", wakeupTime2.strftime("%I:%M %p"))
        print("---------------\nSuitable wake-up times:")
        print("---", wakeupTime3.strftime("%I:%M %p"))
        print("---", wakeupTime4.strftime("%I:%M %p"))
        print("---", wakeupTime5.strftime("%I:%M %p"))
        print("---", wakeupTime6.strftime("%I:%M %p"))
        print("If you wake up at one of these times, you will rise in between 90-minute sleep cycles.")
        print("A good night's sleep consists of 5-6 complete sleep cycles.\n")

    elif Choice == 2:
        print("\nCalculating sleep times based on your desired wake-up time...\n")
        desiredAwakeTime = get_wakeup_time()
        
        # Calculate times to go to sleep by subtracting sleep cycle durations from desired wake-up time
        sleepTime1 = desiredAwakeTime - timedelta(hours=9.25) - timedelta(minutes=extraSleepTime) # 9 hours 15 minutes
        sleepTime2 = desiredAwakeTime - timedelta(hours=7.75) - timedelta(minutes=extraSleepTime)  # 7 hours 45 minutes
        sleepTime3 = desiredAwakeTime - timedelta(hours=6.25) - timedelta(minutes=extraSleepTime)  # 6 hours 15 minutes
        sleepTime4 = desiredAwakeTime - timedelta(hours=4.75) - timedelta(minutes=extraSleepTime)  # 4 hours 45 minutes
        sleepTime5 = desiredAwakeTime - timedelta(hours=3.25) - timedelta(minutes=extraSleepTime)  # 3 hours 15 minutes
        sleepTime6 = desiredAwakeTime - timedelta(hours=1.75) - timedelta(minutes=extraSleepTime)  # 1 hour 45 minutes

        print("You set your wake-up time to:", desiredAwakeTime.strftime("%I:%M %p on %B %d, %Y"))
        print("\nThe average human takes 15 minutes to fall asleep.")
        print("To wake up refreshed at", desiredAwakeTime.strftime("%I:%M %p") +
              ", you need to go to sleep at one of the following times:\n")
        print("Best sleep time:", sleepTime1.strftime("%I:%M %p"))
        print("Good sleep time:", sleepTime2.strftime("%I:%M %p"))
        print("---------------\nSuitable sleep times:")
        print("---", sleepTime3.strftime("%I:%M %p"))
        print("---", sleepTime4.strftime("%I:%M %p"))
        print("---", sleepTime5.strftime("%I:%M %p"))
        print("---", sleepTime6.strftime("%I:%M %p"))
        print()

    elif Choice == 3:
        print("\n\n\n-----------------------")
        print("SETTINGS & PREFERENCES")
        print("-----------------------")
        print("\nHere you can adjust the preferences and settings for this program.")
        print("Add Extra Time to Fall Asleep [1]\nMain Menu[0]")
        try:
            SettingChoice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.\n")
            continue
    
        if SettingChoice == 0:
            print("\nReturning to main menu..\n")
            continue #BACK TO MAIN MENU
            
        elif SettingChoice == 1:
            print("If it usually takes you longer to fall asleep, add extra time to the default 15-minute fall asleep time.")
            print("Enter a time (in minutes) to add onto your falling asleep time.")
            try:
                extraSleepTime = int(input("ENTER TIME IN MINUTES: "))
                print("TIME SAVED.\nAll times will now be adjusted to account for the extra", extraSleepTime," minutes.")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
            print("\nReturning to main menu..")
            
        else:
            print("Invalid choice in Settings. Returning to the main menu...\n")
            
                

    elif Choice == 0:
        print("\nExiting the program. Have a good day!")
        break

    else:
        print("Invalid choice! Please select a valid option.\n")


    input("Press Enter to return to the main menu...")
    print("\n")
