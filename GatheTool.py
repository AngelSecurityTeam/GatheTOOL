#!usr/bin/python
import os,socket,requests,platform

def logo():
    
    print('''
\033[96m ██████╗  █████╗ ████████╗██╗  ██╗███████╗████████╗ ██████╗  ██████╗ ██╗     
\033[96m██╔════╝ ██╔══██╗╚══██╔══╝██║  ██║██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[96m██║  ███╗███████║   ██║   ███████║█████╗     ██║   ██║   ██║██║   ██║██║     
\033[39m██║   ██║██╔══██║   ██║   ██╔══██║██╔══╝     ██║   ██║   ██║██║   ██║██║     
\033[39m╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
\033[39m ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ''')
    print("""                                                           \033[39m|AngelSecurityTeam|\033[39m""")
    print()

def menu():
    print("""
\033[39m 1)\033[96m Whois Lookup             \033[39m8)\033[96m HTTP Header                  
\033[39m 2)\033[96m DNS Lookup               \033[39m9)\033[96m Host Finder
\033[39m 3)\033[96m GeoIP Lookup             \033[39m10)\033[96m IP-Locator   
\033[39m 4)\033[96m Subnet Lookup            \033[39m11)\033[96m Find Shared DNS Servers 
\033[39m 5)\033[96m Port Scanner             \033[39m12)\033[96m Get Robots.txt   
\033[39m 6)\033[96m Page Links               \033[39m13)\033[96m Host DNS Finder
\033[39m 7)\033[96m Zone Transfer            \033[39m14)\033[96m Exit                
          """)
    print()

def GATHETOOL():

      
    try:
        
        if 1 > 2 :
              print("buffer")
        else:
            opciones()

            
    except socket.gaierror:
        GATHETOOL()
    except UnboundLocalError:
        GATHETOOL()
    except requests.exceptions.ConnectionError:
        exit
    except IndexError:
        print('?')
        GATHETOOL()



def opciones():
        logo()
        website = input('\033[96mWebsite : \033[39m')
        
        
        menu()
        
        valorselec = input('Option: \033[39m')   

       
		   
        if valorselec == '1':
            whois = 'https://api.hackertarget.com/whois/?q='+website
            info = requests.get(whois)
            print('\033[99m')
            print(info.text)            
            opciones()


        elif valorselec == '2':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+website
            info = requests.get(dnslook)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+website
            info = requests.get(ipgeo)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+website
            info = requests.get(subnet)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '5':
            port = 'https://api.hackertarget.com/nmap/?q='+website
            info = requests.get(port)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+website
            info = requests.get(pagelink)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q='+website
            info = requests.get(zone)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '8':
            header = "https://api.hackertarget.com/httpheaders/?q="+website
            info = requests.get(header)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '9':
            host = "https://api.hackertarget.com/hostsearch/?q="+website
            info = requests.get(host)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '10':
            website = socket.gethostbyname(website)
            iplt = 'https://ipinfo.io/'+website+'/json'
            info = requests.get(iplt)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '11':
           
            shared = 'https://api.hackertarget.com/findshareddns/?q='+website
            info = requests.get(shared)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '12':
            robots ='http://'+website+'/robots.txt'
            info = requests.get(robots)
            print('\033[99m')
            print(info.text)
            opciones()

        elif valorselec == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+website
            info = requests.get(hostdns)
            print('\033[99m')
            print(info.text)
            opciones()



        elif valorselec == '14':
            exit

        else:
           
            GATHETOOL()
GATHETOOL()
