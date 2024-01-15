import random

nome = input()


#player 1
dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
#player 2 
dice_3 = random.randint(1,6)
dice_4 = random.randint(1,6)


#Player 1 
if dice_1 == 1:
		  printf(f"⭐️{nome}")
		  print("""
 _________
 |	     |
 |   0   |
 |	     |
 ---------\n""")
elif dice_1 == 2:
	   print(f"⭐️{nome}")
	   print("""
_________
|0	    |
|	      |
|	     0|
---------\n""")
elif dice_1 == 3:
	   print(f"⭐️{nome}")
	   print("""
_________
|0	    |
|   0   |
|	     0|
---------\n""")
elif dice_1 == 4:
		print(f"⭐️{nome}")
		print("""
_________
|0	   0|
|	      |
|0	   0|
---------\n""")
elif dice_1 == 5:
		print(f"⭐️{nome}")
		print("""
_________
|0	   0|
|   0   |
|0	   0|
---------\n""")
elif dice_1 ==6:
	   print(f"⭐️{nome}")
	   print("""
_________
|0	   0|
|0	   0|
|0	   0|
---------\n""")
if dice_2 == 1:
		 print("""
			 _________
			 |	     |
			 |   0   |
			 |	     |
			 ---------\n""")
elif dice_2 == 2:
	   print("""
			 _________
			 |0	     |
			 |	     |
			 |	    0|
			 ---------\n""")
elif dice_2 == 3:
	   print("""
			 _________
			 |0	     |
			 |   0   |
			 |	    0|
			 ---------\n""")
elif dice_2 == 4:
		print("""
			 _________
			 |0	    0|
			 |	     |
			 |0  	  0|
			 ---------\n""")
elif dice_2 == 5:
		print("""
			 _________
			 |0   	0|
			 |   0   |
			 |0	    0|
			 ---------\n""")
elif dice_2 ==6:
	   print("""
			 _________
			 |0	    0|
			 |0	    0|
			 |0	    0|
			 ---------\n""")
#Player 2
if dice_3 == 1:
		  print("💻Computer")
		  print("""
 _________
 |	     |
 |   0   |
 |	     |
 ---------\n""")
elif dice_3 == 2:
	   print("💻Computer")
	   print("""
_________
|0	    |
|	      |
|	  0   |
---------\n""")
elif dice_3 == 3:
	   print("💻Computer")
	   print("""
_________
|0	    |
|   0   |
|	  0   |
---------\n""")
elif dice_3 == 4:
		 print("💻computer")
		 print("""
_________
|0	   0|
|	      |
|0	   0|
---------\n""")
elif dice_3 == 5:
		print("💻Computer")
		print("""
_________
|0	   0|
|   0   |
|0	   0|
---------\n""")
elif dice_3 ==6:
		print("💻Computer")
		print("""
_________
|0	   0|
|0	   0|
|0	   0|
---------\n""")
if dice_4 == 1:
		 print("""
			 _________
			 |	     |
			 |   0   |
			 |	     |
			 ---------\n""")
elif dice_4 == 2:
	   print("""
			 _________
			 |0	     |
			 |	     |
			 |	    0|
			 ---------\n""")
elif dice_4 == 3:
	   print("""
			 _________
			 |0	     |
			 |   0   |
			 |	    0|
			 ---------\n""")
elif dice_4 == 4:
		print("""
			 _________
			 |0	    0|
			 |	     |
			 |0	    0|
			 ---------\n""")
elif dice_4 == 5:
		print("""
			 _________
			 |0	    0|
			 |   0   |
			 |0	    0|
			 ---------\n""")
elif dice_4 ==6:
	   print("""
			 _________
			 |0 	  0|
			 |0	    0|
			 |0	    0|
			 ---------\n""")

if dice_1 + dice_2 > dice_3 + dice_4:
		   print(f"			   ⭐️{nome}⭐️: {dice_1 + dice_2} WIN!")
		   print(f"			💻Computer💻: {dice_3 + dice_4} LOSE!")
elif dice_1 + dice_2 == dice_3 + dice_4:
		   print("			 No One Wins: DRAW!")
else:
		   print(f"			💻Computer💻: {dice_3 + dice_4} WIN!")
		   print(f"			⭐️{nome}⭐️: {dice_1 + dice_2} LOSE!")
