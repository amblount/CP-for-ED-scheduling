# Emergency Medicine Scheduling

After seaking with the UCSF cheif residents it was clear there were a lot of constraints which I needed to include and define in
the system to improve the manual scheduling process which takes place currently.

### How it currently works

Medical practitioners go through formal classroom training or medical school and they complete in person [residency programs](https://en.wikipedia.org/wiki/Residency_(medicine)) to learn 
the hands on skills required to practice medicine. There are many portions of the hospital which the residents are exposed to to enable
the future licesnsed physicians to make a decision about the type of medicine they would like to practice. Once of the residency rotations
and possible specialties is in the Emergency Department as an Emergency Medicine physician. This residecy program is slightly different
than traditional residency programs because the emergency room is open 24 hours per day and 7 days per week, and needs to be staffed
around the clock. Residents are scheduled in blocks to work in the emergency department and block are composed of four week. Each year as new residents
are accepted into the UCSF residency program they are also scheduled to complete blocks in the Emergency medicine rotation. 

Currently the emergency department receives csv file of residents and their availability in the ED for each week of the year. If residents are available 
in the ED, then they need to be placed on the schedule in the ED.

### Current composition of the UCSF Emergency Department

The UCSF Emergency Department is composed of 4 different facilities with different shifts, each shift is 8-hours in length. There are current regulations in place which state that residents must have 8-hours off between shifts and residents must not work more than 7 consecutive days in a row. 

### Other constraints

- clinicals
- diacdics
- exams

These three residency requirements are not shifts but they are a critical part of the residents learning experience and they are shorter in time span when they do occur around 2-3 hours. 

### Current software

Currently the chief resident at each facility is doing the manual scheduling and using a generic scheduling tool to create block schedules for the month. The software is not performing very well at the moment and the resident is required to go in and update the schedule each day to make sure the software falls in line with the system constraints. 


