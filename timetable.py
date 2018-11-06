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
    
    

# Test: Example time tables
TT1 = Timetable(4, {"Maths": 2, "EC": 1, "CS": 1})
TT2 = Timetable(6, {"Maths": 2, "EC": 1, "CS": 2, "Bio": 1})

print(TT1.slots)
print(TT2.subj_dict)
