def main_a():
	print(me+" Hello"+" "+name+", how is going? Good or bad?")
	ans_1=input(I)
	if(ans_1=="good"):
		print(me+"Thats awsome !!!! Do you like to join my club?")
		ans_2=input(I)
		if(ans_2=="yes"):
			print(me+"Nice , here is the link: https://discord.gg/asYcjnustv")
			start=input(me+"press a to start again\n")
		else:
			print(me+"Okey , have a nice day! I hope I don't have to kill you. but lock your room tight!!")
			start=input(me+"press a to start again\n")
	elif(ans_1=="bad"):
		print(me+"Oh! Why?")
		ans_b=input(I)
		if(ans_b !=1):
			print(me+"You can join my club to remove your pain. Do you want to join it?")
			ans_c=input(I)
			if(ans_c=="yes"):
				print(me+"Nice, here is the link: https://discord.gg/asYcjnustv ")
				start=input(me+"press a to start again\n")
			elif(ans_c=="no"):
				print(me+"well you chose the death")
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
print(me+"Hello, my friend ! What is your name ?")
name=input("you:")
I=name+":"
if(name!=1):
	main_a()	