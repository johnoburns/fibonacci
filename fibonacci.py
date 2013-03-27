from math import sqrt
def fibonacci(x):
    if not(x.isdigit()):
        return "Please enter a positive integer."
    sequence = ""
    for n in range(int(x)) :sequence +=str(int((((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))) +" "
    return sequence

 
def fibonacci_xml_response(x):
    if not(x.isdigit()):
        return "Please enter a positive integer."
    xml_response = '<?xml version="1.0"?>'
    xml_response += "<fibonacci>"
    for n in range(int(x)):
        xml_response +='    <value index="%s">%s</value>'%((n+1),(str(int((((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))))))
    xml_response += '</fibonacci>'
    return xml_response
