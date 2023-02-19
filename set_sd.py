# symmetric difference:
# like a venn diagram, it is the intersection of
# what is in between - exclusion not inclusion!

morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)