required_skills = {"Python", "SQL", "Git", "Docker"}
skills_1candidate = {"Python", "SQL", "Git", "Docker", "Kubernetes"}
skills_2candidate = {"Python", "SQL", "JavaScript"}
skills_3candidate = {"Python", "SQL", "Git", "HTML/CSS"}
print("Требуемые навыки: ", required_skills)
print("Кандидат 1: ", skills_1candidate)
print("Кандидат 2: ", skills_2candidate)
print("Кандидат 3: ", skills_3candidate)

print("Кандидат 1")
print(f"а) Есть ли все требуемые навыки: {required_skills.issubset(skills_1candidate)}")
print(f"б) Какие требуемые отсутствуют: {required_skills.difference(skills_1candidate)}")
print(f"в) Какие дополнительные навыки есть : {skills_1candidate.difference(required_skills)}")

print("Кандидат 2")
print(f"а) Есть ли все требуемые навыки: {required_skills.issubset(skills_2candidate)}")
print(f"б) Какие требуемые отсутствуют: {required_skills.difference(skills_2candidate)}")
print(f"в) Какие дополнительные навыки есть : {skills_2candidate.difference(required_skills)}")

print("Кандидат 3 ")
print(f"а) Есть ли все требуемые навыки: {required_skills.issubset(skills_3candidate)}")
print(f"б) Какие требуемые отсутствуют: {required_skills.difference(skills_3candidate)}")
print(f"в) Какие дополнительные навыки есть : {skills_3candidate.difference(required_skills)}")