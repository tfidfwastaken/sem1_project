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
def dist_subjects(week_dict, slot_dict):
    subj_dict_list = []     # Eg: [{"s1":1, "s2":2}, {"s1":2, "s3":3}, ...]
    if sum(week_dict.values()) > sum(slot_dict.values()):
        hr_deficit = sum(week_dict.values()) - sum(slot_dict.values())
        print("Too many hours to accomodate.")
        print(f"Please reduce {hr_deficit} hours from the week or increase those many slots")
    # else: distribute the slots of each subject as evenly as possible
        

# Test: Example time tables
TT1 = Timetable(4, {"Maths": 2, "EC": 1, "CS": 1})
TT2 = Timetable(6, {"Maths": 2, "EC": 1, "CS": 2, "Bio": 1})

print(TT1.slots)
print(TT2.subj_dict)
