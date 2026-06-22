cia = set(["Bond", "Smith", "Hunt"])
mi6 = set(["Bond", "Power", "Hunt"])
kgb = set(["Petrov", "Hunt", "Ivanov"])

double_agent = cia.intersection(mi6)
double_agent_kgb = double_agent.intersection(kgb)
double_agent_nato = double_agent.difference(kgb)
agent_nato = cia.symmetric_difference(mi6)
print(*double_agent_nato, "- Двойной агент, ", *agent_nato, "- не пересекаются, ", *double_agent_kgb, "- есть в КГБ")