def count_substring(string, sub_string):
    count=0;
    if not(string is None) and not(sub_string is None):
        for lens in range(0,len(string)-len(sub_string)+1):
            #print(type(lens))
            #print(type(newlen))
            if string[lens:lens+len(sub_string)] == sub_string:
                count= count+1
    return count        

if __name__ == '__main__':
    print(count_substring("CDCCDC","CDC"))
	
#my final test
    
