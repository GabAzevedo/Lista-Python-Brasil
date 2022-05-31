População_A = 8000 
Crescimento_A = 1.03
População_B = 200000
Crescimento_B = 1.015

ano = 1
while (População_A != População_B):
    População_A *= Crescimento_A
    População_B *= Crescimento_B
    ano += 1

print(f'Será necessário {ano} anos para que a População A, ultrapasse  o crescimento da População B')