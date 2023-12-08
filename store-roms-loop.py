# just using some code from this video to test an idea
# https://www.youtube.com/watch?v=_DhqDYLS8oY&list=TLPQMDMwODIwMjOwjDOF6EU55g&index=16
# (around 6:20)
# note: i guess i'm re-re-learning this but the code in this video at that time stamp is actually for finding an ending header
# and adding in some data after that ending so it doesn't do what i thought it did

#

# Sky Diver (USA).a26

#end_hex = b"\n\x01\x03\x04\x05\x06\x00\xf0\xfe\x02"


if __name__ == '__main__':

    with open('Sky Diver (USA).a26', 'rb') as f:
        content = f.read()
        end_of_file = content[-10:]
        #str_hex = str(get_hex)
        #end_hex = bin(str_hex)
    
        #f.seek(offset + len(end_hex))
        #print(f"the type of end hex is {type(end_hex)}")
        #print(end_hex)   
 


#print(f"The length of conntent is {content_len}")


#store_game = (content)    

#print(f"Now a tuple, content length is {len(store_game)}")


#offset = store_game[-10:]



#print(f"the offset is {offset}")


