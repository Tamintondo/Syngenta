entrada = input('')

Lakewood_reg = {'rank' : 3, 'mon':160, 'tue': 160, 'wed':160 , 'thu':160, 'fri': 160,  'sat': 60, 'sun':60}

Lakewood_rew = {'rank' : 3, 'mon':110, 'tue': 110, 'wed':110 , 'thu':110, 'fri': 110,  'sat': 50, 'sun':50}

Ridgewood_reg = {'rank' : 5, 'mon':220, 'tue': 220, 'wed':220 , 'thu':220, 'fri':220,  'sat':150, 'sun':150}

Ridgewood_rew = {'rank' : 5, 'mon':100, 'tue':100, 'wed':100 , 'thu':100, 'fri': 100,  'sat': 40, 'sun':40}

valor_Lakewood, valor_Ridgewood = 0,0

if entrada.count('Regular')>0:
	for i in Lakewood_reg.keys():
		valor_Lakewood += Lakewood_reg.values(i)*entrada.count(Lakewood_reg.keys(i))
		valor_Ridgewood += Ridgewood_reg.values(i)*entrada.count(Ridgewood_reg.keys(i))
elif entrada.count('Reward')>0:
	for i in Lakewood_rew.keys():
		valor_Lakewood += Lakewood_rew.values(i)*entrada.count(Lakewood_rew.keys(i))
		valor_Ridgewood += Ridgewood_rew.values(i)*entrada.count(Ridgewood_rew.keys(i))
else:
	print('Erro 404, function problem, please retry')

if valor_Lakewood < valor_Ridgewood:
	print ('Lakewood')
elif valor_Lakewood > valor_Ridgewood:
	print ('Ridgewood')
else:
	print('Ridgewood')




	