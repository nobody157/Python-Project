A1=int(input())
B1=int(input())
C1=int(input())
D1=int(input())
E1=int(input())
A2=int(input())
B2=int(input())
C2=int(input())
D2=int(input())
E2=int(input())
petrol_cost=C1+60*E1+60*D1*B1/A1
diesel_cost=C2+60*E2+60*D2*B2/A2
if(diesel_cost>petrol_cost):
    print("petrol")
else:
    print("diesel")
