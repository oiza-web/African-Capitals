import random

africanCapitals = [
  ("Algeria", "Algiers"),
  ("Angola", "Luanda"),
  ("Benin", "Porto-Novo"),
  ("Botswana", "Gaborone"),
  ("Burkina Faso", "Ouagadougou"),
  ("Burundi", "Bujumbura"),
  ("The Republic of Cabo Verde", "Praia"),
  ("The Central African Republic", "Bangui"),
  ("Chad", "N'Djamena"),
  ("Comoros", "Moroni"),
  ("ocratic Republic of CongoDem", "Kinshasa"),
  ("Republic of Congo", "Brazzaville"),
  ("Cote d'Ivoire", "Yamoussoukro"),
  ("Djibouti", "Djibouti"),
  ("Egypt", "Cairo"),
  ("Equatorial Guinea", "Malabo"),
  ("Eritrea", "Asmara"),
  ("Ethiopia", "Addis Ababa"),
  ("Gabon", "Libreville"),
  ("Gambia", "Banjul"),
  ("Ghana", "Accra"),
  ("Guinea", "Conakry"),
  ("Guinea-Bissau", "Bissau"),
  ("Kenya", "Nairobi"),
  ("Lesotho", "Maseru"),
  ("Libya", "Tripoli"),
  ("Madagascar", "Antananarivo"),      
  ("Liberia", "Monrov~ia"),
  ("Malawi", "Lilongwe"),
  ("Mali", "Bamako"),
  ("Mauritania", "Nouakchott"),
  ("Mauritius", "Port Louis"),
  ("Morocco", "Rabat"),
  ("Mozambique", "Maputo"),
  ("Namibia", "Windhoek"),
  ("Niger", "Niamey"),
  ("Nigeria", "Abuja"),
  ("Rwanda", "Kigali"),
  ("Republic Arab Saharawi Democratic", "Aauin"),
  ("Sao Tome and Principe", "Sao Tome"),
  ("Senegal", "Dakar"),
  ("Seychelles", "Victoria"),
  ("Sierra Leone", "Freetown"),
  ("Somalia", "Mogadishu"),
  ("South Africa", "Pretoria"),
  ("South Sudan", "Juba"),
  ("Sudan", "Khartoum"),
  ("Swaziland", "Lobamba"),
  ("Tanzania", "Dar es Salaam"),
  ("Togo", "Lome"),
  ("Tunisia", "Tunis"),
  ("Uganda", "Kampala"),
  ("Zambia", "Lusaka"),
  ("Zimbabwe", "Harare")
]

user_score = 0


for i in range(0, 10):
  (Key,Value) = random.choice(africanCapitals)
  print("------------------------------------------------------------------" )  
  print("------------------------------------------------------------------" )  
  print("YOUR SCORE: " + str(user_score))
  print("------------------------------------------------------------------" )  
  print("------------------------------------------------------------------" )  

  user_entry = input("Enter the capital of " + Key + ":" )

  if user_entry != Value:
    user_score += 0
  else:
    user_score += 5
  

print("Your total is " + str(user_score))

