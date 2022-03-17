# input qualifiacation by list of string
# output qualification by nested list of strings
# 1:diploma 2:bachelor 3:master 4:phd

level_lookup = {'diploma': 1, 'bachelor': 2, 'master': 3, 'phd': 4,
                              'bachelors':2, 'masters':3,
                              'BTech':2,     'MTech':3,       'PhD':4,
                              'B.Tech':2,    'M.Tech':3,      'P.H.D':4,
                              'B.tech':2,    'M.tech':3,      'P.H.d':4,
                              'B.TECH':2,    'M.TECH':3,      'Phd':4,}


def parse_qualifications(qualifications):
    parsed_qualification = []
    for qualification in qualifications:
        level = qualification.split(' ')[0]
        degree = qualification.split(' ')[2]
        level = int(level_lookup[level])
        parsed_qualification.append([level, degree])
    return parsed_qualification

def parse_qualification(qualification):
    parsed_qualification = ''
    level = qualification.split(' ')[0]
    degree = qualification.split(' ')[2]
    level = int(level_lookup[level])
    parsed_qualification=[level, degree]
    return parsed_qualification
