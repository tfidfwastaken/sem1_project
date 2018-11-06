"""
Creates a time tables based on the following inputs:
Number of hours
Number of classes
Number of subjects and their credits
Other stuff like let-off days etc.
"""

class Timetable:
    def __init__(self, hours, subj_dict):
        self._hours = hours
        # subj_dict is a dictionary with subjects as key and credits as value
        self._subj_dict = subj_dict
    
    def get_hours(self):
        return self._hours
    
    def get_subj_dict(self):
        return self._subj_dict
    
    hours = property(get_hours)
    subj_dict = property(get_subj_dict)

# Test: Example time tables
TT1 = Timetable(4, {"Maths": 2, "EC": 1, "CS": 1})
TT2 = Timetable(6, {"Maths": 2, "EC": 1, "CS": 2, "Bio": 1})

print(TT1.hours)
print(TT2.subj_dict)
