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
        if file == None:
            return

        try:
            outfile = open(file, "w")
        except IOError:
            print("Unable to Save" + file)

        else:
            self.saveLine()
            self.saveFile()
        
    def saveLine(self, x, outfile):
        pass

    def inOrder(self, x):
        if x.left == None: return
        else:
            self.inOrder(x.left)
        self.printer(x)

        if x.right == None: return
        else:
            self.inOrder(x.right)

          
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
        if x == None: return None

        if x.key==k:
            return x

        elif x.key > k:
            self.TREE_SEARCH(x.left, k)

        else:
            self.TREE_SEARCH(x.right, k)
    
    def printer(self, x):
        print(x.key)
        print("Company: " , x.personInfo.company)
        print("Address: ", x.personInfo.address)
        print("ZipCode: ", x.personInfo.zipcode)
        print("Phone: ", x.personInfo.phone)
        print("Email: ",  x.personInfo.email)

    def TREE_TRACE(self, x, k):
        if x == None: return

        if x.key==k:
            print(k)
            return

        elif x.key > k:
            print(x.key)
            self.TREE_SEARCH(x.left, k)

        else:
            print(x.key)
            self.TREE_SEARCH(x.right, k)
        
    def TREE_MINIMUM(self, x):
        pass
    
    def TREE_MAXIMUM(self, x):
        pass

    def TREE_SUCCESSOR(self, x):
        pass

    def TREE_PREDECESSOR(self, x):
        pass

    def TREE_DELETE(self, z):
        pass

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
                    print(x.personInfo.name)
                    print(" 회사: ", x.personInfo.company)
                    print(" 주소: ", x.personInfo.address)
                    print(" 우편번호: ", x.personInfo.zipcode)
                    print(" 전화번호: ", x.personInfo.phone)
                    print(" 전자우편: ", x.personInfo.email)
                    
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



