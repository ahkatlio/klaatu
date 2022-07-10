def main_a():
	print(me+" Hello"+" "+name+", how is going? Good or bad?")
	ans_1=input(I)
	if(ans_1=="good" or ans_1=="Good" or ans_1=="GOOD" or ans_1=="ok" or ans_1=="Ok" or ans_1=="OK" or ans_1=="Okey" or ans_1=="Okay" or ans_1=="okey" or ans_1=="okay" or ans_1=="OKAY" or ans_1=="OKEY"):
		print(me+"Thats awsome !!!! Do you like to join my club?")
		ans_2=input(I)
		if(ans_2=="yes" or ans_2=="good" or ans_2=="Good" or ans_2=="GOOD" or ans_2=="ok" or ans_2=="Ok" or ans_2=="OK" or ans_2=="Okey" or ans_2=="Okay" or ans_2=="okey" or ans_2=="okay" or ans_2=="OKAY" or ans_2=="OKEY" or ans_2=="why not" ):
			print(me+"Nice , here is the link: https://discord.gg/asYcjnustv")
			start=input(me+"press a to start again\n")
		else:
			print(me+"Okey , have a nice day! I hope I don't have to kill you. but lock your room tight!!")
			start=input(me+"press a to start again\n")
	elif(ans_1=="bad" or ans_1=="not good" or ans_1=="Not Good" or ans_1=="NOT GOOD" or ans_1=="not ok" or ans_1=="Not Ok" or ans_1=="NOT OK" or ans_1=="Not Okey" or ans_1=="Not Okay" or ans_1=="not okey" or ans_1=="not okay" or ans_1=="NOT OKAY" or ans_1=="NOT OKEY"):
		print(me+"Oh! Why?")
		ans_b=input(I)
		if(ans_b !=1):
			print(me+"You can join my club to remove your pain. Do you want to join it?")
			ans_c=input(I)
			if(ans_c=="yes" or ans_c=="yes" or ans_c=="good" or ans_c=="Good" or ans_c=="GOOD" or ans_c=="ok" or ans_c=="Ok" or ans_c=="OK" or ans_c=="Okey" or ans_c=="Okay" or ans_c=="okey" or ans_c=="okay" or ans_c=="OKAY" or ans_c=="OKEY" or ans_c=="why not"):
				print(me+"Nice, here is the link: https://discord.gg/asYcjnustv ")
				start=input(me+"press a to start again\n")
			elif(ans_c=="no" or ans_c=="nah" or ans_c=="hell no"):
				print(me+"well, you have chosen the death")
				start=input(me+"press a to start again\n")
			else:
				main_a()
	else:
		main_a()
	if(start=="a"):
		main_a()
	else:
		exit()
me="Klaatu:"	
print(me+"Hello, my friend! I'm Klaatu the chatbot. What is your name?")
name=input("you:")
I=name+":"
if(name!=1):
	main_a()	