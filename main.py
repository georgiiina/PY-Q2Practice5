from pyscript import document, display
def check_country(e):
   document.getElementById("output1").innerHTML = ""
   country = {
       "ph" : "Philippines",
       "ic" : "Iceland",
       "ge" : "Germany",
       "sw" : "Switzerland",
       "us" : "United States of America"
   }
   country_code = document.getElementById("countries").value
   show_country= country_code in country
   list_country= list(country.keys())

#add a country
   country["ca"] = "Canada"
   display("The number of countries are", len(country), target = "output1")
   display("Is it in the dictionary?", show_country, target = "output1")
   display("What are the countries in the dictionary?", list_country, target = "output1")
