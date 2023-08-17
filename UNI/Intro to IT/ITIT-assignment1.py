# Author: Burton Vandetstok
# Date Created: 27/03/2023
# Date Last Changed: 28/03/2023
# This program has a menu which chosing out of the 3 options you can calculate bond yeild 
# or how many times a ball can bounce as well as how far it travelled

def Bond():
    # taking inputs from user
    faceValue = int(input("Face Value: "))
    couponInterestRate = float(input("Coupon Interest Rate (Decimal Eg: 0.03): "))
    currentMarketPrice = int(input("Current Market Price: "))
    yearsUntilMaturity = int(input("Years Until Maturity: "))
    
    # calculating YTM    
    intr = couponInterestRate * 1000
    a = (faceValue - currentMarketPrice)/yearsUntilMaturity
    b = (faceValue + currentMarketPrice)/2
    YTM = (intr + a)/b
    YTM *= 100

    # outputs
    print("The YTM is {}%".format(round(YTM,2)))

def Bounce():
    # taking inputs
    # Coefficient of restitution
    cor = float(input("Enter Coefficient of Restitution: "))
    initialHeight = float(input("Enter Initial Height in Meters: "))
    
    initialHeight *= 100
    
    #calculating
    BOUNCES = 0
    TOTAL_DISTANCE = 0
    while initialHeight >= 10:
        BOUNCES += 1
        TOTAL_DISTANCE += initialHeight
        print(initialHeight/100,TOTAL_DISTANCE/100)
        initialHeight = initialHeight * cor
        if  initialHeight >= 10:
            TOTAL_DISTANCE += initialHeight
    
    # outputs
    TOTAL_DISTANCE = round(TOTAL_DISTANCE /100,2)
    print("Number of Bounces: {}".format(BOUNCES))
    print("Meters Traveled: {}".format(TOTAL_DISTANCE))
    
def main():
    # menu
    print("A: Bond Yeild\nB: Bouncing Ball\nX:Exit")
    menu = input("Enter A,B,X: ")
    if menu == "A":
        Bond()
    if menu == "B":
        Bounce()

if __name__ == "__main__":
    main()