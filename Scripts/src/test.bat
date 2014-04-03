::Test plotPerformanceLogs.py
::TODO: A unittest module is better

python plotPerformanceLogs.py

python plotPerformanceLogs.py -output LogPlot2.png

python plotPerformanceLogs.py -output LogPlot3.png ../data/results_firstrun.txt

python plotPerformanceLogs.py -output LogPlot4.png ../data/results_firstrun.txt ../data/results_secondrun.txt ../data/results_baseline.txt

del *.png