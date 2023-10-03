print("===== Nokia main menu =====")
print("""Press
    1 -> Phone book
    2 -> Message
    3 -> Chat
    4 -> Call register
    5 -> Tones
    6 -> Settings
    7 -> Call divert
    8 -> Games
    9 -> Calculator
    10 -> Reminders
    11 -> Clock
    12 -> Profiles
    13 -> SIM services
                            """)
print("Kindly select option: ")
nokia = int(input())
if nokia == 1:
    print("======= Phone book =======")
    print("""=====For phone book=====
    1 -> Search
    2 -> Services Nos
    3 -> Add name
    4 -> Erase
    5 -> Edit
    6 -> Assign tone
    7 -> Send b'card
    8 -> Options
    9 -> Speed dial
    10 -> Voice tags
                        """)
    print("Kindly select option: ")
    typeOfView = int(input())
    if typeOfView == 1:
        print("Search")
    elif typeOfView == 2:
        print("Service Nos")
    elif typeOfView == 3:
        print("Add name")
    elif typeOfView == 4:
        print("Erase")
    elif typeOfView == 5:
        print("Edit")
    elif typeOfView == 6:
        print("Assign tone")
    elif typeOfView == 7:
        print("Send b'card")
    elif typeOfView == 8:
        print("===== Options =====")
        print("""For Options
        1-> Type of view
        2 -> Memory status
                                """)
        print("Kindly select option: ")
        options = int(input())
        if options == 1:
            print("Type of view")
        elif options == 2:
            print("Memory status")
elif nokia == 2:
    print("===== Message =====")
    print("""For Message
        1 -> Write messages
        2 -> Inbox
        3 -> Outbox
        4 -> Picture message
        5 -> Template
        6 -> Smileys
        7 -> Message settings
                        """)
    print("Kindly select option: ")
    message = int(input())
    if message == 1:
        print("Write message")
    elif message == 2:
        print("Inbox")
    elif message == 3:
        print("Outbox")
    elif message == 4:
        print("Picture message")
    elif message == 5:
        print("Template")
    elif message == 6:
        print("Smileys")
    elif message == 7:
        print("===== Message settings =====")
        print("""For settings:
                1 -> Set 1
                2 -> Common
                                             """)
        print("Kindly select option: ")
    settings = int(input())
    if settings == 1:
        print("===== Set 1 =====")
        print("""For set 1
            1 -> Message centre number
            2 -> Message sent as
            3 -> Message validity
            4 ->  Common
                                        """)
        print("Kindly select option: ")
        setInput = int(input())
        if setInput == 1:
            print("Message centre number")
        elif setInput == 2:
            print("Message sent as")
        elif setInput == 3:
            print("Message validity")
        elif settings == 4:
                print("===== Common =====")
                print("""For common:
                1 -> Delivery reports
                2 -> Reply via same centre
                3 -> Character support
                                            """)
                print("Kindly select option: ")
                common = int(input())
                if common == 1:
                    print("Delivery Report")
                elif common == 2:
                    print("Reply via same centre")
                elif common == 3:
                    print("Character support")


elif nokia == 3:
    print("===== Chat =====")
    print("""
    1 -> select chat
                        """)
    print("Kindly select option: ")


elif nokia == 4:
    print("===== Call Register =====")
    print("""For call register
        1 -> Missed calls
        2 -> Received calls
        3 -> Dialled numbers
        4 -> Erase recent call history
        5 -> Show call duration
        6 -> Show call cost
        7 -> Call cost settings
        8 -> Prepaid credit
                                            """)
    print("Kindly select option: ")
    showCallDuration = int(input())
    if showCallDuration == 1:
        print("Missed calls")
    elif showCallDuration == 2:
        print("Received calls")
    elif showCallDuration == 3:
        print("Dialled numbers")
    elif showCallDuration == 4:
        print("Erase recent call list")
    elif showCallDuration == 5:
        print("""Show call duration
            1 -> Last call duration")
            2 -> All calls duration")
            3 -> Received call duration")
            4 -> Dialled calls duration")
            5 -> Clear timers")
                                          """)
        print("Kindly select option: ")
    lastCallDuration = int(input())
    if lastCallDuration == 1:
        print("Last call duration")
    elif lastCallDuration == 2:
        print("All calls duration")
    elif lastCallDuration == 3:
        print("Received calls duration")
    elif lastCallDuration == 4:
        print("Dialled calls duration")
    elif lastCallDuration == 5:
        print("Clear timers")
    elif showCallDuration == 6:
        print("===== Show call cost =====")
        print("""For show call cost
            1 -> Last call cost
            2 -> All calls cost
            3 -> Clear counters
                                    """)
        print("Kindly select option: ")
    costSettings = int(input())
    if costSettings == 1:
        print("Last call cost")
    elif costSettings == 2:
        print("All call cost")
    elif costSettings == 3:
        print("Clear counters")
    elif showCallDuration == 7:
        print("===== Call cost settings =====")
        print("""For call cost settings
            1 -> Call cost limit
            2 -> Show costs in
                                    """)
        print("Kindly select option: ")
    callSettings = int(input())
    if callSettings == 1:
        print("Call cost settings")
    elif callSettings == 2:
        print("Show costs in")
    elif showCallDuration == 8:
        print("Prepaid credit")


elif nokia == 5:
    print("===== Tones =====")
    print("""For Tones
        1 -> Ring Tone
        2 -> Ring Volume
        3 -> Incoming call alert
        4 -> Composer
        5 -> Message alert tone
        6 -> Vibrate alert
        7 -> Screen saver
                                     """)
    print("Kindly select option: ")
    ringingTone = int(input())
    if ringingTone == 1:
        print("Ring Tone")
    elif ringingTone == 2:
        print("Ring Volume")
    elif ringingTone == 3:
        print("Incoming call alert")
    elif ringingTone == 4:
        print("Composer")
    elif ringingTone == 5:
        print("Message alert tone")
    elif ringingTone == 6:
        print("Vibrate alert")
    elif ringingTone == 7:
        print("Screen saver")


elif nokia == 6:
    print("===== Setting =====")
    print("""For settings
            1 -> Call settings
            2 -> Phone settings
            3 -> Security settings
            4 -> Restore factory settings
                                        """)
    print("Kindly select option: ")
    settings = int(input())
    if settings == 1:
        print("===== Call settings =====")
        print("""For call settings
            1 -> Automatic redial
            2 -> Speed dialling
            3 -> Call waiting options
            4 -> Own number sending
            5 -> Phone line in use
            6 -> Automatic answer
                                    """)
        print("Kindly select option: ")
        autoRedial = int(input())
        if autoRedial == 1:
            print("Automatic redial")
        elif autoRedial == 2:
            print("Speed dialling")
        elif autoRedial == 3:
            print("Call waiting options")
        elif autoRedial == 4:
            print("Own number sending")
        elif autoRedial == 5:
            print("Phone line in use")
        elif autoRedial == 6:
            print("Automatic answer")
    elif settings == 2:
        print("===== Phone settings =====")
        print("""For phone settings
            1 -> Language
            2 -> Cell info display
            3 -> Welcome note
            4 -> Network selection
            5 -> Lights
            6 -> Confirm SIM service actions
                                            """)
    print("Kindly select option: ")
    language = int(input())
    if language == 1:
        print("Language")
    elif language == 2:
        print("Cell info display")
    elif language == 3:
        print("Welcome note")
    elif language == 4:
        print("Network selection")
    elif language == 5:
        print("Lights")
    elif language == 6:
        print("Confirm SIM service actions")
    elif settings == 6:
        print("===== Security settings =====")
    print("""For security settings
            1 -> PIN code request
            2 -> Call bearing service
            3 -> Fixed dialling
            4 -> Closed user group
            5 -> Phone security
            6 -> Change access codes
                                        """)
    print("Kindly select option: ")
    securitySettings = int(input())
    if securitySettings == 1:
        print("PIN code request")
    elif securitySettings == 2:
        print("Call bearing service")
    elif securitySettings == 3:
        print("Fixed dialling")
    elif securitySettings == 4:
        print("Closed user group")
    elif securitySettings == 5:
        print("Phone security")
    elif securitySettings == 6:
        print("Change access codes")
    elif settings == 7:
        print("Restore factory settings")


elif nokia == 7:
    print("======= Call divert =======")
    print(""" 1 -> Call divert
                                    """)
    print("Kindly select option: ")


elif nokia == 8:
    print("======= Games =======")
    print("Games")


elif nokia == 9:
    print("======= Calculator =======")
    print("Calculator")


elif nokia == 10:
    print("======= Reminder =======")
    print("Reminder")


elif nokia == 11:
    print("===== Clock =====")
    print("""For clock
        1 -> Alarm clock
        2 -> Clock settings
        3 -> Date settings
        4 -> Stopwatch
        5 -> Countdown timer
        6 -> Auto update of date and time
                                           """)
    print("Kindly select option: ")
    clock = int(input())
    if clock == 1:
        print("Alarm clock")
    elif clock == 2:
        print("Clock settings")
    elif clock == 3:
        print("Date settings")
    elif clock == 4:
        print("Stopwatch")
    elif clock == 5:
        print("Countdown timer")
    elif clock == 6:
        print("Auto update of date and time")


elif nokia == 12:
    print("======= Profile =======")
    print("Profiles")


elif nokia == 13:
    print("======= Sim Service =======")
    print("SIM Services")
