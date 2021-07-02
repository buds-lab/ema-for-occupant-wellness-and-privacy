infection_schema = [{
    "name": "surroundingsIncreaseInfectionRisk",
    "displayName": "Do surroundings increase risk?",
    "type": "icon",
    "questionText": "Do your surroundings",
    "questionSecondText": "increase infection risk?",
    "answerDirectTo": {
        "11": {
            "next": "HowManyPeopleIn5M",
        },
        "10": {
            "next": "WhatCausesMoreRisk",
        },
        "9": {
            "next": "WhatCausesMoreRisk"
        }
    },
    "iconText": ["Not at all", "A lot", "A little"],
    "iconColors": ["fb-black", "fb-black", "fb-black", ],
    "iconImages": [
        "images/icons/onith_covid/not_at_all.png", 
        "images/icons/onith_covid/a_lot.png", 
        "images/icons/onith_covid/a_little.png", 
    ],
}, {
    "name": "WhatCausesMoreRisk",
    "displayName": "What causes more risk?",
    "type": "icon",
    "questionText": "What causes ",
    "questionSecondText": "more risk?",
    "answerDirectTo": {
        "11": {
            "next": "SpecificallyWhatConcernsYou",
        },
        "10": {
            "next": "HowManyPeopleIn5M",
        },
        "9": {
            "next": "HowManyPeopleIn5M"
        }
    },
    "iconText": ["People", "Surface", "Ventilation"],
    "iconColors": ["fb-black", "fb-black", "fb-black", ],
    "iconImages": [
        "images/icons/onith_covid/people.png", 
        "images/icons/onith_covid/surface.png", 
        "images/icons/onith_covid/ventilation.png", 
    ],
}, {
    "name": "SpecificallyWhatConcernsYou",
    "displayName": "Specifically what concerns you?",
    "type": "icon",
    "questionText": "Specifically, what",
    "questionSecondText": "concerns you?",
    "answerDirectTo": {
        "11": {
            "next": "HowManyPeopleIn5M",
        },
        "10": {
            "next": "HowManyPeopleIn5M",
        },
        "9": {
            "next": "HowManyPeopleIn5M"
        }
    },
    "iconText": ["Density", "Proximity", "Both"],
    "iconColors": ["fb-black", "fb-black", "fb-black", ],
    "iconImages": [
        "images/icons/onith_covid/density.png", 
        "images/icons/onith_covid/proximity.png", 
        "images/icons/onith_covid/both.png", 
    ],
}, {
    "name": "HowManyPeopleIn5M",
    "displayName": "How many People?",
    "type": "icon",
    "questionText": "Currently, how many",
    "questionSecondText": "people within 5m?",
    "answerDirectTo": {
        "11": {
            "next": "end",
        },
        "10": {
            "next": "end",
        },
        "9": {
            "next": "end"
        }
    },
    "iconText": ["0 pax", "1-4 pax", "5+ pax"],
    "iconColors": ["fb-black", "fb-black", "fb-black", ],
    "iconImages": [
        "images/icons/onith_covid/0.png", 
        "images/icons/onith_covid/1-4.png", 
        "images/icons/onith_covid/5plus.png", 
    ],
}, ]