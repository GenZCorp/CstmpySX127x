import rx_cont as rxrun

#make this loop after every 3 minutes
SNUMBER = 0
rxrun.setuplora()
rxrun.runlora(SNUMBER)
SNUMBER = SNUMBER + 1



