### Polya Urnen-Experiment (17.10.2017)

import random, pylab as plt

nexp = 10 # Anzahl der Experimente
niter = 100 # Anzahl der Iterationen (Züge aus der Urne)
rednum = blacknum = 1 # Anzahl der Kugeln in der Urne zu Beginn
reinforce = 1 # Positive / negative Verstärkung

for i in range(0, nexp):
    frac = []
    nred = rednum
    nblack = blacknum

    for j in range(0, niter):
        if random.random() < nred / float(nred + nblack): # Zufälliges Ziehen einer Kugel
            nred = nred + reinforce # Zurücklegen mit Verstärkung

        else:
            nblack = nblack + reinforce # Zurücklegen mit Verstärkung
        frac.append(nred / float(nred + nblack))


    plt.figure(1, figsize=(20,10))

    # PLOT
    plt.subplot(211)
    plt.title('Polya Urnen-Experiment (Experimente: %s, Züge: %s, Reinforcement: %s)'%(nexp,niter,reinforce))
    plt.plot(frac)
    plt.xlabel('Iteration')
    plt.ylabel('Anteil roter Kugeln')
    plt.grid()

    # HISTOGRAMM
    plt.subplot(212)
    plt.hist(frac, normed=True, bins=10, alpha=0.75)
    # plt.xticks((0.0, 1.0))
    plt.xlabel('Anteil roter Kugeln')
    plt.ylabel('Häufigkeit')
    plt.grid()

plt.show()