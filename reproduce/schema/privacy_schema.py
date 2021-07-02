privacy = [
    {
        "name": "aloneOrInAGroup",
        "displayName": "Alone or in a group",
        "type": "icon",
        "questionText": "Alone or in a group?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "Online_categoryOfActivity",
            },
            "10": {
                "next": "Group_categoryOfActivity",
            },
            "9": {
                "next": "Alone_categoryOfActivity"
            }
        },
        "iconText": [
            "Online",
            "Group",
            "Alone"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/online.png",
            "images/icons/privacy/group.png",
            "images/icons/privacy/alone.png",
        ],
    },
    {
        "name": "Alone_categoryOfActivity",
        "displayName": "Alone category of activity",
        "type": "icon",
        "questionText": "Category of Activity?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "DistractionsNearby",
            },
            "10": {
                "next": "DistractionsNearby",
            }
        },
        "iconText": [
            "Focus",
            "Leisure"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/focus.png",
            "images/icons/privacy/leisure.png",
        ],
    },
    {
        "name": "Group_categoryOfActivity",
        "displayName": "Group category of activity",
        "type": "icon",
        "questionText": "Category of Activity?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "Group_PossiblyDistractingOthers",
            },
            "10": {
                "next": "Group_PossiblyDistractingOthers",
            },
            "9": {
                "next": "Group_PossiblyDistractingOthers"
            }
        },
        "iconText": [
            "Collaborate",
            "Learn",
            "Socialize"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/collaborate.png",
            "images/icons/privacy/learn.png",
            "images/icons/privacy/socialize.png",
        ],
    },
    {
        "name": "Group_PossiblyDistractingOthers",
        "displayName": "Group possibly distracting others",
        "type": "icon",
        "questionText": "Possible distracting?",
        "questionSecondText": "others?",
        "answerDirectTo": {
            "11": {
                "next": "DistractionsNearby",
            },
            "10": {
                "next": "DistractionsNearby",
            }
        },
        "iconText": [
            "No",
            "Yes"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/no.png",
            "images/icons/privacy/yes.png",
        ],
    },
    {
        "name": "Online_categoryOfActivity",
        "displayName": "Online category of activity",
        "type": "icon",
        "questionText": "Category of Activity?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "DistractionsNearby",
            },
            "10": {
                "next": "DistractionsNearby",
            },
            "9": {
                "next": "DistractionsNearby"
            }
        },
        "iconText": [
            "Collaborate",
            "Learn",
            "Socialize"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/collaborate.png",
            "images/icons/privacy/learn.png",
            "images/icons/privacy/socialize.png",
        ],
    },
    {
        "name": "DistractionsNearby",
        "displayName": "Distractions nearby",
        "type": "icon",
        "questionText": "Distractions nearby?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "ALittle_WhatKindOfDistraction",
            },
            "10": {
                "next": "ALot_WhatKindOfDistraction",
            },
            "9": {
                "next": "NeedMorePrivacy"
            }
        },
        "iconText": [
            "A little",
            "A lot",
            "None"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/a_little.png",
            "images/icons/privacy/a_lot.png",
            "images/icons/privacy/none.png",
        ],
    },
    {
        "name": "NeedMorePrivacy",
        "displayName": "Need more privacy",
        "type": "icon",
        "questionText": "Feeling like you need",
        "questionSecondText": "more privacy?",
        "answerDirectTo": {
            "11": {
                "next": "end",
            },
            "10": {
                "next": "whyMorePrivacyNeeded",
            }
        },
        "iconText": [
            "No",
            "Yes"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/no.png",
            "images/icons/privacy/yes.png",
        ],
    },
    {
        "name": "ALittle_WhatKindOfDistraction",
        "displayName": "A little, What kind of distracton?",
        "type": "icon",
        "questionText": "What kind of distraction?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "NeedMorePrivacy",
            },
            "10": {
                "next": "WhatIsIt",
            },
            "9": {
                "next": "NeedMorePrivacy"
            }
        },
        "iconText": [
            "Audio",
            "Others",
            "Visual"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/audio.png",
            "images/icons/privacy/others.png",
            "images/icons/privacy/visual.png",
        ],
    },
    {
        "name": "ALot_WhatKindOfDistraction",
        "displayName": "A little, What kind of distracton?",
        "type": "icon",
        "questionText": "What kind of distraction?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "NeedMorePrivacy",
            },
            "10": {
                "next": "WhatIsIt",
            },
            "9": {
                "next": "NeedMorePrivacy"
            }
        },
        "iconText": [
            "Audio",
            "Others",
            "Visual"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/audio.png",
            "images/icons/privacy/others.png",
            "images/icons/privacy/visual.png",
        ],
    },
    {
        "name": "WhatIsIt",
        "displayName": "What is it?",
        "type": "icon",
        "questionText": "What is it?",
        "questionSecondText": "",
        "answerDirectTo": {
            "11": {
                "next": "NeedMorePrivacy",
            },
            "10": {
                "next": "NeedMorePrivacy",
            },
            "9": {
                "next": "NeedMorePrivacy"
            }
        },
        "iconText": [
            "Thermal",
            "Glare",
            "Scent"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/thermal.png",
            "images/icons/privacy/glare.png",
            "images/icons/privacy/scent.png",
        ],
    },
    {
        "name": "whyMorePrivacyNeeded",
        "displayName": "Why more privacy needed?",
        "type": "icon",
        "questionText": "Why more privacy",
        "questionSecondText": "needed?",
        "answerDirectTo": {
            "11": {
                "next": "WhatPeopleSee",
            },
            "10": {
                "next": "end",
            },
            "9": {
                "next": "end"
            }
        },
        "iconText": [
            "See me",
            "Both",
            "Hear me"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/seeme.png",
            "images/icons/privacy/both.png",
            "images/icons/privacy/hearme.png",
        ],
    },
    {
        "name": "WhatPeopleSee",
        "displayName": "What do people see?",
        "type": "icon",
        "questionText": "What do people see?",
        "questionSecondText": "",
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
        "iconText": [
            "Work",
            "Behavior",
            "Appearance"
        ],
        "iconColors": [
            "fb-peach",
            "fb-peach",
            "fb-peach"
        ],
        "iconImages": [
            "images/icons/privacy/work.png",
            "images/icons/privacy/behaviour.png",
            "images/icons/privacy/appearance.png",
        ],
    },
]