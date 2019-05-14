import os
## + """ "{}" """.format(var) +

def create_story(file_name,var):
    x ="""
- i am looking for work as a [{}](post)
- i am looking to get a [job](user) as an [{}](post) do you have any post open
- i am a professional [{}](post)
- are you recruiting [{}](post)
- would you hire a [{}](post)?
- do you hire a [{}](post)?
- are you any for hiring [{}](post)?
- is there any vacancy for [{}](post)
""".format(var,var,var,var,var,var,var,var)

    file_name.write(x)

db = [
"UX Designer ",
"UX Lead ",
"UI Designer ",
"UI Lead ",
"Graphic Designer",
" Brand Lead ",
"Design Director",
" Illustrator ",
"3D Artist ",
"Product Manager",
" Content Writer",
" Business Development ",
"Manager ",
"HTML Developer",
" PHP Developer ",
"Animator",
" Accounts",
"executive",
" Project Manager",
" Office boy",
" Psychologist "]

with open("data/jobs.md",'a') as ff:
    for d in db:
        create_story(ff,d.lower())
