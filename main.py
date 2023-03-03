#just import using pip method through terminal, but talk to Professor about environment variables
import ttg

#prop_vars = ["p" #It's raining inside
 #            ,"q" #I am inside
  #           ]

#prop_expressions = ["p and q",
 #                   "p or q",
  #                  "~p",
   #                 "p => q",
    #                  "p = q"
     #                 ]
#p => q means if p, then q

#print(ttg.Truths(prop_vars,prop_expressions))



#This is the wampus world example

prop_vars = ["rain", #It is raining outside
             "ins", #I am inside
             "out", #I am outside
             "car", #I am in my car
             "walk", #I am on a walk
             "swea", #I am wearing a sweater

             ]

prop_expressions = ["rain => ins", #If it is rainy,I am inside (if "rain", then "ins")
                    "ins => ~out" ,#If "ins", then -"out" and vice versa. 
                    "out => car or walk",#If "out", then "car" or "walk"
                    "car => ~walk", #If "car",then -"walk" and vice versa.
                    "walk => swea", #IF "walk", then "swea"

                    
                    ]


print(ttg.Truths(prop_vars,prop_expressions))

perceptrons = [
    "~rain", #It is NOT raining outside
    "walk",#I am on a walk
]

prop_expressions = prop_expressions + perceptrons

print(ttg.Truths(prop_vars,prop_expressions))