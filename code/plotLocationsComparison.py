import math
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import world_set
import gc
import company

winsVSlosses = []
for i in range(2):
	winsVSlosses += [0]



for i in range(1):
	gc.collect()
	import world_set
	clients, companies = world_set.setupWorld(50, 4, verbose=True, learnQ=False)

	for j in range(200):
		world_set.step(clients, companies, verbose=False)

	rankings = world_set.generateStatesByActives(companies)

	if(rankings[0].getId() == "COMP-1"):
		winsVSlosses[0] += 1
	else:
		winsVSlosses[1] += 1

print("FINISHED")
plt.figure()
plt.bar(["Wins", "Losses"], winsVSlosses)
plt.xlabel("Local")
plt.ylabel("Number wins")
plt.title("Number wins of the RL company")
#plt.show()


print(winsVSlosses[0])




