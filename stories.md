## tell time
* asktime
  - action_time
## tell about name
* whyYellow
  - utter_whyYellow
## tell about bot
* aboutBot
  - utter_aboutBot
## tell about company
* aboutCompany
  - utter_aboutCompany
## tell about owners
* aboutOwners
  - utter_aboutOwners
## show projects
* askProjects
  - action_show_projects
## tell yellow Story
* Yellowstory
  - utter_yellowstory
## tell location
* companyLocation
  - utter_companyLocation

## tell about culture
* aboutYellowCulture
  - utter_aboutYellowCulture

## tell date
* askdate
  - action_date

## happy intern path
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pubg"}
  - utter_ask_assist
* intern
  - intern_form
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "ux design"}
  - utter_ask_duration
  - slot{"duration": "4 months"}
* thanks
  - utter_mypleasure

## job from
* job
  - job_form
  - form{"name": "job_form"}
## client form
* client
  - action_client
  - client_form
  - form{"name": "client_form"}

## intern form
* intern
  - intern_form
  - form{"name": "intern_form"}
* intern
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "ux design"}
  - utter_ask_duration
  - slot{"duration": "1 month"}

## intern form
* intern
  - intern_form
  - form{"name": "intern_form"}
* intern
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "ux design"}
  - utter_ask_duration
  - slot{"duration": "4 months"}

## intern form
* intern
  - intern_form
  - form{"name": "intern_form"}
* intern
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "designing"}
  - utter_ask_duration
  - slot{"duration": "6 months"}

## unhappy intern path
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pubg"}
  - utter_ask_assist
* joke
  - action_joke
* chitchat
  - utter_chitchat
* chitchat
  - action_joke
* chitchat
  - utter_ask_assist
* intern
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "designing"}
  - utter_ask_duration
  - slot{"duration": "1 month"}
* thanks
  - utter_mypleasure

## job runaway
* greet
  - utter_greet
  - utter_ask_assist
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pablo"}
* job
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "brand design"}
* deny
  - utter_ask_again
* affirm
  - action_restart

## happy job path
* greet
  - utter_greet
  - utter_ask_assist
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pablo"}
* job
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "brand design"}
* thanks
  - utter_mypleasure

## happy job path
* greet
  - utter_greet
  - utter_ask_assist
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pablo"}
* job
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills": "brand design"}
* thanks
  - utter_mypleasure


## back off path
* greet
  - utter_greet
  - utter_ask_assist
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pablo"}
* chitchat
  - utter_chitchat
  - utter_ask_assist
* deny
  - utter_ask_again
* affirm
  - action_restart


## unhappy job path
* greet
  - utter_greet
  - utter_ask_assist
* chitchat
  - utter_ask_name
  - slot{"PERSON": "pablo"}
* chitchat
  - utter_chitchat
* deny
  - utter_ask_again
* deny
  - utter_ask_assist
* chitchat
  - utter_chitchat
* joke
  - action_joke
* job
  - job_form
  - form{"name": "job_form"}
  - utter_ask_skills
  - slot{"skills": "brand design"}
* thanks
  - utter_mypleasure


## happy client path
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "diablo"}
  - utter_ask_assist
* client
  - action_client
  - client_form
  - form{"name": "client_form"}
  - form{"name": null}
  - utter_ask_assignment
  - slot{"assignment": "website design"}
* deny
  - utter_mypleasure

## unhappy client path
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "ziablo"}
  - utter_ask_assist
* client
  - action_client
  - client_form
  - form{"name": "client_form"}
  - form{"name": null}
* chitchat
  - utter_chitchat
* deny
  - utter_ask_again
* deny
  - utter_ask_assist
* chitchat
  - utter_chitchat
* joke
  - action_joke
* client
  - action_client
  - form{"name": "client_form"}
  - form{"name": null}
  - utter_ask_assignment
  - slot{"assignment": "interaction design"}
* chitchat
  - utter_ask_phone-number
* contact{"phone-number": "9099981021"}
  - slot{"phone-number": "9099981021"}
* thanks
  - utter_mypleasure

## joke
* joke
  - action_joke

## askProjects
* askProjects
  - action_show_projects

## internform
* intern
  - intern_form
  - form{"name": "intern_form"}
  - form{"name": null}
  - utter_ask_skills
  - slot{"skills":"ux design"}
  - utter_ask_duration
  - slot{"duration":"1 month"}
  - action_deactivate_form

## runway
* greet
  - utter_greet
* stop
    - utter_goodbye
    - action_restart

## say goodbye
* thanks
  - utter_mypleasure

## fallback story
* default_fallback
  - utter_default


## Generated Story 7383952088192633656
* greet
    - utter_greet
    - utter_ask_name
* greet{"PERSON": "pablo"}
    - slot{"PERSON": "pablo"}
    - utter_ask_assist
* intern
    - utter_ask_skills
* intern{"skills": "brand design"}
* deny
    - utter_ask_again
* thanks
    - utter_mypleasure
    - action_restart
## Generated Story -8023036080112622600
* greet
    - utter_greet
* job
    - utter_ask_skills
* job{"skills": "brand design"}
    - slot{"skills": "brand design"}
    - slot{"user":"job_applicant"}
* goodbye
    - utter_mypleasure

## Generated Story -8023036080112622670
* greet
    - utter_greet
* job
    - utter_ask_skills
* job{"skills": "ux design"}
    - slot{"skills": "ux design"}
    - slot{"user":"job_applicant"}

* deny
    - utter_ask_assist
* intern
  - utter_ask_skills
* intern{"skills":"brand design"}
  - slot{"skills": "brand design"}
  - slot{"user":"intern"}
  * goodbye
    - utter_mypleasure

## Generated Story -971968789765781684
* greet{"PERSON": "cool"}
    - slot{"PERSON": "cool"}
    - utter_greet
* chitchat
    - utter_chitchat
    - utter_ask_assist
* joke
    - action_joke
* stop
    - utter_goodbye
    - action_restart

## Generated Story -7681157385034198227
* greet
    - utter_greet
* job
    - utter_ask_skills
* job{"skills": "brand design"}
* thanks
    - utter_mypleasure
    - action_restart
## Generated Story 2979059577582233108
* greet
    - utter_greet
* chitchat
    - utter_chitchat
    - utter_ask_assist
* joke
    - action_joke
* joke
    - action_joke
* goodbye{"time": "2019-03-04T02:34:13.000-08:00"}
    - utter_goodbye
    - action_restart
## generated story shit
* greet
    - utter_greet
* chitchat
    - utter_chitchat
    - utter_ask_assist
* joke
    - action_joke
* stop
    - utter_goodbye
    - action_restart
## Generated Story 5376797172310290323
* greet
    - utter_greet
* chitchat
* chitchat{"phone-number": 9099981021}
    - slot{"phone-number": 9099981021}
    - utter_ask_assist
* intern
    - intern_form
    - utter_ask_skills
* intern{"skills": "ux design"}
    - slot{"skills": "ux design"}
    - utter_ask_duration
* intern
    - action_deactivate_form
    - form{"name": null}
    - action_restart
## Generated Story 5396570414065032083
* greet
    - utter_greet
* intern
    - intern_form
    - utter_ask_skills
* intern{"skills": "ui design"}
    - slot{"skills": "ui design"}
    - utter_ask_duration
* intern{"duration": "4 months"}
    - slot{"duration": "4 months"}
    - utter_ask_name
* greet{"PERSON": "jae"}
    - slot{"PERSON": "jae"}
    - utter_ask_phone-number
* contact{"phone-number": "9099981021"}
    - slot{"phone-number": "9099981021"}
    - action_default_ask_affirmation

## job application
* greet
  - utter_greet
* deny
  - utter_chitchat
  - utter_ask_assist
* job
  - job_form
  - form{"name": "job_form"}
  - utter_ask_skills
* job{"skills": "ui design"}
  - slot{"skills": "ui design"}
  - utter_ask_name
* greet{"PERSON": "jae"}
  - slot{"PERSON": "jae"}
  - utter_ask_phone-number
* contact{"phone-number": "9099981021"}
  - slot{"phone-number": "9099981021"}
  - slot{"user": "job_applicant"}
* affirm
  - utter_mypleasure
* chitchat
  - action_joke
* stop
   - utter_goodbye
## Generated Story 7289277780753964599
* greet
    - utter_greet
* deny
    - utter_chitchat
    - utter_ask_assist
* client
  - action_client{"assignment": "logo design"}
    - slot{"assignment": "logo design"}
    - client_form
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: phone-number{"phone-number": "99483904704"}
    - slot{"phone-number": "99483904704"}
    - form: action_confirm
    - slot{"phone-number": "99483904704"}
    - slot{"requested_slot": "email"}
* form: phone-number{"email": "djsiand@gmail.com"}
    - slot{"email": "djsiand@gmail.com"}
    - form: action_confirm
## run stories
* client
  - action_client

## run stories
* job
  - action_job

## run Story
* intern
  - action_intern

## Generated Story -2286462709126408554
* intern
    - action_intern
    - slot{"user": "intern"}
    - intern_form
    - form{"name": "intern_form"}
    - slot{"requested_slot": "skills"}
* form: intern{"skills": "ui design"}
    - slot{"skills": "ui design"}
    - form: intern_form
    - slot{"skills": "ui design"}
    - slot{"requested_slot": "duration"}
* form: intern{"duration": "1 month"}
    - slot{"duration": "1 month"}
    - form: intern_form
    - slot{"duration": "1 month"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "76969686969"}
    - slot{"phone-number": "76969686969"}
    - form: action_confirm
    - slot{"phone-number": "76969686969"}
    - slot{"requested_slot": "email"}
* greet
    - utter_greet
    - action_listen
    - action_confirm
    - slot{"requested_slot": "email"}
* form: contact{"email": "shaion@gmail.com"}
    - slot{"email": "shaion@gmail.com"}
    - form: action_confirm
    - slot{"email": "shaion@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_mypleasure
* asktime
    - action_time
* thanks
    - utter_mypleasure

## Generated Story 2233510692313162768
* greet
    - utter_greet
* Yellowstory
    - utter_yellowstory
* aboutOwners
    - utter_aboutOwners
* job
    - job_form
    - form{"name": "job_form"}
    - slot{"requested_slot": "skills"}
* form: job{"skills": "Brand Design"}
    - slot{"skills": "designer"}
    - form: job_form
    - slot{"skills": "designer"}
    - slot{"user": "job_applicant"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "87879798789"}
    - slot{"phone-number": "87879798789"}
    - form: action_confirm
    - slot{"phone-number": "87879798789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "dirwfgiu@emial.com"}
    - slot{"email": "dirwfgiu@emial.com"}
    - form: action_confirm
    - slot{"email": "dirwfgiu@emial.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_mypleasure

## job example
* greet
    - utter_greet
* Yellowstory
    - utter_yellowstory
* aboutOwners
    - utter_aboutOwners
* job
    - job_form
    - form{"name": "job_form"}
    - slot{"requested_slot": "skills"}
* form: job{"skills": "Brand Design"}
    - slot{"skills": "designer"}
    - form: job_form
    - slot{"skills": "designing"}
    - slot{"user": "job_applicant"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "87879798789"}
    - slot{"phone-number": "87879798789"}
    - form: action_confirm
    - slot{"phone-number": "87879798789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "dirwfgiu@emial.com"}
    - slot{"email": "dirwfgiu@emial.com"}
    - form: action_confirm
    - slot{"email": "dirwfgiu@emial.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_mypleasure


## confirm story
* job
  - job_form
  - action_confirm

## confirm story
* intern
  - intern_form
  - action_confirm

## confirm story
* client
  - action_client
  - client_form
  - action_confirm

## confirm story
* job
  - job_form
  - action_confirm

## confirm story
* intern
  - intern_form
  - action_confirm

## confirm story
* client
  - action_client
  - client_form
  - action_confirm

## name Story
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "sunny"}
  - utter_ask_assist

## name Story1
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "kishor"}
  - utter_ask_assist

## name Story2
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "harshad"}
  - utter_ask_assist

## name Story
* greet
  - utter_greet
* chitchat
  - utter_ask_name
  - slot{"PERSON": "jae"}
  - utter_ask_assist
## Generated Story -8861730491782255360
* greet
    - utter_greet
    - utter_ask_name
* greet{"PERSON": "sunny"}
    - slot{"PERSON": "sunny"}
    - utter_ask_assist
* job
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"requested_slot": "skills"}
* form: job{"skills": "ui design"}
    - slot{"skills": "ui design"}
    - form: job_form
    - slot{"skills": "ui design"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "8787989757"}
    - slot{"phone-number": "8787989757"}
    - form: action_confirm
    - slot{"phone-number": ["8787989757", "8787989757"]}
    - slot{"requested_slot": "email"}
* form: contact{"email": "sjaijanso78@yahoo.com"}
    - slot{"email": "sjaijanso78@yahoo.com"}
    - form: action_confirm
    - slot{"email": "sjaijanso78@yahoo.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
* thanks
    - utter_noworries
