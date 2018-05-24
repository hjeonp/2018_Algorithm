class Person:
    def __init__(self, name, company, address, zipcode, phone, email):
        self.name = name
        self.company = company
        self.address = address
        self.zipcode = zipcode
        self.phone = phone
        self.email = email

class Node:
    def __init__(self, personInfo, key):
        self.personInfo=personInfo
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

class BST:
    def __init__(self, T=None):
        self.root = T

    def readFile(self, file=None):
        infile = open(file, "r")
        for line in infile:
            person = line.split('|')
            personInfo = Person(person[0].split(), person[1].split(), person[2].split(), person[3].split(), person[4].split(), person[5].split())
            personNode = Node(personInfo, person[0])
            personBST.TREE_INSERT(personNode)
        infile.close()

    def saveFile(self, file=None):
        outfile=open(file,"w")
        self.inOrder2(self.root,file,outfile)


    def inOrder(self, x):
        if x.left == None: return
        else:
            self.inOrder(x.left)
        self.printer(x)

        if x.right == None: return
        else:
            self.inOrder(x.right)

    def inOrder2(self, x, name,outfile):
        if x.left == None:
            return
        else:
            self.inOrder2(x.left,name,outfile)
        string=x.key+'|'+printer_2(x.personInfo.company)+'|'+printer_2(x.personInfo.address)+'|'+\
                printer_2(x.personInfo.zipcode) +'|'+ printer_2(x.personInfo.phone)+'|'+printer_2(x.personInfo.email)+'\n'
        outfile.write(string)
        if x.right == None:
            return
        else:
            self.inOrder2(x.right,name,outfile)

          
    def TREE_INSERT(self, z):
        if self.root==None:
            self.root=z
            return
        #print(z.key)

        temp=self.root
        while True:
            if temp.key>z.key:
                if temp.left==None:
                    temp.left=z
                    z.parent=temp
                    break
                else:
                    temp=temp.left
            else:
                if temp.right==None:
                    temp.right=z
                    z.parent=temp
                    break
                else:
                    temp=temp.right

    def TREE_SEARCH(self, x, k):
        if x == None:
            return None

        if x.key.split()[0]==k:
            return x

        elif x.key > k:
            return self.TREE_SEARCH(x.left, k)

        else:
            return self.TREE_SEARCH(x.right, k)
    
    def printer(self, x):
        print(x.key)
        print("Company: " , printer_2(x.personInfo.company))
        print("Address: ", printer_2(x.personInfo.address))
        print("ZipCode: ", printer_2(x.personInfo.zipcode))
        print("Phone: ", printer_2(x.personInfo.phone))
        print("Email: ",  printer_2(x.personInfo.email))

    def TREE_TRACE(self, x, k):
        if x == None:
            return

        if x.key==k:
            print(k)
            return

        elif x.key > k:
            print(x.key)
            self.TREE_TRACE(x.left, k)

        else:
            print(x.key)
            self.TREE_TRACE(x.right, k)
        
    def TREE_MINIMUM(self, x):
        pass
    
    def TREE_MAXIMUM(self, x):
        pass

    def TREE_SUCCESSOR(self, x):
        if x.right!=None:
            while True:
                temp=x.parent
                if temp.left==temp:
                    break
            if temp.parent.left==temp:
                temp.parent.left=x
                x.left==temp.left
            else:
                temp.parent.right==x
                x.right=temp.right
        else:
            temp=x.right
            while temp.left!=None:
                temp=temp.right
            if temp.parent.left==temp:
                temp.parent.left=x
                x.left==temp.left
            else:
                temp.parent.right==x
                x.right=temp.right

    def TREE_PREDECESSOR(self, x):
        pass

    def TREE_DELETE(self, z):
        if z.left==None and z.right==None:
            if z.parent.left==z:
                z.parent.left=None
            else:
                z.parent.right=None
        elif z.left!=None and z.right!=None:
            self.TREE_SUCCESSOR(z)
        else:
            if z.left!=None:
                if z.parent.left==z:
                    z.parent.left=z.left
                    z.left.parent=z.parent
                else:
                    z.parent.right=z.left
                    z.right.parent=z.parent
            else:
                if z.parent.left==z:
                    z.parent.left=z.right
                    z.left.parent=z.parent
                else:
                    z.parent.right=z.right
                    z.right.parent=z.parent

def printer_2(arr):
     temp_str = ""
     for char in arr:
         temp_str += char
         temp_str += " "
     return temp_str

personBST = None
choice = -1
while(choice != 0):
    print("\n 0. 종료 \n 1. 파일읽기 \n 2. 사람찾기 \n 3. 경로찾기 \n 4. 삭제 \n 5. 정렬하여 출력하기 \n 6. 파일저장 \n")
    choice = int(input("select one: "))
    if (choice==0):
        break
    elif (choice == 1):
        if (input('Do you want to make BST from File? (y, n): ') == 'y'):
            fname = input("input your File name you want to make BST: ")
            personBST = BST()
            personBST.readFile(fname)
            print("File reading job is finished!")
            
    elif (choice == 2):
        while (input('Do you want to find some person from BST? (y, n): ') == 'y'):
            if (personBST == None):
                print("No Binary Search Tree !")
                break;
            else:
                key = input(">> 찾는 사람 이름: ")
                x  = personBST.TREE_SEARCH(personBST.root, key)
                if (x == None):
                    print("Not found it! Try again!")
                else:
                    print(printer_2(x.personInfo.name))
                    print(" 회사: ", printer_2(x.personInfo.company))
                    print(" 주소: ", printer_2(x.personInfo.address))
                    print(" 우편번호: ", printer_2(x.personInfo.zipcode))
                    print(" 전화번호: ", printer_2(x.personInfo.phone))
                    print(" 전자우편: ", printer_2(x.personInfo.email))
                    
    elif (choice == 3):                    
        while (input("Do you want to trace some people? (y, n):")=='y'):
            if (personBST == None):
                print("No Binary Search Tree !")
                break
            key = input(">> 추적하고자 하는 사람 이름: ")
            personBST.TREE_TRACE(personBST.root, key)

    elif (choice == 4):                
        while (input("Do you want to delete some person? (y, n):") == 'y'):
            if (personBST == None):
                print("No Binary Search Tree !")
                break
            key = input(">> 삭제하고자 하는 사람 이름: ")
            delX = personBST.TREE_SEARCH(personBST.root, key)
            if (delX == None):
                print("그런 사람 없어요!")
            else:
                personBST.TREE_DELETE(delX)
                print(key + "를(을) 삭제했어요.")
    elif (choice == 5):
        while (input("Do you want to see all of data from BST by Inorder? (y, n):") == 'y'):
            if (personBST == None):
                print("No Binary Search Tree !")
                break
            personBST.inOrder(personBST.root)
    elif (choice == 6): 
        while(input("Do you want to save your BST? (y, n): ") == 'y'):
            if (personBST == None):
                print("No Binary Search Tree !")
                break
            sName = input("input your file name to save BST: ")
            personBST.saveFile(sName)
