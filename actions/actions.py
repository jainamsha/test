from __future__ import absolute_import, division, print_function, unicode_literals
import json
import time
import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUttered,Restarted,AllSlotsReset,FollowupAction
from rasa_core_sdk.forms import FormAction

class ActionExplain(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_explain"

    def run(self, dispatcher, tracker, domain):
        leftSlot = tracker.get_slot(required_slots)
        if leftSlot != None:
            this = "sir i would like you to provide me {}".format(leftSlot)
            dispatcher.utter_message(this)
        else :
            this = "ill explain once im sure about it."
            dispatcher.utter_message(this)

class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value'] # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class AskForJob(Action):
    def name(self):
        return "action_ask_job"

    @staticmethod
    def required_slots(tracker):
        return ["user"]

    def slot_mappings(self):
        return {"user": self.from_entity(entity="user")}

    def run(self, dispatcher, tracker, domain):
        user = tracker.get_slot("user")
        intern = ["intern", "internship", "interns"]
        jobguy = ["jobs","placements " ,"job", "job applicant", "job applicants", "professional"]
        if user in intern:
            return [SlotSet('user',"intern"),FollowupAction("action_intern")]
        if user in jobguy:
            return [SlotSet('user',"job_applicant"),FollowupAction("action_job")]
        if user == "client":
            return [SlotSet('user',"client"),FollowupAction("action_client")]
        else:
            dispatcher.utter_message("can you confirm, if it is for a job or internship you looking for ?")

class ActionConfirm(FormAction):
    def name(self):
        return "action_confirm"
    @staticmethod
    def required_slots(tracker):
        return ["phone-number", "email"]

    def slot_mappings(self):
        return {"phone-number": self.from_entity(entity="phone-number"),
                "email": self.from_entity(entity="email")}

    def submit(self, dispatcher, tracker, domain):
       user = tracker.get_slot('user')
       email = tracker.get_slot('email')
       zz = """Okay, so your {} mail has been recieved! we'll reach you back at {} ASAP 😉""".format(user,email)
       dispatcher.utter_message(zz)
       return[FollowupAction("action_slot_reset")]

class ActionTellTime(Action):
    def name(self):
        return "action_time"

    def slot_mappings(self):
        return {"time": self.from_intent(intent=asktime)}

    def run(self, dispatcher, tracker, domain):
        timeslot = tracker.get_slot("time")
        if timeslot == None:
            times = str(time.asctime())
            timee = times.split()
            timed = timee[3].split(":")
            timedisplay = "it's {} hours and {} minutes in my land!".format(timed[0],timed[1])
            dispatcher.utter_message(timedisplay)

        else:
            timeslot = str(timeslot)
            times = timeslot.split("T")
            timed = times[1].split(":")
            timedisplay = "Your requested time is {} hours and {} minutes ".format(timed[0],timed[1])
            dispatcher.utter_message(timedisplay)

class ActionTellDate(Action):
    def name(self):
        return "action_date"

    def slot_mappings(self):
        return {"time": self.from_intent(intent=askdate)}

    def run(self, dispatcher, tracker, domain):
        dateslot = tracker.get_slot("time")
        if dateslot == None:
            times = str(time.asctime())
            date = times.split(" ")
            datedisplay = "its  is {} {} {} of {} ".format(date[0],date[1],date[2],date[4])
            dispatcher.utter_message(datedisplay)
        else:
            dateslot = str(dateslot)
            fulldate = dateslot.split("T")
            date = fulldate[0].split("-")
            datedisplay = "it will be {} of {} of year {}".format(date[2],date[1],date[0])
            dispatcher.utter_message(datedisplay)

class InternForm(FormAction):
   def name(self):
       return "intern_form"
   @staticmethod
   def required_slots(tracker) :
        return ["skills","duration"]

   def slot_mappings(self):
        intern = "intern"
        return {"skills": self.from_entity(entity="skills"),
        "duration": self.from_entity(entity="duration", not_intent="deny")}

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]

       PERSON = tracker.get_slot('PERSON')
       skills = tracker.get_slot('skills')
       duration = tracker.get_slot('duration')
       # utter submit template
       zz = """okay so {} your {} internship request for {} is recieved, well reach back to you ASAP""".format(PERSON,duration,skills)
       dispatcher.utter_message(zz)
       return[FollowupAction("action_confirm")]

class ActionIntern(Action):
    def name(self):
        return "action_intern"
    def run(self,dispatcher,tracker,domain):
       return [SlotSet('user',"intern"),FollowupAction("intern_form")]

class JobForm(FormAction):
   def name(self):
       return "job_form"
   @staticmethod
   def required_slots(tracker) :
       if tracker.get_slot("assignment") != None:
           return ["post"]
       if tracker.get_slot("post") != None:
           return ["post"]
       else:
           return ["skills","post"]


   def slot_mappings(self):
        return {"skills": self.from_entity(entity="skills",not_intent="client"),
        "assignment": self.from_entity(entity="assignment"),
        "post": self.from_entity(entity="post")}

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]

       PERSON = tracker.get_slot('PERSON')
       assignment = tracker.get_slot("assignment")
       skills = tracker.get_slot('skills')
       post = tracker.get_slot('post')

       if assignment != None :
           zz = """okay so {} your job application for {} has been recieved, and we'll get back to you ASAP!""".format(PERSON,assignment)
       if post != None :
           zz = """okay so {} your job application for {} post has been recieved, and we'll get back to you ASAP!""".format(PERSON,post)
       if skills != None :
           zz = """okay so {} your job application for {} skill has been recieved, and we'll get back to you ASAP!""".format(PERSON,skills)
       dispatcher.utter_message(zz)
       return [SlotSet('user',"job_applicant"),FollowupAction("action_confirm")]

class Actionjob(Action):
    def name(self):
        return "action_job"
    def run(self,dispatcher,tracker,domain):
       return [SlotSet('user',"job_applicant"),FollowupAction("job_form")]

class ClientForm(FormAction):
   def name(self):
       return "client_form"
   #
   @staticmethod
   def required_slots(tracker) :
       # type: () -> List[Text]
       """A list of required slots that the form has to fill"""
       if tracker.get_slot("assignmentType") != None:
           return ["PERSON","assignment","assignmentType"]
       else:
           return ["PERSON","assignment"]

   def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        client = "client"
        return {"assignment": self.from_entity(entity="assignment"),
        "PERSON": self.from_entity(entity="PERSON"),
        "assignmentType": self.from_entity(entity="assignmentType")}

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]

       PERSON = tracker.get_slot('PERSON')
       assignment = tracker.get_slot('assignment')
       assignmentType = tracker.get_slot('assignmentType')
       if assignmentType == None:
           zz = """okay so {} your request for the project featuring {} for your company is being processed,would you like our executives to reach you personally?""".format(PERSON,assignment)
           dispatcher.utter_message(zz)
       else:
           zz = """okay so {} your request for the {} project featuring {} for your company is being processed,would you like our executives to reach you personally?""".format(PERSON,assignmentType,assignment)
           dispatcher.utter_message(zz)

       return [SlotSet('user',"client"),FollowupAction("action_show_projects")]

class Actionclient(Action):
    def name(self):
        return "action_client"
    def run(self,dispatcher,tracker,domain):
       assignment = tracker.get_slot("assignment")
       if assignment in ui_db():
           return[SlotSet("assignmentType", "UX/UI Design")]
           return [SlotSet('user',"client"),FollowupAction("client_form")]

       if assignment in ui_db() and assignment.lower() in branding_db():
           dispatcher.utter_message("Wow {} is both a branding and a design project and you'll love it cause they're both Yellow Slice's speciality 🤩")
           return [SlotSet('user',"client"),FollowupAction("client_form")]

       if assignment in branding_db():
           return[SlotSet("assignmentType", "Brand Design")]
           return [SlotSet('user',"client"),FollowupAction("client_form")]
       if assignment == None:
           zz = """"I'm sorry ! i dont understand what project do you want help with?"""
           dispatcher.utter_message(zz)
           return [FollowupAction("client_form")]
       else:
           return [SlotSet('user',"client"),FollowupAction("client_form")]

class ShowProjects(Action):
    def name(self):
        return "action_show_projects"

    def required_slots(tracker):
        return["assignment"]
    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        client = "client"
        return {"assignment": self.from_entity(entity="assignment")}
    def run(self, dispatcher, tracker, domain):
        assignment = tracker.get_slot("assignment")
        dispatcher.utter_message("have a look at our recent {} projects here!!".format(assignment))
        return [FollowupAction("action_confirm")]

def ui_db():

    return [
    "ux & ui designs",
    "ux design",
    "ui design",
    "visual design",
    "icon design",
    "illustration",
    "svg animation",
    "packaging design",
    "web design",
    "website design",
    "app design",
    "software design",
    "ux audit",
    "ux research",
    "ux strategy",
    "interaction design"]

def branding_db():

    return  ["icon design",
      "illustration",
      "branding",
      "logo design",
      "identity design",
      "svg animation",
      "brochure design",
      "store design",
      "web design",
      "website design",
      "brand budit",
      "graphic design"]
