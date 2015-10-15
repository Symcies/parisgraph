#PARISGRAPH - GOAL

Project = Building a web application with the following goal : 

- Interface : A map of Paris with dots representing interesting** places of Paris {Museums, urbex, underground, parcs, bars, ...}

- User's Inputs : {Starting Point & Time to Spend}  OR  {Starting Point & Ending Point}

- Web App outputs : Path beginning at the starting point, giving a itinerary through the interesting** places

** Interestings places : Everyone has its own understanding of what a interesting place is! Because of that, each itinerary has to be built according to the users.
Therefor, each place has a weight depending on the user preferences.

At first, these preferences are choosen by the user. 

Machine Learning Part: The goal is to ask what the user likes within a set of pictures/description so that the algorithm sets the user's preferences iteslf


# Technologies
- Front End : AngularJS & Google Maps Javascript API (Direction)
- Back End : Django framework with Neo4J to work with graph database
