from javapythonassignment.calculator import Calculators


def phone_menu():
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
        print(phone_book())
    elif nokia == 2:
        print(message())
    elif nokia == 3:
        print(chat())
    elif nokia == 4:
        print(call_register())
    elif nokia == 5:
        print(tone())
    elif nokia == 6:
        print(settings())
    elif nokia == 7:
        print(call_divert())
    elif nokia == 8:
        print(games())
    elif nokia == 9:
        Calculators()
    elif nokia == 10:
        print(Reminders())
    elif nokia == 11:
        print(Clock())
    elif nokia == 12:
        print(Profile())
    elif nokia == 13:
        print(Sim_service())

    def phone_menu():
        print(phone_menu())


def phone_book():
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
    view = str(input())
    if view == 1:
        print("===== Search =====")
        print("""Search
            1-> 
            
                                """)
    elif view == 2:
        print("Service Nos")
    elif view == 3:
        print("Add name")
    elif view == 4:
        print("Erase")
    elif view == 5:
        print("Edit")
    elif view == 6:
        print("Assign tone")
    elif view == 7:
        print("Send b'card")
    elif view == 8:
        print("===== Options =====")
        print("""For Options
        1-> Type of view
        2 -> Memory status
                                """)
        print("Kindly select option: ")
        options = str(input())
        if options == 1:
            print("Type of view")
        elif options == 2:
            print("Memory status")
        elif options == 4:
            print(phone_menu())


def message():
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
        message_settings = int(input())
        if message_settings == 1:
            print("===== Set 1 =====")
            print(""" For set 1
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
            elif setInput == 4:
                print("Common")
            message_settings = int(input())
        elif message_settings == 2:
            print("===== Common =====")
            print(""" For common:
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
            elif common == 4:
                print(phone_menu())


def chat():
    print("===== Chat =====")
    print("""
        1-> Text
        2-> Chat settings
        3-> Chat
        4-> Phone menu
                    """)
    print("Kindly select options:")
    chat = int(input())
    if chat == 1:
        print("Text")
    elif chat == 2:
        print("Chat settings")
        phone_menu()


def call_register():
    print("===== Call register =====")
    print("""
     1-> Missed calls
     2-> Received calls
     3-> Dialled numbers
     4-> Erase recent call list
     5-> Show call duration
     6-> Show call cost
     7-> Call cost settings
     8-> Prepaid credit
     9-> Back to call register
     10-> Back to phonebook
     11-> Back to main menu
                               """)
    print("Kindly select options:")
    call_register = int(input())
    if call_register == 1:
        print("Missed calls")
    elif call_register == 2:
        print("Received calls")
    elif call_register == 3:
        print("Dialled numbers")
    elif call_register == 4:
        print("Erase recent call list")
    elif call_register == 5:
        print("""Show call duration
            1 -> Last call duration
            2 -> All calls duration
            3 -> Received call duration
            4 -> Dialled calls duration
            5 -> Clear timers
                                          """)
        print("Kindly select option: ")
        Show_call_durationas = int(input())
        if Show_call_durationas == 1:
            print("Last call duration")
        elif Show_call_durationas == 2:
            print("All calls duration")
        elif Show_call_durationas == 3:
            print("Received calls duration")
        elif Show_call_durationas == 4:
            print("Dialled calls duration")
        elif Show_call_durationas == 5:
            print("Clear timers")
        elif Show_call_durationas == 6:
            print(phone_menu())
    elif call_register == 6:
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
        elif costSettings == 4:
            print(())
    elif call_register == 7:
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
    elif call_register == 8:
        print("Prepaid credit")


def tone():
    print("===== Tones =====""")
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
    elif ringingTone == 8:
        print(tone())
    elif ringingTone == 9:
        print(phone_menu())


def settings():
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
        elif language == 7:
            phone_menu()
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
            phone_menu()
    elif settings == 7:
        print("Restore factory settings")
    elif settings == 8:
        phone_menu()


def call_divert():
    print("======= Call divert =======")
    print("""      Call divert
            1-> Pin code request
            2-> phone menu 
                                    """)
    print("Kindly select option: ")
    call_divert= int(input())
    if call_divert == 1:
        print("PIN code request")
    elif settings == 2:
        phone_menu()

def games():
    print("======= Games =======")
    print(""" Games 
            1-> start games
            2-> phone menu
                            """)
    print("Kindly select option: ")
    games = int(input())
    if games == 1:
        print("Games")
    elif games == 2:
        phone_menu()



def Calculator():
    print("======= Calculator =======")
    print("""
    1-> calculate
    2-> phone menu
                                    """)
    calculator = input("Kindly select option: ")
    if calculator == 1:
        Calculators()

    elif Reminders == 2:
        phone_menu()


def Reminders():
    print("======= Reminder =======")
    if Reminders == 1:
        print("set-up")
    elif Reminders == 2:
        phone_menu()
    print("Kindly select option: ")


def Clock():
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
    elif clock == 7:
        phone_menu()


def Profile():
    print("======= Profile =======")
    if Profile == 1:
        print("profile")
    elif Profile == 2:
        phone_menu()
    print("Kindly select option: ")


def Sim_service():
    print("======= Sim Service =======")
    if Sim_service == 1:
        print("sim service")
    elif Reminders == 2:
        phone_menu()
    print("Kindly select option: ")


phone_menu()
