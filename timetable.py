"""
Creates a time tables based on the following inputs:
Number of slots
Number of classes
Number of subjects and their credits
Other stuff like let-off days etc.
"""

class Timetable:
    def __init__(self, tt_dict):
        self._tt_dict = tt_dict
    
    def get_tt_dict(self):
        return self._tt_dict
    
    tt_dict = property(get_tt_dict)
    
    """
    def generate_day_sched():
        Does this to the subj_dict for example the sub-dict in tt_dict:
        {"Maths": 2, "EC": 1, "CS": 1} --> ["Maths", "EC", "Maths", "CS"]
        We just need to make it a list having each subject *frequency* number
        of times and shuffle its contents
    """


""" TODO: Delete this mess, once refactored
# Takes the quota of subjects per week and slots per week
# and makes a time table in dict form
def dist_subjects(week_dict, slot_dict):
    tt_dict = {}     # Eg: {"Mon":{"s1":1, "s2":2}, "Tue":{"s1":2, "s3":3}, ...}
    if sum(week_dict.values()) > sum(slot_dict.values()):
        hr_deficit = sum(week_dict.values()) - sum(slot_dict.values())
        print("Too many hours to accomodate.")
        print(f"Please reduce {hr_deficit} hours from the week or increase those many slots")
    else:
        # Just making tt_dict's keys and initializing to empty/zero
        for subject in week_dict:
            for day in slot_dict:
                    if day not in tt_dict:
                        tt_dict[day] = {}
                    if subject not in tt_dict[day]:
                        tt_dict[day][subject] = 0
        daily_quota = slot_dict
        subj_quota = week_dict
        while sum(daily_quota.values()) != 0:
            # take day with max quota and increment with a subject with max quota
            day = max(daily_quota, key=daily_quota.__getitem__)
            subj = max(subj_quota, key=subj_quota.__getitem__)
            tt_dict[day][subj] += 1
            daily_quota[day] -= 1
            subj_quota[subj] -= 1
    return tt_dict
"""

def gen_master_freq(sub_dict, slot_dict, sec_list):
    if sum(sub_dict.values()) > sum(slot_dict.values()):
        hr_deficit = sum(sub_dict.values()) - sum(slot_dict.values())
        print("Too many hours to accomodate.")
        print(f"Please reduce {hr_deficit} hours from the week or increase those many slots")
    else:
        table = dict(zip(slot_dict, [{}] * len(slot_dict)))
        for day in table:
            table[day] = dict(zip(sec_list, [{}] * len(sub_dict)))
            for sec in sec_list:
                table[day][sec] = dict(zip(sub_dict, [0] * len(sub_dict)))
        return table

""" TODO: Remove later
# Test: the distribution algorithm
tt1 = dist_subjects(
    {"Maths": 5, "Chem": 4, "EC": 4, "Bio": 2, "Comp": 4, "CSLab": 2, "ChemLab": 2},
    {"Mon": 6, "Tue": 6, "Wed": 4, "Thu": 6, "Fri": 5})
tt2 = dist_subjects(
    {"Cooking": 3, "Carpentry": 5, "Pole-Vaulting": 4},
    {"Mon": 4, "Wed": 5, "Fri": 3})

# Test: Example time tables
TT1 = Timetable(tt1)
TT2 = Timetable(tt2)

print(TT1.tt_dict)
print(TT2.tt_dict)
"""
tt = gen_master_freq(
    {"Maths": 3, "Phy": 5, "Chem": 4},
    {"Mon": 4, "Wed": 5, "Fri": 3}, ["A", "B", "C"])

print(tt)
