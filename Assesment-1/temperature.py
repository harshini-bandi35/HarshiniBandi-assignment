'''- Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin based on user input.
   - Use functions for each conversion.
'''
def user_input():
    temperature=input("enter temperature in celcius: ")
    return (temperature)
def compute_farenheit(temperature):
    farenheit=((9/5)*(int(temperature)))+32
    return farenheit
def compute_kelvin(temperature):
    kelvin=int(temperature)+273.15
    return kelvin
def display(farenheit,kelvin):
    print(f"The temperature in farenheit is {farenheit}")
    print(f"The temperature in kelvin is {kelvin}")
def main():
    (temperature)=user_input()
    farenheit=compute_farenheit(temperature)
    kelvin=compute_kelvin(temperature)
    display(farenheit,kelvin) 
main()   
    