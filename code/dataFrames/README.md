# Data description
## Columns of [fitness.csv](fitness.csv)
### Time
Timestamp at which the survey was answered, format yyyy-MM-dd- HH:mm:ss.SSSSSSZ, e.g., 2021-04-08 13:21:18.229000+08:00
### stairsElevator
Response to the question "In the past 60min, I used"
 - 9 = "Both"
 - 10 = "Stairs"
 - 11 = "Lift"
 - 12 = "Neither"
### workingNow
Response to question "Are you working right now?"
 - 10 = "Yes"
 - 11 = "No"
### BothLiftAndStairs_WhyLift	
Response to question "Took lift, why?" as a follow up question to the response "both" to the question "In the past 60min, I used"
 - 9 = "Convenience"
 - 10 = "No stairs"
 - 11 = "Less effort"
### BothLiftAndStairs_WhyStairs	
Response to question "Took stairs, why?" as a follow up question to the response "both" to the question "In the past 60min, I used"
 - 9 = "Convenience"
 - 10 = "No lift"
 - 11 = "Healthy"
 - 12 = "Save energy"
### whyLift	
Response to question "Took lift, why?" as a follow-up question to the response "lift" to the question "In the past 60min, I used"
 - 9 = "Convenience"
 - 10 = "No stairs"
 - 11 = "Less effort"
### whyStairs	
Response to question "Took stairs, why?" as a follow-up question to the response "stairs" to the question "In the past 60min, I used"
 - 9 = "Convenience"
 - 10 = "No lift"
 - 11 = "Healthy"
 - 12 = "Save energy"
### workStationType	
Response to question "What kind of workstation?"
  - 9 = "Adjustable"
 - 10 = "Sitting"
 - 11 = "Standing"
### adjustedWorkstationToday	
Response to question "Adjusted workstation height today?" as a follow-up question to the response "adjustable" to the question "What kind of workstation?"
 - 9 = "down & up"
 - 10 = "up"
 - 11 = "down"
 - 12 = "no adjustments"
### StairsConvenientBecause	
Response to question "Convenient because?" as a follow-up question to the response "convenient" to the question "Took stairs, why?" as a follow-up question to the response response "stairs" to the question "In the past 60min, I used"
 - 9 = "Both"
 - 10 = "Fastest"
 - 11 = "Easiest"
### BOTH_StairsConvenientBecause	
Response to question "Convenient because?" as a follow-up question to the response "convenient" to the question "Took stairs, why?" as a follow-up question to the response "both" to the question "In the past 60min, I used"
 - 9 = "Both"
 - 10 = "Fastest"
 - 11 = "Easiest"
### LiftConvenientBecause	
Response to question "Took lift, why?" as a follow-up question to the response "convenient" to the question "Took lift, why?" as a follow-up question to the response response "lift" to the question "In the past 60min, I used"
 - 9 = "Both"
 - 10 = "Fastest"
 - 11 = "Easiest"
### BOTH_LiftConvenientBecause	
Response to question "Took lift, why?" as a follow-up question to the response "convenient" to the question "Took lift, why?" as a follow-up question to the response response "both" to the question "In the past 60min, I used"
 - 9 = "Both"
 - 10 = "Fastest"
 - 11 = "Easiest"
### areYou	
Response to the question "Are you standing or sitting?"
 - 10 ="sitting"
 - 11 ="standing"
### heartRate	
Heart rate at the time of survey completion, e.g., 74
### lat	
Latitude provided by the GPS of the smartphone at the time of survey completion, e.g., 1.29654
### lon	
Longitude provided by the GPS of the smartphone at the time of survey completion, e.g., 103.77033
### Accuracy	
Accuracy of beacon-based localisation (Yak App) in meters at the time survey completion, e.g., 2.25
### Floor	
Floor level of the building in which the participant completed the survey at the time of survey completion, e.g., 3.0
### Latitude	
Latitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 1.2968251020999366
### Longitude	
Longitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 103.77049674151849
### Space_id	
Space id of the zone, e.g., 2.0
### Userid
ID of the study participant, e.g., onith27

## Columns of [infection_risk.csv](infection_risk.csv)
### time	
Timestamp at which the survey was answered, format yyyy-MM-dd- HH:mm:ss.SSSSSSZ, e.g., 2021-04-08 13:21:18.229000+08:00
### surroundingsIncreaseInfectionRisk	
Response to question "Do your surroundings increase infection risk?"
 - 9 = "A little"
 - 10 = "A lot"
 - 11 = "Not at all"
### WhatCausesMoreRisk
Response to question "What causes more risk?" as a follow-up question to the responses "A little" and "A lot" to the question "Do your surroundings increase infection risk?"
 - 9 = "Ventilation"
 - 10 = "Surface"
 - 11 = "People"
### SpecificallyWhatConcernsYou	
Response to the question "Specifically, what concerns you?" as a follow-up question to the response "People" to the question "What causes more risk?"
 - 9 = "Both"
 - 10 = "Proximity",
 - 11 = "Density",
### HowManyPeopleIn5M	
Response to the question "Currently, how many people within 5m?"
 - 9 = "5+ pax"
 - 10 = "1-4 pax"
 - 11 = "0 pax"
### heartRate	
Heart rate at the time of survey completion, e.g., 74
### lat	
Latitude provided by the GPS of the smartphone at the time of survey completion, e.g., 1.29654
### lon	
Longitude provided by the GPS of the smartphone at the time of survey completion, e.g., 103.77033
### Accuracy	
Accuracy of beacon-based localisation (Yak App) in meters at the time survey completion, e.g., 2.25
### Floor	
Floor level of the building in which the participant completed the survey at the time of survey completion, e.g., 3.0
### Latitude	
Latitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 1.2968251020999366
### Longitude	
Longitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 103.77049674151849
### Space_id	
Space id of the zone, e.g., 2.0
### Userid
ID of the study participant, e.g., onith27
### q1->4	
Responses of question 1 ("What causes more risk?") and question 4 ("Currently, how many people within 5m?") combined
### q2->4	
Responses of question 2 ("Specifically, what concerns you?") and question 4 ("Currently, how many people within 5m?") combined
### RiskCause
Response to the question "What causes more risk?" as a follow-up question to the responses "A little" and "A lot" to the question "Do your surroundings increase infection risk?"
 - People
 - Surface
 - Ventilation

## Columns of [privacy.csv](privacy.csv)
### Time
Timestamp at which the survey was answered, format yyyy-MM-dd- HH:mm:ss.SSSSSSZ, e.g., 2021-04-08 13:21:18.229000+08:00
### aloneOrInAGroup	
Response to the question "Alone or in a group?"
 - 9 = "Alone"
 - 10 = "Group"
 - 11 = "Online"
### Alone_categoryOfActivity	
Response to the question "Category of activity?" as a followp-up question to the response "Alone" to the question "Alone or in a group?"
 - 10 = "Leisure"
 - 11 = "Focus"
### Group_categoryOfActivity	
Response to the question "Category of activity?" as a followp-up question to the responses "Group" or "Online" to the question "Alone or in a group?"
 - 9 = "Socialize"
 - 10 = "Learn"
 - 11 = "Collaborate"
### Group_PossiblyDistractingOthers	
Response to the question "Possibly distracting others?" as a second follow-up question to the response to the response "Group" to the question "Alone or in a group?"
 - 10 = "Yes"
 - 11 = "No"
### Online_categoryOfActivity	
Response to the question "Possibly distracting others?" as a second follow-up question to the response to the response "Online" to the question "Alone or in a group?"
 - 9 = "Socialize"
 - 10 = "Learn"
 - 11 = "Collaborate"
### DistractionsNearby	
Response to the question "Distractions nearby?"
 - 9 = "None"
 - 10 = "A lot"
 - 11 = "A little"
### NeedMorePrivacy	
Response to the question "Feeling like you need more privacy?"
 - 10 = "Yes"
 - 11 = "No"
### ALittle_WhatKindOfDistraction	
Response to the question "What kind of distraction" as a follow-up question to the response "A little" to the question "Distractions nearby?"
 - 9 = "Visual"
 - 10 = "Others"
 - 11 = "Audio"
### ALot_WhatKindOfDistraction	
Response to the question "What kind of distraction" as a follow-up question to the response "A lot" to the question "Distractions nearby?"
 - 9 = "Visual"
 - 10 = "Others"
 - 11 = "Audio"
### WhatIsIt	
Response to the question "What is it?" as a follow-up question the response "Others" to the question "What kind of distraction?"
 - 9 = "Scent"
 - 10 = "Glare"
 - 11 = "Thermal"
### whyMorePrivacyNeeded	
Response to the question "Why more privacy needed?" as a follow-up question to the response "Yes" to the question "Feeling like you need more privacy?"
 - 9 = "Scent"
 - 10 = "Glare"
 - 11 = "Thermal"
### WhatPeopleSee	
Response to the question "What do people see?" as a follow-up question to the response "See me" to the question "Why more privacy needed?"
 - 9":"Appearance
 - 10":"Behavior
 - 11":"Work
### heartRate	
Heart rate at the time of survey completion, e.g., 74
### lat	
Latitude provided by the GPS of the smartphone at the time of survey completion, e.g., 1.29654
### lon	
Longitude provided by the GPS of the smartphone at the time of survey completion, e.g., 103.77033
### Accuracy	
Accuracy of beacon-based localisation (Yak App) in meters at the time survey completion, e.g., 2.25
### Floor	
Floor level of the building in which the participant completed the survey at the time of survey completion, e.g., 3.0
### Latitude	
Latitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 1.2968251020999366
### Longitude	
Longitude of the beacon-based localisation (Yak App) at the time of survey completion, e.g., 103.77049674151849
### Space_id	
Space id of the zone, e.g., 2.0
### Userid
ID of the study participant, e.g., onith27
