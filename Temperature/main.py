import shapes
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")


choice=int(input("Enter your choice: "))
if choice==1:
    r=float(input("Enter the radius of the circle: "))
    print("Area of circle is:", shapes.circle(r))
elif choice==2:
    l=float(input("Enter the length of the rectangle: "))
    b=float(input("Enter the breadth of the rectangle: "))
    print("Area of rectangle is:", shapes.rectangle(l,b))
elif choice==3:
    b=float(input("Enter the base of the triangle: "))
    h=float(input("Enter the height of the triangle: "))
    print("Area of triangle is:", shapes.triangle(b,h))
else:    print("Invalid choice")
