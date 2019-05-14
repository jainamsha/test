## greet
* greet
 - utter_greet
 - action_listen
 - utter_ask_assist

## name
* PERSON
 - utter_ask_assist
## job
* job
 - action_ask_job

## thanks
* thanks
 - utter_mypleasure

## about owners
* aboutOwners
 - utter_aboutOwners

## yellow Story
* Yellowstory
 - utter_yellowstory

## asktime
* asktime
 - action_time

## yellow culture
* aboutYellowCulture
 - utter_aboutYellowCulture

## company Location
* companyLocation
 - utter_companyLocation

## why yellow
* whyYellow
 - utter_whyYellow

## client
* client
 - action_client

## chitchat
* chitchat
 - utter_chitchat

## about Bot
* aboutBot
 - utter_aboutBot

## about company
* aboutCompany
 - utter_aboutCompany

## ask askProjects
* askProjects
 - action_show_projects

## assistance
* assistance
 - utter_ask_assist

## ask date
* askdate
 - action_date

## affirm
* affirm
 - utter_noworries

<!-- ## explain
* explain
 - action_explain -->

## goodbye
* goodbye
 - utter_goodbye

## joke
* joke
 - action_joke

## deny
* deny
 - utter_noworries

## stop
* stop
 - reset_slots
 - utter_ask_again

## story job as "UX Designer "
* job{"user": "job", "post": "UX Designer " }
    - slot{"post": "UX Designer " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "UX Lead "
* job{"user": "job", "post": "UX Lead " }
    - slot{"post": "UX Lead " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "UI Designer "
* job{"user": "job", "post": "UI Designer " }
    - slot{"post": "UI Designer " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "UI Lead "
* job{"user": "job", "post": "UI Lead " }
    - slot{"post": "UI Lead " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "Graphic Designer"
* job{"user": "job", "post": "Graphic Designer" }
    - slot{"post": "Graphic Designer" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Brand Lead "
* job{"user": "job", "post": " Brand Lead " }
    - slot{"post": " Brand Lead " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "Design Director"
* job{"user": "job", "post": "Design Director" }
    - slot{"post": "Design Director" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Illustrator "
* job{"user": "job", "post": " Illustrator " }
    - slot{"post": " Illustrator " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "3D Artist "
* job{"user": "job", "post": "3D Artist " }
    - slot{"post": "3D Artist " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "Product Manager"
* job{"user": "job", "post": "Product Manager" }
    - slot{"post": "Product Manager" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Content Writer"
* job{"user": "job", "post": " Content Writer" }
    - slot{"post": " Content Writer" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Business Development "
* job{"user": "job", "post": " Business Development " }
    - slot{"post": " Business Development " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "Manager "
* job{"user": "job", "post": "Manager " }
    - slot{"post": "Manager " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "HTML Developer"
* job{"user": "job", "post": "HTML Developer" }
    - slot{"post": "HTML Developer" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " PHP Developer "
* job{"user": "job", "post": " PHP Developer " }
    - slot{"post": " PHP Developer " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "Animator"
* job{"user": "job", "post": "Animator" }
    - slot{"post": "Animator" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Accounts"
* job{"user": "job", "post": " Accounts" }
    - slot{"post": " Accounts" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as "executive"
* job{"user": "job", "post": "executive" }
    - slot{"post": "executive" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Project Manager"
* job{"user": "job", "post": " Project Manager" }
    - slot{"post": " Project Manager" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Office boy"
* job{"user": "job", "post": " Office boy" }
    - slot{"post": " Office boy" }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story job as " Psychologist "
* job{"user": "job", "post": " Psychologist " }
    - slot{"post": " Psychologist " }
    - slot{"user": "job"}
    - action_ask_job
    - slot{"user": "job_applicant"}
    - followup{"name": "action_job"}
    - action_job
    - slot{"user": "job_applicant"}
    - followup{"name": "job_form"}
    - job_form
    - form{"name": "job_form"}
    - slot{"user": "job_applicant"}
    - form: followup{"name": "action_confirm"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "769698986923"}
    - slot{"phone-number": "769698986923"}
    - form: action_confirm
    - slot{"phone-number": "769698986923"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "igsfig@gmail.com"}
    - slot{"email": "igsfig@gmail.com"}
    - form: action_confirm
    - slot{"email": "igsfig@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
## story client for  "ux & ui designs"
* client{"assignment":  "ux & ui designs" }
    - slot{"assignment":  "ux & ui designs" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "ux design"
* client{"assignment":  "ux design" }
    - slot{"assignment":  "ux design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "ui design"
* client{"assignment":  "ui design" }
    - slot{"assignment":  "ui design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "visual design"
* client{"assignment":  "visual design" }
    - slot{"assignment":  "visual design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "icon design"
* client{"assignment":  "icon design" }
    - slot{"assignment":  "icon design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "illustration"
* client{"assignment":  "illustration" }
    - slot{"assignment":  "illustration" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "svg animation"
* client{"assignment":  "svg animation" }
    - slot{"assignment":  "svg animation" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "packaging design"
* client{"assignment":  "packaging design" }
    - slot{"assignment":  "packaging design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "web design"
* client{"assignment":  "web design" }
    - slot{"assignment":  "web design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "website design"
* client{"assignment":  "website design" }
    - slot{"assignment":  "website design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "app design"
* client{"assignment":  "app design" }
    - slot{"assignment":  "app design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "software design"
* client{"assignment":  "software design" }
    - slot{"assignment":  "software design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "ux audit"
* client{"assignment":  "ux audit" }
    - slot{"assignment":  "ux audit" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "ux research"
* client{"assignment":  "ux research" }
    - slot{"assignment":  "ux research" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "ux strategy"
* client{"assignment":  "ux strategy" }
    - slot{"assignment":  "ux strategy" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "interaction design"
* client{"assignment":  "interaction design" }
    - slot{"assignment":  "interaction design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "icon design"
* client{"assignment":  "icon design" }
    - slot{"assignment":  "icon design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "illustration"
* client{"assignment":  "illustration" }
    - slot{"assignment":  "illustration" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "branding"
* client{"assignment":  "branding" }
    - slot{"assignment":  "branding" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "logo design"
* client{"assignment":  "logo design" }
    - slot{"assignment":  "logo design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "identity design"
* client{"assignment":  "identity design" }
    - slot{"assignment":  "identity design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "svg animation"
* client{"assignment":  "svg animation" }
    - slot{"assignment":  "svg animation" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "brochure design"
* client{"assignment":  "brochure design" }
    - slot{"assignment":  "brochure design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "store design"
* client{"assignment":  "store design" }
    - slot{"assignment":  "store design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "web design"
* client{"assignment":  "web design" }
    - slot{"assignment":  "web design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "website design"
* client{"assignment":  "website design" }
    - slot{"assignment":  "website design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "brand budit"
* client{"assignment":  "brand budit" }
    - slot{"assignment":  "brand budit" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}

## story client for  "graphic design"
* client{"assignment":  "graphic design" }
    - slot{"assignment":  "graphic design" }
    - action_client
    - slot{"user": "client"}
    - followup{"name": "client_form"}
    - client_form
    - form{"name": "client_form"}
    - slot{"user": "client"}
    - form: followup{"name": "action_show_projects"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_projects
    - followup{"name": "action_confirm"}
    - action_confirm
    - form{"name": "action_confirm"}
    - slot{"requested_slot": "phone-number"}
* form: contact{"phone-number": "785876699789"}
    - slot{"phone-number": "785876699789"}
    - form: action_confirm
    - slot{"phone-number": "785876699789"}
    - slot{"requested_slot": "email"}
* form: contact{"email": "hjjjhg@gmail.com"}
    - slot{"email": "hjjjhg@gmail.com"}
    - form: action_confirm
    - slot{"email": "hjjjhg@gmail.com"}
    - form: followup{"name": "action_slot_reset"}
    - form{"name": null}
    - slot{"requested_slot": null}
