#!/usr/bin/python
  
import math
import itertools
import textwrap


def host_number():
    
        
  
        try:
            for host in range(1,255): # since the loop goes up to 254
                     host=int (input("\033[1;32mHow many Hosts do you need IPs for:\033[0m"))
                     host_bit = int(math.ceil((math.log(host+2)/math.log(2)))) #the ceil ensures the operatio is always rounded up eg  3.01 will be 4 while int turns the float to integer for further operations 
                     n = 8-host_bit #network bit portion
                     if host==0:
                           print '\033[1;31mYou Cannot Have 0 hosts!!!\033[0m '
                           continue
                     elif host>254:     
                           print '\033[1;31mYou Cant Have more than 254 Hosts in Class C !!!\033[0m '
                           continue

                     else:
                          print ("You require \033[1;32m ::%d bits for the host portion formula (2**n)-2 \033[0m," %host_bit)
                          print ("The network bits will be\033[1;32m ::%d, formula 2**n \033[0m," %n) 
                          break 
             
        except NameError: 
                          print("\033[2;31mUse real a number....\033[0m")
                          host_number()
        return (n,host) # returns a tuple of n and host



def ip_input(): 
    ip_addr= []
    max_ip_length = 4
    while len(ip_addr)< max_ip_length:
         octets =  int(input("\033[1;32m Enter Each of the four Octet of the ip address \033[0m"+"\033[2;32m::\033[0m"))
         ip_addr.append(octets)
    print 'You entered this IP address ::'+'\033[3;32m {0}.{1}.{2}.{3}\033[0m'.format(ip_addr[0],ip_addr[1],ip_addr[2],ip_addr[3])
    return ip_addr
         


# handles the subnetmask portion(CIDR NOTATION) for class c
def ip_subnet():
    subnet_mask = [] # no need for this
    mask = input("\033[1;32m Enter the subnet mask eg 255.255.255.0\033[0m"+"\033[2;32m::\033[0m")
    if mask != 2552552550 :
        print "Enter real Class c subnet"
    
    elif mask== 2552552550:
        subnet_mask.append(mask)    
   
    
    subnet_mask_used=[255,255,255,0]
    bin_subnet=[]
    for sub_mask in range (len(subnet_mask_used)):
        
         bin_subnet.append(format(subnet_mask_used[sub_mask],'b').zfill(8))

    print bin_subnet
ip_subnet()     
    
    

def binary_convert():
    five_octets=ip_input() # passing the list from the ip_input function
    ip_addr=five_octets[0:4] # slicing the list to four octets
     
    binary_converted = []
    for octet in range (len(ip_addr)): # accessing individual octets
        binary_converted.append(format(ip_addr[octet],'b').zfill(8))
    print (binary_converted)
    return binary_converted

 

""" This module here is concerned with handling the network bits till they are eight bits in length, ie from where the other functon has determine the numbers of network bits and host bits"""

n,host=host_number() #unpacking the values of the tuple  and making n and host_number global variables 

def subnet_handler():
    
    my_list=map(list,itertools.product([0,1],repeat =n))
    print (my_list)
    single_list= [item for sublist in my_list for item in sublist]
    single_list_string=[''.join(str(item) for item in single_list)]
        
    print ('AM SINGLE LIST STRIN',single_list_string)
   
    return n,single_list_string #returns a tuple of the local variable n and single_list_string in form of (n, [x, y, x,x,y]) 


n,single_list_string =subnet_handler() # unpcking the two returned values to n and single_list_string


myList = single_list_string

new_list_chunk= [i for text in myList for i in textwrap.wrap(text, n)]
print new_list_chunk



def make_each_eight():
    print "\033[3;32m Alist containing all the posible combination \033[0m:",new_list_chunk
    same_list =new_list_chunk # since the content is the same we do this to create a local variable for this function

    return [value.ljust(8,'0') for value in  same_list] 
each_eight_bit=make_each_eight() # aglobal variable
print  "\033[3;32m Here we now make the items 8 bits long:\033[0m ", each_eight_bit

""" The module ends here for handling the network bits ends here"""  

# The displaying function


def network_addr():
   
   ip_addr_bin= binary_convert()
   
   all_combination= each_eight_bit
  
   for item in all_combination:
       N=host # we assigning the number of hosts to variable m as this will help us get broadcast and other addresses
       ip_addr_bin[3] =item
       network_addr=[ int(octet_string_bin,2) for octet_string_bin in ip_addr_bin] #list copresion technique helps to cahnge each binary to decimal value
       
       print "\033[1;32m Network Address:{0}.{1}.{2}.{3}\033[0m".format(network_addr[0],network_addr[1],network_addr[2],network_addr[3])
       print 'First Usable IP address for this subnet:{0}.{1}.{2}.{3}'.format(network_addr[0],network_addr[1],network_addr[2],network_addr[-1] +1)
       print 'Last Usable IP address for this subnet:{0}.{1}.{2}.{3}'.format(network_addr[0],network_addr[1],network_addr[2],network_addr[-1] +N)
       print '\033[2;32m Broadcast  address for this subnet:{0}.{1}.{2}.{3}\033[0m'.format(network_addr[0],network_addr[1],network_addr[2],network_addr[-1] +(N+1))


network_addr()



 




    



