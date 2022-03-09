import random
import sys
import os
import time


big_ben = """        ╖@╣╣╢▓╬@,╓╖╥╖∩╥╦╣╣╣╢▒▒╫╣╢╣▒▒▒▒╖
        ▒╣▓▓╫╣╢╣▒╙▒▒▒╣▒║╣▒╣╣▒▒▒▒▒▒╢▓▓▓╣▒▒╓
     ,╓║▓▓▓▓▓▓╣▒▒╢╫╣║╬╢╣╣▓▒▒▒▒▒▒▒▒░▒▓▓▓▓▓▒╗─
     ▒▒╢▓▓▓▓▓▌░▒▒╫╣╢╫▒╢╢▒╢╢▓▓▓▓▓▓▓▒░▒▓▓▓▓╫╣▒[
     ╢╫▓▓▓▓▓▓▒░▒╫╬▓▓▓▓▓▓▓▓▓▓███▌█▓▓▒▒▒▓█▓▓▓▓╬╣╖
     ]╫╫▓▓▓▓▓▒▒╫▓▓▌▓████▓▓▓▓██▓▓▓▓▓╣╣╢▒▓█▓▓▓▓╢╣║╖
    ,╫╣▓▓▓▓█▓▒╢╣▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢╢╣║╢▒▒▒▓█▓▓▓▓╬▓▒▒
   ,╫╢▓▓▓▓▓█╣╢╢▒╢╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╢╢▒▒▒▒▓██▓▓▓▓╫▒
   ╟▓▓▓▓▓▒▒╜▒║╢╣▓╢▓▓██████████████▓▓╣▒▒▒@▒▒▓▓▓▓▓╢▒
   ╫▓▓▓░░,▒╣║▒╢╫╫▓█████████████████▓▓▓╣▒▒▒▒░╙▀▓▓▓╣
  ]╢▓▓▓∩░▒▒▒▒▒▓╣▓▓█████████████████▓▓▓▒╖,░░   ▒╜╙
  ║╫▓▓▓░░▒▒░▒▒▒▒▓▓▓████████████████▓▓▓╣▒░▒╓░░░▒
 '╨▓▓▓▓░▒▒▒▒▒▒▒▒╢╢▓▓╢███████████▓▓▓▓╣▒▒▒▒▒░░░▒▒
      '╣╫╣▒▒▒▒▒░▒▒╫╫╫╫▓▓▓███▓▓╣▓▓▓▒╣▒╢Ñ▒▒▒▒▒▒▒
       ╙╢╣▓▓▒▒▒╣▒╣╫▒▒╢▒╣▓▓▓▓╢╢▒▓▒╢▒▒▒▒╢▒╣▒Ñ░
░          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣╣╣╢╬▒╢▒▒▒▒▒╫▓▓
░░░░         ╙▓╢╣╣╫╫╣╣╢╢╣╢╢╢▓╣╬╣╬▓▓╣╣╢▓`
░░░░░░░        ▒▓▓▓▓▓▓▒▒╢▒▒╢▒▒╢▒▒▓▓▓▓▓╣▓U,
░░░░░░░      ,▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓╢╣╢╣╣╢╬@╖
 ░░░░░   ╔╦@▓▓▓▓▓▓▓▓▓▓╠▓╫▓▒╢▒╫╣║▒▒▒▒▒▒╣╢╢╣╣╬▒╬╖\n\n"""


def typeing(text, tim=0.1, space=True):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(tim)
	if space == True:
		print("\n")


def ben_first():
	print(big_ben)
	print("""Exit with ":exit" \n""")
	typeing("Ben: BÆn\n\n-------------------")
	ben_last()

def ben_phone():
	typeing("Ringing", 0.1, False)
	typeing("Ringing...")
	typeing("Ben: BÆn\n\n-------------------")
	ben_last()


def ben_last():
	number = random.randint(0, 8)
	user_input = input("Type you're answer: ")
	if user_input == ":exit":
		sys.exit(0)

	if number == 0 or number == 1:
		typeing(f"\nYou: {user_input}\n", 0.05, False)
		time.sleep(0.5)
		typeing("Ben: Yes")
		ben_last()
	elif number == 2 or number == 3:
		typeing(f"\nYou: {user_input}\n", 0.05, False)
		time.sleep(0.5)
		typeing("Ben: No")
		ben_last()
	elif number == 4 or number == 5:
		typeing(f"\nYou: {user_input}\n", 0.05, False)
		time.sleep(0.5)
		typeing("Ben: Huhuhu")
		ben_last()
	elif number == 6 or number == 7:
		typeing(f"\nYou: {user_input}\n", 0.05, False)
		time.sleep(0.5)
		typeing("Ben: Ohwg")
		ben_last()
	elif number == 8:
		typeing(f"\nYou: {user_input}\n", 0.05, False)
		time.sleep(0.5)
		typeing("""Ben: "Hangs up" """)
		ben_phone()
	
		
