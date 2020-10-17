while 1:
    s=str(input("Which Solid Do You Select Sir(Cube, Cuboid, Cylinder, Sphere or Hemisphere)"))
    if s=="cube":
        c=int(input('Enter side of cube'))
        print ("Total Surface Area Of Cube Is",6*c*c)
        print ("Curved Surface Area Of Cube Is",4*c*c)
        print ("Volume Of Cube Is",c*c*c)
    elif s=="cuboid":
        cl=int(input('Enter length of cuboid'))
        cb=int(input('Enter breadth of cuboid'))
        ch=int(input('Enter height of cuboid'))
        print ("Total Surface Area Of Cuboid Is",2*cl*cb+2*cl*ch+2*cb*ch)
        print ("Curved Surface Area Of Cuboid Is",2*ch*(cl+cb))
        print ("Volume Of Cuboid Is",cl*cb*ch)
    elif s=="cylinder":
        cr=int(input('Enter radius of cylinder'))
        ch1=int(input('Enter height of cylinder'))
        print ("Total Surface Area Of Cylinder Is",2*3.14*cr*(cr+ch1))
        print ("Curved Surface Area Of Cylinder Is",2*3.14*cr*ch1)
        print ("Volume Of Cylinder Is",3.14*cr*ch1)
    elif s=="sphere":
        sr=int(input('Enter radius of Sphere'))
        print ("Total Surface Area Of Sphere Is",4*3.14*sr*sr)
        print ("Volume Of Sphere Is",4/3*3.14*sr*sr*sr)
    elif s=="hemisphere":
        hr=int(input('Enter radius of Hemisphere'))
        print ("Total Surface Area Of Hemisphere Is",3*3.14*hr*hr)
        print ("Curved Surface Area Of Hemisphere Is",2*3.14*hr*hr)
        print ("Volume Of Hemisphere Is",2/3*3.14*hr*hr*hr)
    elif s=="triangle":
        s1=int(input('Enter 1st side'))
        s2=int(input('Enter 2nd side'))
        s3=int(input('Enter 3rd side'))
        sp=(s1+s2+s3)/2
        print ("Area Of Triangle is",(sp*(sp-s1)*(sp-s2)*(sp-s3))**(1/2))
    else:
        print("That is not in my programme")
    o=input("do you want it again")
    if o=='no':
        break
    

     
