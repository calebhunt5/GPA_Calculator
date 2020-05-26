def Main():
    sem =int(input("How many smesters have you completed?"))

    list =[]

    #loop for overall semesters
    count =1
    while(count <= sem):
        print("Semester "+str(count))
        count2 =0

        #loop for individual classes
        while(count2 <6):
            grade =input("enter a letter grade")
        
            list.append(grade)
            count2 =count2+1
        count =count+1

    temp =0
    #foreach loop that determines and calculates gpa
    for x in list:
        if(x == "a"):
            numTemp =4.0

        elif(x == "a-"):
            numTemp =3.7

        elif(x == "b+"):
            numTemp =3.3

        elif(x == "b"):
            numTemp =3.0

        elif(x == "b-"):
            numTemp =2.7

        elif(x == "c+"):
            numTemp =2.3

        elif(x == "c"):
            numTemp =2.0

        elif(x == "c-"):
            numTemp =1.7
        
        elif(x == "d+"):
            numTemp =1.3
        
        elif(x == "d"):
            numTemp =1.0
        
        elif(x == "d-"):
            numTemp =0.7
        
        elif(x == "e"):
            numTemp =0.0
        
        else:
            print("NO")

            
        temp =temp+numTemp

    temp =temp/len(list)
    #output of gpa
    print(temp)

Main()
