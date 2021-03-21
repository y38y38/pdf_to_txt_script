import unicodedata

def del_notjapanese(message):
	#str new_message
	new_message = ''
	for i in message:
		letter = unicodedata.east_asian_width(i)
		#print(letter)
		if letter == 'F':     
			new_message = new_message + i
		elif letter == 'A':     # 全角
			new_message = new_message + i
		elif letter == 'W':     # 全角
			new_message = new_message + i
	
	return new_message

def del_lastequal(message, char):
	#str new_message
	new_message = ''
	message_len = len(message)

	counter = 0
#	print(counter)
	for i in message:
		if (counter+1 == message_len):
			if (message[counter] != char):
				new_message = new_message + i
		else:
			new_message = new_message + i
		
		counter = counter + 1
	
	return new_message

def is_number(char):
	if (char != '1'):
		if ((char) != '2'):
			if ((char) != '3'):
				if ((char) != '4'):
					if ((char) != '5'):
						if ((char) != '6'):
							if ((char) != '7'):
								if ((char) != '8'):
									if ((char) != '9'):
										return False

	return True


#先頭の数字を削除する
def del_topnumberandspace(message):
	#str new_message
	new_message = ''
	message_len = len(message)

	counter = 0
	search_end = 0
	is_space = 0
	for i in message:
		if (search_end == 0):
			if (is_number(message[counter])==False):
				new_message = new_message + i
			else:
				search_end = 1
				is_space = 1
		
		else:
			if (is_space == 0):
				new_message = new_message + i
			else:
				is_space = 0


		counter = counter + 1

	return new_message

#@以降を削除する
def del_afteratmark(message):
	#str new_message
	new_message = ''
	message_len = len(message)

	counter = 0
	search_end = 0
	is_space = 0
	for i in message:
		if (search_end == 0):
			if (i != '@'):
				new_message = new_message + i
			else:
				search_end = 1

	return new_message


out_file = open('out.csv', 'w')
#for i in range(15, 202, 1): 
for i in range(15, 202, 2): 
    jp_filename = 'freze-%03d' % (i) + '.txt'
    eg_filename = 'freze-%03d' % (i+1) + '.txt'

    #print(filename )
    jp_file = open(jp_filename)
    jp_list = jp_file.readlines()
    #jp_list = jp_list.replace("\n","")

    eg_file = open(eg_filename)
    eg_list = eg_file.readlines()
    #eg_list = eg_list.replace("\n","")

    jp_len = len(jp_list)
    eg_len = len(eg_list)
    #print(jp_len)
    #print(eg_len)
    
    if (jp_len > eg_len):
        file_len = jp_len
    else:
        file_len = eg_len

    #print(eg_list[0])
    #exit()
    jp_counter = 0
    eg_counter = 0
    for j in range (0, file_len, 1):

        #print(jp_len)
        #print(jp_counter)
        #print(eg_len)
        #print(eg_counter)
        if (jp_len <= jp_counter):
            if (eg_len <= eg_counter):
                break

        while(1):
            if (jp_len > jp_counter):
                jp_line = jp_list[jp_counter].replace("\n","")
                jp_counter=jp_counter + 1
                jp_line = jp_line.replace(",","")
                jp_line = jp_line.replace("ロ","")
                jp_line = del_notjapanese(jp_line)
                jp_line = del_lastequal(jp_line, "一")
                jp_line = del_lastequal(jp_line, "ー")
                if(len(jp_line) > 1):
                    out_file.write(jp_line)
                    #print(jp_line)
                    break
            else:
                break

        out_file.write(",")

        while(1):
            if (eg_len > eg_counter):
                eg_line = eg_list[eg_counter].replace("\n","")
                eg_counter=eg_counter +1
                eg_line = eg_line.replace(",","")
                eg_line = del_topnumberandspace(eg_line)
                eg_line = del_afteratmark(eg_line)
                if(len(eg_line) > 1):
                    out_file.write(eg_line)
                    #print(eg_line)
                    break
            else:
                break

        out_file.write("\n")
        #print('next')
        #print('\n')

    #print(file_len)
    out_file.write("\n\n\n")
    #for jp_line in jp_list:
        #print (jp_line)


