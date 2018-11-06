"""
Creates a time tables based on the following inputs:
Number of slots
Number of classes
Number of subjects and their credits
Other stuff like let-off days etc.
"""

class Timetable:
    def __init__(self, slots, subj_dict):
        self._slots = slots
        # subj_dict is a dictionary with subjects as key and credits as value
        self._subj_dict = subj_dict
    
    def get_slots(self):
        return self._slots
    
    def get_subj_dict(self):
        return self._subj_dict
    
    slots = property(get_slots)
    subj_dict = property(get_subj_dict)
    
    """
    def generate_day_sched():
        Does this to the subj_dict for example:
        {"Maths": 2, "EC": 1, "CS": 1} --> ["Maths", "EC", "Maths", "CS"]
        We just need to make it a list having each subject *frequency* number
        of times and shuffle its contents
    """

# We need a function that takes a subj_dict for a whole week (week_dict)
# and makes them into 7 subj_dict's for each day
# slot_dict contains slots mapped to each day
#   like {"Mon": 6, "Tue": 6, "Wed": 4, "Thu": 6, "Fri": 5}

def dist_subjects(week_dict, slot_dict):
    subj_dict_by_day = {}     # Eg: {"Mon":{"s1":1, "s2":2}, "Tue":{"s1":2, "s3":3}, ...}
    #for day in slot_dict:
        #subj_dict_by_day[day] = {}
    if sum(week_dict.values()) > sum(slot_dict.values()):
        hr_deficit = sum(week_dict.values()) - sum(slot_dict.values())
        print("Too many hours to accomodate.")
        print(f"Please reduce {hr_deficit} hours from the week or increase those many slots")
    else:
        for subject in sorted(week_dict, key=week_dict.__getitem__, reverse=True):
            dist_value = week_dict[subject] // len(slot_dict)
            remainder = 0
            if week_dict[subject] % len(slot_dict) != 0:
                remainder = week_dict[subject] % len(slot_dict)
            for day in sorted(slot_dict, key=slot_dict.__getitem__, reverse=True):
                #print("ay")
                if day not in subj_dict_by_day:
                    subj_dict_by_day[day] = {}
                if subject not in subj_dict_by_day[day]:
                    #print(subj_dict_by_day)
                    subj_dict_by_day[day][subject] = dist_value
                    if remainder != 0:
                        subj_dict_by_day[day][subject] += 1
                        remainder -= 1
    return subj_dict_by_day

# Test: Example time tables
TT1 = Timetable(4, {"Maths": 2, "EC": 1, "CS": 1})
TT2 = Timetable(6, {"Maths": 2, "EC": 1, "CS": 2, "Bio": 1})

#print(TT1.slots)
#print(TT2.subj_dict)

# Test: the distribution algorithm
print(dist_subjects(
    {"Maths": 5, "Chem": 4, "EC": 4, "Bio": 2, "Comp": 4},
    {"Mon": 6, "Tue": 4, "Wed": 4, "Thu": 6, "Fri": 5}))
