#!/usr/bin/python

import requests as req
from bs4 import BeautifulSoup
from termcolor import colored

def chosenFunc(func,binaryTitle,whichNumber,funcLen):

    print(colored("----------------------------------","green"))
    print(colored("[+] You have choosen --> " + binaryTitle + " Binary ----> " + func + " function","red"))
    print(colored("----------------------------------","green"))
    print(binaryTitle)
    print(whichNumber)
    
    #url of the binary's function
    urlfunc = "https://gtfobins.github.io/gtfobins/"+binaryTitle+"/#"+func

    request = req.get(urlfunc).text
    soup = BeautifulSoup(request,"lxml")

    body = soup.find("body")

    ul = body.find_all("ul",{"class":"examples"})

    print(ul[int(whichNumber)].text)


def chosenBinary(binaryTitle):

    #function names
    functions = []

    #print patterns
    print(colored("----------------------------------","green"))
    print(colored("You have chosen! ----> " + binaryTitle + " Binary","red"))
    print(colored("----------------------------------","green"))

    #Url of the binary name
    urlbinary = "https://gtfobins.github.io/gtfobins/"+binaryTitle

    
    #request binary url
    request = req.get(urlbinary).text
    soup = BeautifulSoup(request,"lxml")

    bodyText = soup.find("body")
    ul = bodyText.find("ul",{"class":"function-list"})
    li = ul.find_all("li")

    for i in range(0,len(li),1):
        functions.append(li[i].text)

    for i in range(0,len(li),1):
        print(str(i)+" : "+functions[i])


    #print(functions)
    inputfunc = input(colored("Choose one function! (Enter a number, example : 1)\n","red"))

    chosenFunc(functions[int(inputfunc)],binaryTitle,inputfunc,len(li))
    


def binaryTitles():

    #List Binary Titles

    url = "https://gtfobins.github.io/"

    request = req.get(url).text
    soup = BeautifulSoup(request, "lxml")

    body = soup.find("body")
    div = body.find_all("div")
    table = div[2].find("table")
    tbody = table.find("tbody")
    tbodyTrTags = tbody.find_all("tr")

    #binary names
    binaries=[]
    print(colored("-------------------------------------------------------- Binary Names --------------------------------------------------------\n","red"))
    for i in range(0,len(tbodyTrTags),1):
        print(tbodyTrTags[i].find("td").text, sep=" ", end="  |  ", flush=True)
        binaries.append(tbodyTrTags[i].find("td").text)
    

    inputBinary = input(colored("\nChoose One Binary! (Example : zip)\n","yellow"))

    if (inputBinary in binaries):
        chosenBinary(inputBinary)
    else:
        print(colored('wR0nq funct10N!\nDo you want to choose function again?\n1-Yes\n2-No','red'))

        chooseAgain = input("")
        if chooseAgain == "1":
            binaryTitles()
        elif chooseAgain == "2":
            exit()


binaryTitles()