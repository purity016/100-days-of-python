import sympy as sy
t = sp.symbols('t')
s = t**3 + 2*t**2 + 4*t + 2
v = sp.diff(s, t)
a = sp.diff(v, t)

t_val = 3
v_at_t3 = v.subs(t, t_val)
a_at_t3 = a.subs(t, t_val)

print(f"Tangential velocity at t={t_val}: {v_at_t3}")
print(f"Tangential acceleration at t={t_val}: {a_at_t3}")