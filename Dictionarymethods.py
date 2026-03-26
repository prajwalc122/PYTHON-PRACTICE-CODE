bio_data={
    
    "name":"prajwal",                   #keys is name and value is prajwal
    "age":18,
    "class":"BCA",
}

print(bio_data)
print(bio_data.items())            #.items is gives key value pairs and key value pairs is given in tuple form,


#dictionary means word -> meaning 
#dictionary means key -> value


meanings={
    "bat":"used to hit six",
    "ball":"used to bowled ",
    "wicket":"IS main part of cricket"
    
}



print(meanings,type(meanings))                  #to print the meanings key and values.
print(meanings.keys(),type(meanings))           #.keys used to display key value in dictionary.
print(meanings.values(),type(meanings))         #.values is used for displays the values in a dictionary.
print(meanings.items())                         #.values is used for displays the items in a dictionary.    
meanings.update({"bat":"BAT"})
print(meanings)
print(meanings.get("bat2"))                      #.get is used to print and main reason is incase of gives the key  value it give NONE
print(meanings["bat"])                           #IT GIVES THE error 