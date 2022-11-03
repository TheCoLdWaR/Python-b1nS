#!/usr/bin/python

# https://github.com/GTFOBins
# https://gtfobins.github.io/

# github.com/TheCoLdWaR

from termcolor import colored

if __name__== "__main__":

    def greeting():
        codesFile()


    def codesFile():

        #links
        print("\n")
        print("https://github.com/GTFOBins")
        print("https://gtfobins.github.io/")
        print("github.com/TheCoLdWaR\n")


        print(colored('W3Lc0m3 s1R H0w C4n 1 h3Lp Y0u ? ',"yellow"))
        input1 = input(colored("1-Show Binaries\n2-Exit\n","yellow"))

        if input1 == "1":
            import codes
            
        elif input1 == "2":
            exit()
            
 
    greeting()